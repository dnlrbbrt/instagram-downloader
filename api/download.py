from http.server import BaseHTTPRequestHandler
import json
import urllib.parse
import yt_dlp


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        url = params.get("url", [""])[0]

        if not url:
            self._json(400, {"error": "Missing url parameter"})
            return

        try:
            ydl_opts = {
                "quiet": True,
                "no_warnings": True,
                "socket_timeout": 8,
                "extractor_args": {"instagram": {"include_feed_data": ["1"]}},
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)

            if not info:
                self._json(404, {"error": "No video found at that link"})
                return

            video_url = self._best_url(info)

            if not video_url:
                self._json(404, {"error": "Could not extract a video URL from this post"})
                return

            uploader = (info.get("uploader") or info.get("uploader_id") or "instagram")
            title = (info.get("title") or "video").strip()[:40].replace(" ", "_")
            filename = f"{uploader}_{title}.mp4"

            self._json(200, {"url": video_url, "filename": filename})

        except yt_dlp.utils.DownloadError as exc:
            msg = str(exc).lower()
            if "private" in msg or "login" in msg or "authentication" in msg:
                self._json(403, {"error": "This account is private — only public posts can be downloaded"})
            elif "not found" in msg or "does not exist" in msg:
                self._json(404, {"error": "Post not found or has been deleted"})
            else:
                self._json(500, {"error": f"Could not download: {exc}"})
        except Exception as exc:
            self._json(500, {"error": str(exc)})

    def do_OPTIONS(self):
        self.send_response(200)
        self._cors()
        self.end_headers()

    def _best_url(self, info):
        formats = info.get("formats") or []
        mp4 = [f for f in formats if f.get("ext") == "mp4" and f.get("url")]
        if mp4:
            return max(mp4, key=lambda f: f.get("height") or 0)["url"]
        if formats:
            with_url = [f for f in formats if f.get("url")]
            if with_url:
                return max(with_url, key=lambda f: f.get("height") or 0)["url"]
        return info.get("url")

    def _json(self, status, data):
        body = json.dumps(data).encode()
        self.send_response(status)
        self._cors()
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")

    def log_message(self, fmt, *args):
        pass

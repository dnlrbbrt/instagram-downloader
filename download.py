#!/usr/bin/env python3
"""
Instagram Video Downloader (command-line)
Requires: pip install yt-dlp
Usage:    python download.py <instagram_url>
"""

import sys
import os

try:
    import yt_dlp
except ImportError:
    print("Error: yt-dlp is not installed.")
    print("Run:  pip install yt-dlp")
    sys.exit(1)


def download(url: str, output_dir: str = ".") -> None:
    ydl_opts = {
        "outtmpl": os.path.join(output_dir, "%(uploader)s_%(id)s.%(ext)s"),
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "merge_output_format": "mp4",
        "quiet": False,
        "no_warnings": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python download.py <instagram_url>")
        print("Example: python download.py https://www.instagram.com/p/ABC123/")
        sys.exit(1)

    url = sys.argv[1]
    print(f"Downloading: {url}\n")
    try:
        download(url)
        print("\nDone!")
    except yt_dlp.utils.DownloadError as e:
        print(f"\nFailed: {e}")
        sys.exit(1)

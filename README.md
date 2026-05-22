# Instagram Video Downloader

A clean, ad-free Instagram video & reel downloader. Use it in your browser (works on phone) or from the command line.

## Web App (Phone / Browser)

Visit your GitHub Pages URL:
```
https://<your-username>.github.io/<repo-name>/
```

1. Open Instagram → find the video → tap **⋯** → **Copy link**
2. Paste the link into the web app → tap **Download**
3. Tap **Save** to download the file

> Only works on **public** accounts.

## Command-Line (Desktop)

**Install dependency:**
```bash
pip install yt-dlp
```

**Download a video:**
```bash
python download.py https://www.instagram.com/p/POSTID/
```

The video is saved as `username_postid.mp4` in the current directory.

## How It Works

The web app sends your link to [cobalt.tools](https://cobalt.tools) — a free, open-source video downloader API with no ads and no tracking. The command-line script uses [yt-dlp](https://github.com/yt-dlp/yt-dlp), the gold-standard open-source download tool.

## Deploy to GitHub Pages

1. Push this repo to GitHub
2. Go to **Settings → Pages**
3. Set Source to **Deploy from a branch**, branch `main`, folder `/ (root)`
4. Save — your site will be live at `https://<username>.github.io/<repo>/`

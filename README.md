# Instagram Video Downloader

A clean, ad-free Instagram video & reel downloader. Use it in your browser (works on phone) or from the command line.

## Web App (Phone / Browser)

Visit your Vercel URL (set up once — see below):
```
https://instagram-downloader-<hash>.vercel.app
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

The web app calls a serverless API function (`/api/download`) that uses [yt-dlp](https://github.com/yt-dlp/yt-dlp) to extract the video URL from Instagram, then your browser downloads it directly. No ads, no tracking.

## Deploy to Vercel (free)

1. Go to [vercel.com](https://vercel.com) and sign in with GitHub
2. Click **Add New → Project** and import `instagram-downloader`
3. Leave all settings as default and click **Deploy**
4. Your live URL appears — bookmark it on your phone

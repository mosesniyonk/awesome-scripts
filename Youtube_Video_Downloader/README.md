# Youtube Video Downloader Script

Downloads YouTube videos or audio from a single video URL or a playlist using `yt-dlp`.

## Requirements

- Python 3.8+
- FFmpeg (for audio conversion and video merging)

## Installation

1. Create virtual environment:
   ```
   python -m venv venv
   ```

2. Activate virtual environment (Bash or fish):
    ```
    source venv/bin/activate
    ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script:
```
python download_video.py
```

You'll be prompted for:
- YouTube video or playlist URL
- Download folder path
- Media type (audio or video)
- Video quality if choosing video (e.g., 720p, 1080p)

## Fixed Issues

- ✅ Switched to `yt-dlp` for more reliable downloads
- ✅ Updated the CLI to accept a single video URL or a playlist

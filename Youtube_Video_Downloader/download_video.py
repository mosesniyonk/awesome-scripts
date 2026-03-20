import os
import sys
import shutil
from yt_dlp import YoutubeDL

QUALITY_CHOICES = {
    "360p": 360,
    "480p": 480,
    "720p": 720,
    "1080p": 1080,
    "4k": 2160,
    "8k": 4320,
}


def is_playlist_url(url):
    return "/playlist" in url or ("list=" in url and "v=" not in url)


def parse_quality(quality):
    if not quality:
        return QUALITY_CHOICES["720p"]

    normalized = quality.strip().lower()
    if normalized in QUALITY_CHOICES:
        return QUALITY_CHOICES[normalized]
    if normalized.endswith("p"):
        normalized = normalized[:-1]
    if normalized.isdigit():
        return int(normalized)
    raise ValueError("Choose one of: 360p, 480p, 720p, 1080p, 4k, 8k.")


def format_quality_label(quality_height):
    if quality_height == 2160:
        return "4k"
    if quality_height == 4320:
        return "8k"
    return f"{quality_height}p"


def prompt_quality():
    quality_prompt = (
        "Enter the quality of the video "
        "(360p, 480p, 720p, 1080p, 4k, 8k) [default: 720p]: "
    )
    return input(quality_prompt).strip() or "720p"


def get_available_video_heights(url):
    options = {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
    }

    with YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=False)

    heights = set()
    for fmt in info.get("formats", []):
        if fmt.get("vcodec") != "none" and fmt.get("height"):
            heights.add(fmt["height"])

    return heights


def format_eta(seconds):
    if seconds is None:
        return "--:--"

    seconds = max(0, int(seconds))
    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    if hours:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def build_progress_bar(percent):
    columns = shutil.get_terminal_size((80, 20)).columns
    bar_width = max(8, min(12, columns - 38))
    filled = min(bar_width, int(percent / 100 * bar_width))
    return "[" + ("█" * filled) + ("░" * (bar_width - filled)) + "]"


def download_progress_hook(progress):
    if progress.get("status") == "downloading":
        total = progress.get("total_bytes") or progress.get("total_bytes_estimate")
        downloaded = progress.get("downloaded_bytes", 0)
        percent = (downloaded / total * 100) if total else 0
        eta = format_eta(progress.get("eta"))
        speed = progress.get("speed")
        speed_text = "--"
        if speed:
            units = ["B/s", "KiB/s", "MiB/s", "GiB/s"]
            value = float(speed)
            unit_index = 0
            while value >= 1024 and unit_index < len(units) - 1:
                value /= 1024
                unit_index += 1
            speed_text = f"{value:.1f} {units[unit_index]}"
        bar = build_progress_bar(percent)
        sys.stdout.write(f"\r\033[2K{percent:3.0f}% {bar} ETA {eta} S {speed_text}")
        sys.stdout.flush()
    elif progress.get("status") == "finished":
        sys.stdout.write("\r\033[2K100% [████████████] ETA 00:00 S --")
        sys.stdout.flush()


def download_youtube_media(url, folder_path, quality, media_type):
    output_template = os.path.join(folder_path, "%(title)s.%(ext)s")
    options = {
        "outtmpl": output_template,
        "noplaylist": not is_playlist_url(url),
        "quiet": True,
        "no_warnings": True,
        "noprogress": True,
        "progress_hooks": [download_progress_hook],
    }

    if media_type == "audio":
        options.update(
            {
                "format": "bestaudio/best",
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }
                ],
            }
        )
    else:
        height = parse_quality(quality)
        available_heights = get_available_video_heights(url)
        if height not in available_heights:
            available = ", ".join(
                format_quality_label(value) for value in sorted(available_heights)
            )
            print(f"{format_quality_label(height)} is not available for this video.")
            print(f"Available video qualities: {available}")
            return

        options.update(
            {
                "format": f"bestvideo[height={height}]+bestaudio/best[height={height}]",
                "merge_output_format": "mp4",
            }
        )

    with YoutubeDL(options) as ydl:
        print("Downloading full video...")
        ydl.download([url])
        sys.stdout.write("\n")
        print("Download completed!")


url = input("Enter the URL of the YouTube video or playlist: ")
folder_path = input("Enter the path of the folder where you want to save the videos: ")
media_type = input("Enter the media type (audio or video): ")

if media_type == "video":
    quality = prompt_quality()
else:
    quality = None

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

download_youtube_media(url, folder_path, quality, media_type)

import yt_dlp
import os

def download_audio(url):
    """Download YouTube audio in 320kbps MP3 format."""

    # ensure folder exists
    os.makedirs('downloads', exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info).replace('.webm', '.mp3')
        return filename
    return None


if __name__ == '__main__':
    youtube_urls = [
        "https://www.youtube.com/watch?v=Jm48pJVy3AY",
        "https://www.youtube.com/watch?v=Y6q81V9POZU",
        "https://www.youtube.com/watch?v=cwb_IZv7kDw",
        "https://www.youtube.com/watch?v=lROByWaWtcg",
        "https://www.youtube.com/watch?v=_cQDAX27bmQ",
        "https://www.youtube.com/watch?v=cuXW9a2OA1g",
        "https://www.youtube.com/watch?v=Y8u4kRdNmCY",
        "https://www.youtube.com/watch?v=zgPb1qkprvY",
        "https://www.youtube.com/watch?v=GMh-mTTOnkg",
        "https://www.youtube.com/watch?v=uO1L2U18rTE",
        "https://www.youtube.com/watch?v=ZiZ8KdraJ-0",
        "https://www.youtube.com/watch?v=rngLO3tF2mA",
        "https://www.youtube.com/watch?v=eK7RscW7nF0",
        "https://www.youtube.com/watch?v=S8-z26rBPLw",
        "https://www.youtube.com/watch?v=wurF5may3cE"
    ]

    for url in youtube_urls:
        try:
            output_file = download_audio(url)
            print(f"Downloaded: {output_file}")
        except Exception as e:
            print(f"Failed to download {url}: {e}")

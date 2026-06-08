import yt_dlp
import os

def download_audio(url):
    os.makedirs('downloads', exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'flac',
        }],
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info).rsplit('.', 1)[0] + '.flac'
        return filename


if __name__ == '__main__':
    youtube_urls = []
    for url in youtube_urls:
        try:
            output_file = download_audio(url)
            print(f"Downloaded: {output_file}")
        except Exception as e:
            print(f"Failed to download {url}: {e}")

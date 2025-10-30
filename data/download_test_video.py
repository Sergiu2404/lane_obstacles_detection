import os
import yt_dlp

url = "https://www.youtube.com/shorts/N7-oWwu7gME?t=8&feature=share"
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
output_path = os.path.join(downloads_folder, "test_pothole_model.mp4")

ydl_opts = {
    "outtmpl": output_path,  # save as full path
    "format": "bestvideo+bestaudio/best",  # best quality
    "merge_output_format": "mp4",          # merge video/audio
    "quiet": False                         # show progress
}

# download
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print(f"\nVideo saved to: {output_path}")
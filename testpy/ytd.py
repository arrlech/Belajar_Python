import argparse
from pytube import YouTube

VIDEO_SAVE_DIRECTORY = "./videos"
AUDIO_SAVE_DIRECTORY = "./audio"

def download_video(video_url, output_directory, resolution):
    def on_progress(stream, chunk, remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - remaining
        percentage = (bytes_downloaded / total_size) * 100
        print(f"\rDownload progress: {percentage:.2f}%", end='')

    # Hilangkan karakter tanda tanya (?) dari URL
    video_url = video_url.split('?')[0]
    
    video = YouTube(video_url)
    
    if resolution:
        video_stream = video.streams.filter(res=resolution, file_extension="mp4").first()

        if not video_stream:
            print(f"Video resolution {resolution} not available. Trying highest resolution.")
            video_stream = video.streams.get_highest_resolution()
    else:
        print("Resolusi tidak diberikan. Mencoba resolusi tertinggi.")
        video_stream = video.streams.get_highest_resolution()

    try:
        # Pertanyaan untuk fitur real-time progress
        enable_progress = input("Ingin melihat progres unduhan secara real-time? (yes/no): ")
        if enable_progress.lower() == 'yes':
            video_stream.download(output_directory, on_progress=on_progress)
        else:
            video_stream.download(output_directory)
        print("\nVideo was downloaded successfully.")
    except Exception as e:
        print(f"Failed to download video. Error: {e}")

def download_audio(video_url, output_directory):
    def on_progress(stream, chunk, remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - remaining
        percentage = (bytes_downloaded / total_size) * 100
        print(f"\rDownload progress: {percentage:.2f}%", end='')

    # Hilangkan karakter tanda tanya (?) dari URL
    video_url = video_url.split('?')[0]

    video = YouTube(video_url)
    audio_stream = video.streams.filter(only_audio=True).first()

    try:
        # Pertanyaan untuk fitur real-time progress
        enable_progress = input("Ingin melihat progres unduhan secara real-time? (yes/no): ")
        if enable_progress.lower() == 'yes':
            audio_stream.download(output_directory, on_progress=on_progress)
        else:
            audio_stream.download(output_directory)
        print("\nAudio was downloaded successfully.")
    except Exception as e:
        print(f"Failed to download audio. Error: {e}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", required=True, help="URL to YouTube video")
    ap.add_argument("-a", "--audio", required=False, help="Download audio only", action="store_true")
    args = vars(ap.parse_args())

    output_directory = VIDEO_SAVE_DIRECTORY if not args["audio"] else AUDIO_SAVE_DIRECTORY

    if args["audio"]:
        download_audio(args["video"], output_directory)
    else:
        # Pertanyaan 1: Menentukan Resolusi Video Manual
        resolution = input("Ingin menentukan resolusi video secara manual? (360/420/720/1080/1444/2440/dst, atau enter untuk resolusi tertinggi): ")

        # Pertanyaan 2: Menentukan Direktori Penyimpanan
        custom_directory = input("Ingin menentukan direktori penyimpanan khusus? (yes/no): ")
        if custom_directory.lower() == 'yes':
            output_directory = input("Tolong berikan path lengkap direktori penyimpanan: ")

        # Pertanyaan 4: Mengunduh Semua Resolusi yang Tersedia
        if not resolution:
            download_video(args["video"], output_directory, resolution)
        else:
            print("Resolusi tidak diberikan. Mencoba resolusi tertinggi.")
            download_video(args["video"], output_directory, None)

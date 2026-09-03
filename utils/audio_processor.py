# accept any audio/video and 
import yt_dlp
from pydub import AudioSegment # going to use for chunking later 
import os

DOWNLOAD_DIR = "downloades" # directory for saving all the downloads from this
os.makedirs(DOWNLOAD_DIR, exist_ok = True)

def download_youtube_audio(url : str) -> str:
    output_path = os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s") # whatever be the name of the actual file
    ydl_opts = {
        "format" : "bestaudio/best",
        "outtmpl" : output_path,
        "postprocessos" : [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec" : "wav",
                "prefferedquality" : "192",
            }
        ],
        "quiet" : True # hides how everything (above code{prolog}) is working, remove this if you dont want to see the progress
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download = True)
        filename = ydl.prepare_filename(info).replace("")
    return filename

# paste youtube video link here
# download_youtube_audio("https://youtu.be/xlYJhtL0qbQ?si=wj3Jo36HrcEKyyHG") 

# if we want to use a file which is not actually available on youtube
def convert_to_wav(input_path : str) -> str:
    """convert any audio/video file to WAV format using pydub."""
    output_path = os.path.splitext(input_path)[0]
    audio = AudioSegment.from_file(input_path) # detect the type of file you are giving 
    audio = audio.set_channels(1).set_frame_rate(16000) # set to mono audio , set to 16 khz 
    audio.export(output_path, format = "wav") 
    return output_path

def chunk_audio(wav_path : str, chunk_minutes: int = 10) -> list:
    audio = AudioSegment.from_wav(wav_path)
    chunk_ms = chunk_minutes*60*1000 # ms -> mili second

    chunks = []

    for i, start in enumerate(range(0, len(audio), chunk_ms)):
        chunk = audio[start: start+chunk_ms]
        chunk_path = f"{wav_path}_chunk_{i}.wav"
        chunk.export(chunk_path, format = "wav")

        chunks.append(chunk_path)

    return chunks

# we want to create a function which can convert dual audio to mono audio and preferable to our whisper ai model 
# whisper ai model -> prefers 16 khz
def process_input(source: str) -> list:
    if source.startswith("http://") or source.startswith("https://"):
        print("Detected YouTube URL, Downloading audio....")
        wav_path = download_youtube_audio(source)

    else:
        print("Detected local file. Converting o WAV...")
        wav_path = convert_to_wav(source)

    print("Chunking Audio .....")
    chunks = chunk_audio(wav_path)
    print(f"Audio read - {len(chunks)} chunk(s) created.")
    return chunks

from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from googletrans import Translator

def download_spanish_video_and_translate_transcript(video_url):
    """Downloads a Spanish YouTube video and its transcript, translating the transcript to English."""

    try:
        yt = YouTube(video_url)

        # Download the video (highest resolution)
        print(f"Downloading video: {yt.title}")
        stream = yt.streams.get_highest_resolution()
        stream.download()  # Downloads to current directory.  You can specify a path here.
        print("Video download complete.")

        # Get the transcript (try Spanish first, then auto-detect if not available)
        try:
            transcript = YouTubeTranscriptApi.get_transcript(yt.video_id, languages=['es']) # Try Spanish
        except:
            try:
                transcript = YouTubeTranscriptApi.get_transcript(yt.video_id) # Auto-detect
            except Exception as e:
                print(f"Error getting transcript: {e}.  Video downloaded, but no transcript available.")
                return

        # Translate the transcript to English
        translator = Translator()
        translated_transcript = []


        for entry in transcript:
            try:  # Handle potential translation errors
                translated_text = translator.translate(entry['text'], dest='en').text
                translated_transcript.append({'text': translated_text, 'start': entry['start'], 'duration': entry['duration']})
            except Exception as e:
                print(f"Translation error: {e}")
                translated_transcript.append({'text': "[Translation Error]", 'start': entry['start'], 'duration': entry['duration']})  # Add placeholder for errors


        # Save the translated transcript to a file (e.g., SRT format)
        with open(f"{yt.title}_translated.txt", "w", encoding="utf-8") as f: #  You can adapt this to save as .srt if needed
            for entry in translated_transcript:
                f.write(entry['text'] + '\n')  # Basic text format. For SRT, see below


        print("Transcript downloaded and translated.")

    except Exception as e:
        print(f"An error occurred: {e}")




# Example usage: Replace with the actual YouTube video URL
video_url = "https://www.youtube.com/watch?v=iY6ldZKEZwI&t=1574s" # replace with your URL
download_spanish_video_and_translate_transcript(video_url)


#  Code to save as .srt (replace the above "with open..." block):
"""
with open(f"{yt.title}_translated.srt", "w", encoding="utf-8") as f:
    for i, entry in enumerate(translated_transcript):
        f.write(str(i+1) + '\n')
        start_time = convert_seconds_to_srt_timestamp(entry['start'])
        end_time = convert_seconds_to_srt_timestamp(entry['start'] + entry['duration'])
        f.write(f"{start_time} --> {end_time}\n")
        f.write(entry['text'] + '\n\n')


def convert_seconds_to_srt_timestamp(seconds):
    milliseconds = int(round(seconds * 1000))
    m, s = divmod(milliseconds // 1000, 60)
    h, m = divmod(m, 60)
    s, ms = divmod(milliseconds, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"

"""



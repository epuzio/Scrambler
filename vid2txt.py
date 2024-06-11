#copied from this article: https://www.geeksforgeeks.org/extract-speech-text-from-video-in-python/
import speech_recognition as sr 
import moviepy.editor as mp 
import time
from pydub import AudioSegment
  
VIDEO_PATH = "amar video.mp4"
AUDIO_PATH = "amar"
AUDIO_SEGMENT_LENGTH = 58000
AUDIO_SEGMENT_POSTFIX = "_segment"
TXT_PATH = "amar-txt"

# Load the video 
video = mp.VideoFileClip(VIDEO_PATH) 
  
# Extract the audio from the video 
audio_file = video.audio 
audio_file.write_audiofile(f"{AUDIO_PATH}.wav") 
  
# # Initialize recognizer 
# r = sr.Recognizer() 

# # Load the audio file
# with sr.AudioFile(f"{AUDIO_PATH}.wav") as source:
#     data = r.record(source)

# #only works for 1 minute of audio
# #used this stack overflow post to help: https://stackoverflow.com/questions/62719408/speech-recognition-python-having-strange-request-error
# audio = AudioSegment.from_wav(f"{AUDIO_PATH}.wav")
# length_audio = len(audio)
# segment_paths = []
# for i, seg in enumerate(range(0, length_audio, AUDIO_SEGMENT_LENGTH)):
#     segment_audio = audio[seg:seg + AUDIO_SEGMENT_LENGTH]
#     segment_path = f"{AUDIO_PATH}_{AUDIO_SEGMENT_POSTFIX}_{i}.wav"
#     segment_audio.export(segment_path, format="wav")
#     segment_paths.append(segment_path)

# print("Writing text:")
# with open(f"{TXT_PATH}.txt", "a") as file:
#     print("output file:", f"{TXT_PATH}.txt")
#     for i, segment_path in enumerate(segment_paths):
#         if(i == 0) or (i == 1):
#             continue
#         # Initialize recognizer 
#         r = sr.Recognizer() 

#         # Load the audio file 
#         with sr.AudioFile(f"{segment_path}") as source: 
#             data = r.record(source) 
            
#             # Convert speech to text with retry mechanism
#             text = r.recognize_google(data, key="AIzaSyC4kJbqk_1FfKieqOv6OX9ylwjzXgo5c6g")
#             print("Text: ", text[:30], "...")

#             # Save the text to a .txt file
#             file.write(text)
#             file.write("\n")
#         print("Wrote segment", f"{segment_path}: {i}/{len(segment_paths)}")
        

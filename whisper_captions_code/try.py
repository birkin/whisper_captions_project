import whisper

# Load the QuickTime file
video = whisper.VideoFileClip( '../../videos/09_Gray_building.mov' )

# Extract the audio from the video
audio = video.audio

# Convert the audio to text using speech-to-text
text = audio.to_text()

# Write the text to a file
with open( "../../audio_text_output/audio_text.txt", "w" ) as f:
    f.write(text)

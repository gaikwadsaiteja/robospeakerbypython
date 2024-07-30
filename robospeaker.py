from gtts import gTTS
import os

# Initialize gTTS with the text
tts = gTTS(text="Hello, ?,mr sai teja,how are you doing", lang='te')

# Save the spoken text as an MP3 file
tts.save("output.mp3")

# Play the MP3 file (this command works on Windows)
os.system("start output.mp3")

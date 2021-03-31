from gtts import gTTS
import os
text = 'Welcome to GirlScript Summer of Code!'
language = 'en'
myobj = gTTS(text=text, lang=language, slow=False)
myobj.save("audio.mp3")
os.system("mpg321 audio.mp3")
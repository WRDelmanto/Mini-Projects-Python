from gtts import gTTS  # Google Text-to-Speech
import os

fileName = 'test.mp3'

myText = "Testing, 1, 2, 3"
language = "en"

myobj = gTTS(text=myText, lang=language, slow=False)

myobj.save(fileName)
# os.system(F"start {fileName}")

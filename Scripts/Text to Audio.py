# Importing the required module
from gtts import gTTS
from playsound import playsound

# File name
fileName = 'test.mp3'

# Text input
text = "Testing, 1, 2, 3"

# Language selection
language = 'en'

# Creating an instance of the gTTS class
speech = gTTS(text=text, lang=language, slow=False)

# Saving the converted audio file
speech.save(fileName)

# Playing the converted audio file
playsound(fileName)

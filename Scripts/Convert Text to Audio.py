# Importing the required module
from gtts import gTTS
from playsound import playsound


def textToAudio(text, language):
    # File name
    fileName = "test.mp3"

    # Creating an instance of the gTTS class
    speech = gTTS(text=text, lang=language, slow=False)

    # Saving the converted audio file
    speech.save(fileName)

    # Playing the converted audio file
    playsound(fileName)


textToAudio("Testing, 1, 2, 3", "en")

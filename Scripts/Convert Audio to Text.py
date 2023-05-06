import speech_recognition as sr


def audioToText():
    # Initialize the recognizer
    r = sr.Recognizer()

    # Set the language
    lan = 'en-US'

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Recognize speech using Google Speech Recognition
    try:
        text = r.recognize_google(audio, language=lan)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))


audioToText()

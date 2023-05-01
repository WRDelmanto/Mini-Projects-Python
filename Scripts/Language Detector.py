from langdetect import detect

phase = "This is a test"

language = detect(phase)

print(language)

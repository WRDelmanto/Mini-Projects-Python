from langdetect import detect


def detectLanguage(text):
    # Detect the language
    language = detect(text)

    # Print the outcome
    print(language)


detectLanguage("This is a test")

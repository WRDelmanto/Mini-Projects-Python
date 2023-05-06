from captcha.image import ImageCaptcha


def generateImageCaptcha(captcha_text):
    # Set the path where the generated image will be saved
    path = "captcha.png"

    # Create an ImageCaptcha object with the specified width and height
    image = ImageCaptcha(width=280, height=90)

    # Write the captcha image to the specified path
    image.write(captcha_text, path)


generateImageCaptcha("ABC1234")

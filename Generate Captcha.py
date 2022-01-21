from captcha.image import ImageCaptcha

path = "captcha.png"
captcha_text = "ABC1234"

image = ImageCaptcha(width=280, height=90)

data = image.generate(captcha_text)

image.write(captcha_text, path)

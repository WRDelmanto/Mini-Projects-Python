from PIL import Image, ImageDraw, ImageFont


def textToHandWritten(text):
    # Define the image size and background color
    width = 1000
    height = 1000
    background_color = (255, 255, 255)  # White

    # Define the font and font size
    font = ImageFont.truetype("segoesc.ttf", size=12)

    # Create a new image with the specified size and background color
    blank_image = Image.new("RGB", (width, height), background_color)

    # Get a drawing context for the image
    draw = ImageDraw.Draw(blank_image)

    # Draw the text in a handwriting-like font
    draw.text((0, 0), text, fill=(0, 0, 0), font=font)

    # Determine the size of the text and center it in the image
    text_width, text_height = draw.textsize(text, font)

    # Crop the image
    left = 0
    top = 0
    right = text_width + 20
    bottom = text_height + 8
    cropped_image = blank_image.crop((left, top, right, bottom))

    # Save the image
    cropped_image.save("temp.png")


text = """
    This is a test
    This is a test 2
    This is a test 3
    """

textToHandWritten(text)

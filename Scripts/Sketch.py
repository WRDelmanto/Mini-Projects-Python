import cv2


def sketch(input_path, output_path):
    # Read the image from the input path.
    image = cv2.imread(input_path)

    # Convert the image to a grayscale image.
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the colors of the grayscale image.
    invert = cv2.bitwise_not(grey_image)

    # Apply Gaussian blur to the inverted image
    blur = cv2.GaussianBlur(invert, (21, 21), 0)

    # Invert the colors of the blurred image.
    invertedBlur = cv2.bitwise_not(blur)

    # Create a sketch by dividing the grayscale image by the inverted blurred image. and adjust the scale
    sketch = cv2.divide(grey_image, invertedBlur, scale=220.0)

    # Write the resulting sketch to the output path.
    cv2.imwrite(output_path, sketch)


sketch("temp.png", "temp2.png")

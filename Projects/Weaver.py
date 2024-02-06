import tkinter
from math import cos, radians, sin
import cv2
import numpy as np


def createTxtFile(output_path, lines, segments):
    # Create a list with information about the segments drawn
    archive = [f"Weaver finished({lines} lines)\n"]

    print(archive)

    # Loop through the segments list
    for i in range(1, len(segments)):
        # Append information to the archive list
        archive.append(f"{i}: {segments[(i - 1)]} -> {segments[i]}\n")

    # Construct the output text file path
    output_txt_path = output_path.rsplit(".", 1)[0] + ".txt"

    # Create a text file
    archive_txt = open(output_txt_path, "a+")

    # Write the archive information to it
    archive_txt.writelines(archive)
    archive_txt.close()


def beginWeaver(output_path, nail_quantity):
    # Min 2 nails
    if nail_quantity < 2:
        print("2 nails Min")
        return

    # Set up a window for displaying the output
    root = tkinter.Tk()
    root.withdraw()
    screensize = 800

    # Get the dimensions for the output image
    size = [int(screensize), int(screensize)]

    # Initialize line segments list
    segments = []

    # Count of lines drawn
    lines = 0

    # Calculate the center point of the output image
    center = [int(size[1] / 2), int(size[0] / 2)]

    # Calculate the angle between the center and each nail position
    angle = 360 / nail_quantity

    # Calculate the positions of all the nails on the board.
    nail_positions = []
    for i in range(0, nail_quantity):
        x = int(center[0] + ((center[0] - 1) * sin(-(radians(angle * i)))))
        y = int(center[1] + ((center[0] - 1) * cos(-(radians(angle * i)))))
        positions = [y, x]
        nail_positions.append(positions)

    # Initialize output image
    output_image = np.ones((size[0], size[1], 3), np.uint8) * 255

    # Create a canvas for drawing lines
    canvas = np.ones_like(output_image) * 255

    # Draw lines connecting all nails
    for i in range(nail_quantity):
        for j in range(i + 1, nail_quantity):
            line = [nail_positions[i], nail_positions[j]]
            segments.append(line)

            # Draw the line on the canvas
            cv2.line(
                canvas, (line[1][0], line[1][1]), (line[0]
                                                   [0], line[0][1]), (0, 0, 0), 1
            )

            # Increment lines count
            lines += 1

    # Resize the canvas for display
    output_image = cv2.resize(canvas, (size[1], size[0]))

    # Save the image to a file
    cv2.imwrite(output_path, canvas)

    # Display the output image
    cv2.imshow("output", output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Create the txt file
    createTxtFile(output_path, lines, segments)


# Example: for 2 points = line, for 3 points = triangle
beginWeaver("temp.jpg", 6)  # Change the number of nails as needed

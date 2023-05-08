import ctypes
import tkinter
from math import cos, radians, sin

import cv2


# This function calculates the distance between two points and counts the number of black pixels along that line.
def pixelsAnalysis(point_1, point_2, image):
    # Calculate the distance between the two points along the y and x axes
    y_distance = point_2[0] - point_1[0]
    x_distance = point_2[1] - point_1[1]

    # Determine the maximum distance to iterate over
    if y_distance > x_distance:
        step = abs(y_distance)
    else:
        step = abs(x_distance)

    # Count the number of black pixels along the line
    black_pixels = 0
    for pixel in range(1, step):
        # Calculate the coordinates of the current pixel along the line
        y_position = int(round(point_1[0] + (y_distance * (pixel / step))))
        x_position = int(round(point_1[1] + (x_distance * (pixel / step))))
        pixel_position = [x_position, y_position]

        # Get the color of the pixel
        y_color = image.item(pixel_position[0], pixel_position[1], 0)
        X_color = image.item(pixel_position[0], pixel_position[1], 1)
        z_color = image.item(pixel_position[0], pixel_position[1], 2)
        color = [y_color, X_color, z_color]

        # Check if it's black
        if color[0] == color[1] == color[2] == 0:
            black_pixels += 1

    # Return the number of black pixels and the two input points
    return [black_pixels, point_1, point_2]


# This function sets all pixel values to white RGB(255,255,255)
def cleanImage(cleaned):
    for y_axis in range(0, cleaned.shape[0]):
        for x_axis in range(0, cleaned.shape[1]):
            cleaned.itemset(y_axis, x_axis, 0, 255)
            cleaned.itemset(y_axis, x_axis, 1, 255)
            cleaned.itemset(y_axis, x_axis, 2, 255)


def createTxtFile(input_path, lines, segments):
    # Create a list with information about the segments drawn
    archive = [f"Weaver finished, ({lines} lines)\n"]

    # Loop through the segments list
    for i in range(1, len(segments)):
        # Append information to the archive list
        archive.append(f"{i}: {segments[(i - 1)]} -> {segments[i]}\n")

    # Close the OpenCV window
    cv2.destroyAllWindows()

    # Create a text file
    archive_txt = open(input_path.replace(
        "jpg", "txt").replace("png", "txt"), "a")

    # Write the archive information to it
    archive_txt.writelines(archive)
    archive_txt.close()


def beginWeaver(input_path, nail_quantity, max_lines):
    # Set up a window for displaying the output
    root = tkinter.Tk()
    root.withdraw()
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

    # Load the input image
    input_image = cv2.imread(input_path)

    # Create a copy of the input image
    output_image = cv2.imread(input_path)

    # Set all the input image pixels to white
    cleanImage(output_image)

    # Create a display image by concatenating the original and cleaned images side-by-side
    display = cv2.resize(
        output_image, ((output_image.shape[0] * 2), output_image.shape[1]))

    # Get the dimensions of the input image
    size = input_image.shape

    # Calculate the center point of the image
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

    # Set the starting point
    actual_point = nail_positions[0]

    # Initialize line segments list
    segments = [0]

    # Count of lines drawn
    lines = 0

    # Draw lines until all points are connected
    while True:
        # Find the next point to connect to
        bigger = [0, nail_positions[0], nail_positions[0]]

        for i in range(0, nail_quantity):
            point_analysis = nail_positions[i]
            a = pixelsAnalysis(actual_point, point_analysis, input_image)

            if a[0] > bigger[0]:
                bigger = [a[0], a[1], a[2]]

        # Connect the two points with a line
        actual_point = bigger[2]
        line = [bigger[1], bigger[2]]
        index = nail_positions.index(bigger[2])
        segments.append(index)

        # Draw the line on the original image
        cv2.line(
            input_image,
            (line[1][0], line[1][1]),
            (line[0][0], line[0][1]),
            (255, 255, 255),
            1,
        )

        # Draw the line on the output image
        cv2.line(
            output_image, (line[1][0], line[1][1]), (line[0]
                                                     [0], line[0][1]), (0, 0, 0), 1
        )

        # Resize the image
        display[0: display.shape[0], 0: int(
            display.shape[1] / 2)] = input_image
        display[
            0: display.shape[0], int(display.shape[1] / 2): display.shape[1]
        ] = output_image
        display_show = cv2.resize(
            display, (screensize[0] - 100, screensize[1] - 200))

        # Display the output image
        cv2.imshow("output", display_show)
        cv2.waitKey(10)

        # Increment the line counter
        lines += 1

        # Stop drawing if all points are connected or 1800 lines have been drawn
        if bigger[0] == 0 or lines == max_lines:
            break

    # Resize the output image
    output_image = cv2.resize(
        output_image, (input_image.shape[0], input_image.shape[1]))

    # Save the image to a file
    cv2.imwrite("output_" + input_path, output_image)

    # Display the output image
    cv2.imshow("output", output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Create the txt file
    createTxtFile(input_path, lines, segments)


# Recommended: nail_quantity = 360, max_lines = 1800
beginWeaver("temp3.jpg", 360, 1800)

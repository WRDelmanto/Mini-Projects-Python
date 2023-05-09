import time

import keyboard
import pyautogui
import win32api
import win32con


def clickEvent(x, y):
    # Set the cursor position to the given X and Y coordinates
    win32api.SetCursorPos((x, y))

    # Simulate pressing down the left mouse button
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

    # Wait for a short amount of time (Prevent hold event)
    time.sleep(0.01)

    # Simulate releasing the left mouse button
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def playAimBooster(stop_key, region, pixel_color_red, pixel_color_green, pixel_color_blue):
    # Print a start sentence
    print("Lets Play Aim Booster!")

    # Keep playing the game until the stop key is pressed
    while keyboard.is_pressed(stop_key) == False:
        # Take a screenshot of the specified region
        screenshot = pyautogui.screenshot(region=region)

        # Get the width and height of the screenshot
        width, height = screenshot.size

        # Loop through every 5 pixels in the screenshot
        for x in range(0, width, 5):
            for y in range(0, height, 5):

                # Get the RGB values of the pixel at (x, y)
                red, green, blue = screenshot.getpixel((x, y))

                # Checks if the pixel matches the specified color, click on it and print a message
                if red == pixel_color_red and green == pixel_color_green and blue == pixel_color_blue:
                    # Click on the pixel
                    clickEvent(x + region[0], y + region[1])

                    # Print when clicked
                    print("Clicked at ", x, ":", y)

                    # Exit the inner loop and continue with the outer loop
                    break


# http://www.aimbooster.com/
# Recomended: "Generate Screenshot.py" to help set the coordinates
playAimBooster("q", (660, 370, 600, 420), 255, 219, 195)

import keyboard
import pyautogui


def showPixelColor(stop_key):
    # Check if it should stop the program
    while keyboard.is_pressed(stop_key) == False:
        # Get the mouse pixel coordinates
        x, y = pyautogui.position()

        # Get the mouse pixel coordinates
        pixel_color = pyautogui.screenshot().getpixel((x, y))

        # Print the coordinates
        print("Color: ", pixel_color)


showPixelColor("q")

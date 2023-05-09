import keyboard
import pyautogui


def getPixelCoordinates(stop_key):
    # Check if it should stop the program
    while keyboard.is_pressed(stop_key) == False:
        # Get the mouse pixel coordinates
        x, y = pyautogui.position()

        # Print the coordinates
        print("X: ", x, ", Y: ", y)


getPixelCoordinates("q")

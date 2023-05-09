import keyboard
import pyautogui


def findStickman(stop_key, path, region, confidence):
    # Check if stop_key is not pressed
    while keyboard.is_pressed(stop_key) == False:
        # Locate the stickman on the screen
        location = pyautogui.locateOnScreen(
            path, region=region, confidence=confidence)

        # If stickman is found on the screen, print its location
        if location is not None:
            print("Found stickman at", location)
        else:
            print("Could not find stickman on screen")


# Recomended: "Generate Screenshot.py" to help set the coordinates
findStickman("q", "stickman.png", (0, 0, 1920, 1080), 0.8)

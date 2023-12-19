import keyboard
import time


def generateKeyboardEvent(key, stop_key, should_keep_looping):
    # Print a message to indicate that the function has started
    print("Begin Clicking...")

    # Loop until shouldKeepLooping is False
    while (should_keep_looping):
        # Press and release a keyboard key
        keyboard.press_and_release(key)

        # Wait for a short amount of time (Prevent hold event)
        time.sleep(0.01)

        # Check if a specific key is pressed to stop the loop
        if (keyboard.is_pressed(stop_key)):
            should_keep_looping = False

    # Print a message to indicate that the function has stopped
    print("Stopped")


generateKeyboardEvent("2", "1", True)

import keyboard
import mouse
import time


def generateMouseEvent(key, stop_key, should_keep_looping):
    # Print a message to indicate that the function has started
    print("Begin Clicking...")

    # Loop until shouldKeepLooping is False
    while (should_keep_looping):
        # Click action
        mouse.click(key)

        # Wait for a short amount of time (Prevent hold event)
        time.sleep(0.01)

        # Check if a specific key is pressed to stop the loop
        if (keyboard.is_pressed(stop_key)):
            should_keep_looping = False

    # Print a message to indicate that the function has stopped
    print("Stopped")


generateMouseEvent("left", "right", True)

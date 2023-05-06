import keyboard
import time


def generateKeyboardEvent(loopingKey, loopingStopKey, shouldKeepLooping):
    # Set a variable to store the duration of the sleeping time
    sleepingTime = 0.01

    # Print a message to indicate that the function has started
    print("Started")

    # Loop until shouldKeepLooping is False
    while (shouldKeepLooping):
        # Press and release a keyboard key
        keyboard.press_and_release(loopingKey)

        # Pause the execution for a specified amount of time to prevent bug
        time.sleep(sleepingTime)

        # Check if a specific key is pressed to stop the loop
        if (keyboard.is_pressed(loopingStopKey)):
            shouldKeepLooping = False

    # Print a message to indicate that the function has stopped
    print("Stopped")


generateKeyboardEvent("2", "1", True)

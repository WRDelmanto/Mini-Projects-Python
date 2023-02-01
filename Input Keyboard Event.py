import keyboard
import time

shouldKeepLooping = True
loopingKey = "2"
loopingStopKey = "1"
sleepingTime = 0.01

print("Begin")

while (shouldKeepLooping):
    keyboard.press_and_release(loopingKey)
    time.sleep(sleepingTime)

    if (keyboard.is_pressed(loopingStopKey)):
        shouldKeepLooping = False

print("Stop")

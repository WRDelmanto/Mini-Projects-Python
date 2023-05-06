import winsound


def makeBeepSound(frequency: int, duration: int, numberOfTimes: int):
    for beep in range(numberOfTimes):
        # Play the beep sound
        winsound.Beep(frequency, duration)


makeBeepSound(10000, 1000, 1)

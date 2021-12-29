import winsound

frequency = int(10000)  # Hertz
duration = int(2000)  # Milliseconds
numberOfTimes = int(2)

for i in range(0, numberOfTimes):
    winsound.Beep(frequency, duration)

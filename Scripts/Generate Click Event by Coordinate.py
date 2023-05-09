import time

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


# Recomended: "Get Pixel Coordinates.py" to help set the coordinates
clickEvent("100", "100")

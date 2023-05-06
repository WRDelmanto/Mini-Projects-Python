import pyautogui


def regionScreenshot(x1, x2, y1, y2):
    # Specify the path
    path = "temp.png"

    # take a screenshot
    screenshot = pyautogui.screenshot(region=(x1, y1, x2, y2))

    # Save the screenshot
    screenshot.save(path)


regionScreenshot(0, 100, 0, 100)

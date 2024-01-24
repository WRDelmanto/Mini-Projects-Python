import pyautogui


def generateScreenshot(path, region):
    # Take a screenshot of the specified region
    screenshot = pyautogui.screenshot(region=region)

    # Save the screenshot
    screenshot.save(path)


# Region = left, top, width and height
generateScreenshot("temp.png", (0, 0, 1920, 1080))

import pyautogui


def generateScreenshot(path, region):
    # Take a screenshot of the specified region
    screenshot = pyautogui.screenshot(region=region)

    # Save the screenshot
    screenshot.save(path)


generateScreenshot("temp.png", (660, 370, 600, 420))

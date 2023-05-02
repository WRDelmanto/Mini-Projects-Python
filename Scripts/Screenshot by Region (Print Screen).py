import pyautogui

# Specify the path
path = "temp.png"

# take a screenshot
screenshot = pyautogui.screenshot(region=(660, 350, 600, 400))

# Save the screenshot
screenshot.save(path)

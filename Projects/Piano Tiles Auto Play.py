import pyautogui
import time
import keyboard
import win32api
import win32con

# Tile 1 Position: X:  581 Y:  400 RGB: ( 77,  80, 115)
# Tile 2 Position: X:  682 Y:  400 RGB: (  0,   0,   0)
# Tile 3 Position: X:  770 Y:  400 RGB: ( 79,  82, 116)
# Tile 4 Position: X:  869 Y:  400 RGB: ( 80,  83, 116)


def showPixelCoordinates(stop_key):
    # Check if it should stop the program
    while keyboard.is_pressed(stop_key) == False:
        # Get the mouse pixel coordinates
        x, y = pyautogui.position()

        # Print the coordinates
        print("X: ", x, ", Y: ", y)


def showPixelColor(stop_key):
    # Check if it should stop the program
    while keyboard.is_pressed(stop_key) == False:
        # Get the mouse pixel coordinates
        x, y = pyautogui.position()

        # Get the mouse pixel coordinates
        pixel_color = pyautogui.screenshot().getpixel((x, y))

        # Print the coordinates
        print("Color: ", pixel_color)


def clickEvent(x, y):
    # Set the cursor position to the given X and Y coordinates
    win32api.SetCursorPos((x, y))

    # Simulate pressing down the left mouse button
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)

    # Wait for a short amount of time (Prevent hold event)
    time.sleep(0.01)

    # Simulate releasing the left mouse button
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def playPianoTiles(stop_key, tile_1_x, tile_2_x, tile_3_x, tile_4_x, tiles_y, tile_color_red, tile_color_green, tile_color_blue):
    # Print a start sentence
    print("Lets Play Piano Tiles!")

    # Check if it should stop the program
    while keyboard.is_pressed(stop_key) == False:
        # Get pixel color for tile 1
        tile_1_color_red, tile_1_color_green, tile_1_color_blue = pyautogui.pixel(
            tile_1_x, tiles_y)

        # Check if the pixel color is the same as the tiles color
        if tile_1_color_red == tile_color_red and tile_1_color_green == tile_color_green and tile_1_color_blue == tile_color_blue:
            # Call the clickEvent function
            clickEvent(tile_1_x, tiles_y)

            # Print when pressed
            print("Tile 1 pressed")

        # Get pixel color for tile 2
        tile_2_color_red, tile_2_color_green, tile_2_color_blue = pyautogui.pixel(
            tile_2_x, tiles_y)

        # Check if the pixel color is the same as the tiles color
        if tile_2_color_red == tile_color_red and tile_2_color_green == tile_color_green and tile_2_color_blue == tile_color_blue:
            # Call the clickEvent function
            clickEvent(tile_2_x, tiles_y)

            # Print when pressed
            print("Tile 2 pressed")

        # Get pixel color for tile 3
        tile_3_color_red, tile_3_color_green, tile_3_color_blue = pyautogui.pixel(
            tile_3_x, tiles_y)

        # Check if the pixel color is the same as the tiles color
        if tile_3_color_red == tile_color_red and tile_3_color_green == tile_color_green and tile_3_color_blue == tile_color_blue:
            # Call the clickEvent function
            clickEvent(tile_3_x, tiles_y)

            # Print when pressed
            print("Tile 3 pressed")

        # Get pixel color for tile 4
        tile_4_color_red, tile_4_color_green, tile_4_color_blue = pyautogui.pixel(
            tile_4_x, tiles_y)

        # Check if the pixel color is the same as the tiles color
        if tile_4_color_red == tile_color_red and tile_4_color_green == tile_color_green and tile_4_color_blue == tile_color_blue:
            # Call the clickEvent function
            clickEvent(tile_4_x, tiles_y)

            # Print when pressed
            print("Tile 4 pressed")


# showPixelCoordinates("q")
# showPixelColor("q")
playPianoTiles("q", -1101, -1012, -925, -840, 575, 0, 0, 0)

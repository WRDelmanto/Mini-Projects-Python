import time

import keyboard
import pyautogui
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


# Recomended: "Generate Screenshot.py" to help set the coordinates
# (x1, x2, x3, x4, y) (r,g,b)
playPianoTiles("q", 600, 690, 775, 850, 450, 0, 0, 0)

import board
import neopixel

NUMBER_OF_LEDS = 150
pixels = neopixel.NeoPixel(board.D18, NUMBER_OF_LEDS)

for pixel in pixels:
    pixel = (255, 255, 255)
    input("press enter to continue")
    pixel = (0, 0, 0)

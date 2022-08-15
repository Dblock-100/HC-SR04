import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


# Display Information
oled_reset = digitalio.DigitalInOut(board.D4)
WIDTH = 128
HEIGHT = 64 
BORDER = 5

i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

# Clear display.
oled.fill(0)
oled.show()

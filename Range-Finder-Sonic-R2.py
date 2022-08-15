import RPi.GPIO as GPIO
import time
import board
import adafruit_ssd1306
import digitalio
from PIL import Image, ImageDraw, ImageFont

GPIO.setmode(GPIO.BCM)

TRIG = 23

ECHO = 24

######Start OLED Information#####
#Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

#Size Specs
WIDTH = 128
HEIGHT = 64  
BORDER = 5

# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)
#######END OELD INFORMATION#######

######START TEXT TO DISPLAY ON OELD######
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Load default font.
font = ImageFont.truetype("DejaVuSans.ttf", 19)

print ("Distance Measurement In Progress")
s1="Sending Ping"
# Draw Some Text
text = str(s1)
(font_width, font_height) = font.getsize(text)
draw.text(
    (oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
    text,
    font=font,
    fill=255,
)

# Display image
oled.image(image)
oled.show()

time.sleep(1)
######END TEXT TO DEPLAY ON OELD######

GPIO.setup(TRIG,GPIO.OUT)

GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)

# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Load default font.
font = ImageFont.truetype("DejaVuSans.ttf", 20)

print ("Waiting For Sensor To Settle")
s2="Doing Math"
# Draw Some Text
text = str(s2)
(font_width, font_height) = font.getsize(text)
draw.text(
    (oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
    text,
    font=font,
    fill=255,
)

# Display image
oled.image(image)
oled.show()

time.sleep(1)

GPIO.output(TRIG, True)

time.sleep(0.00001)

GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
    pulse_start = time.time()
    
while GPIO.input(ECHO)==1:
    pulse_end = time.time()
    
pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance, 2)

print (distance,"cm")

#convert cm to feet
cm=distance
feet=0.0328*cm
feet2=(round(feet,2))
print(feet2,("feet"))
out=(feet2)
s = out
str(s)

#convert cm into inches
cm=distance
inches=0.394*cm
inches2=(round(inches,2))
print(inches2,("inches"))

# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Load default font.
font = ImageFont.truetype("DejaVuSans.ttf", 35)

# Draw Some Text
text = str(s)
(font_width, font_height) = font.getsize(text)
draw.text(
    (oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
    text,
    font=font,
    fill=255,
)

# Display image
oled.image(image)
oled.show()

time.sleep(2)
#####################NEW TEXT CODE#######

# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Load default font.
font = ImageFont.truetype("DejaVuSans.ttf", 45)
s3 = "Feet"
# Draw Some Text
text = str(s3)
(font_width, font_height) = font.getsize(text)
draw.text(
    (oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
    text,
    font=font,
    fill=255,
)

# Display image
oled.image(image)
oled.show()

#####END NEW TEXT CODE#####

#Clear OLED##
time.sleep(5)
oled.fill(0)
oled.show()


import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw

i2c = busio.I2C(board.SCL, board.SDA)

oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

oled.fill(0)
oled.show()

image = Image.new("1", (128, 64))
draw = ImageDraw.Draw(image)

draw.text((0, 0), "HELLO", fill=255)
draw.text((0, 20), "SSD1306", fill=255)
draw.text((0, 40), "WORK?", fill=255)

oled.image(image)
oled.show()

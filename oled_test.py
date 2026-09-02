from luma.core.interface.serial import i2c
from luma.oled.device import sh1107
from luma.core.render import canvas

serial = i2c(port=1, address=0x3C)

device = sh1107(serial)

with canvas(device) as draw:
    draw.text((0, 0), "HELLO", fill="white")
    draw.text((0, 16), "MAHJONG AI", fill="white")
    draw.text((0, 32), "CH1115 TEST", fill="white")
    draw.text((0, 48), "SUCCESS", fill="white")






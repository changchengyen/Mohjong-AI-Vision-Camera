from luma.core.interface.serial import i2c
from luma.oled.device import ch1115
from luma.core.render import canvas
import time

serial = i2c(port=1, address=0x3C)
device = ch1115(serial)

with canvas(device) as draw:
    draw.text((0, 0), "HELLO", fill="white")
    draw.text((0, 20), "MAHJONG AI", fill="white")

# 保持 60 秒不要結束
time.sleep(60)

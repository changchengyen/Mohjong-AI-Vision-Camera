from luma.core.interface.serial import i2c
from luma.oled.device import ch1115
from luma.core.render import canvas

serial = i2c(port=1, address=0x3C)
device = ch1115(serial)


def show(hand, tenpai, waits):

    line1 = "".join(hand[:8])
    line2 = "".join(hand[8:16])

    with canvas(device) as draw:

        draw.text((0, 0), "HAND", fill="white")

        draw.text((0, 12), line1, fill="white")

        draw.text((0, 24), line2, fill="white")

        draw.text(
            (0, 42),
            "TENPAI:" + ("YES" if tenpai else "NO"),
            fill="white"
        )

        draw.text(
            (0, 54),
            "WAIT:" + " ".join(waits),
            fill="white"
        )
def show_loading():

    with canvas(device) as draw:
        draw.text((15, 20), "MAHJONG AI", fill="white")
        draw.text((20, 40), "Loading...", fill="white")


def show_error(num):

    with canvas(device) as draw:
        draw.text((0, 0), "HAND ERROR", fill="white")
        draw.text((0, 20), "Detected", fill="white")
        draw.text((0, 36), f"{num}/16", fill="white")

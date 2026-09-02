import time
import cv2
import requests
import numpy as np

from detector import detect
from oled import show, show_loading, show_error
from tenpai import check

# ESP32-CAM 位址
CAM_URL = "http://172.20.10.6/capture"

show_loading()
time.sleep(1)

last_hand = None

while True:

    # ----------------------------
    # 抓 ESP32 最新照片
    # ----------------------------
    try:
        resp = requests.get(CAM_URL, timeout=3)

        img_array = np.frombuffer(resp.content, np.uint8)

        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        if img is None:
            print("Decode failed")
            time.sleep(0.5)
            continue

    except Exception as e:

        print("Camera Error:", e)

        time.sleep(1)

        continue

    # ----------------------------
    # YOLO
    # ----------------------------

    hand = detect(img)

    print("HAND:", hand)

    # ----------------------------
    # 牌數錯誤
    # ----------------------------

    if len(hand) != 16:

        show_error(len(hand))

        last_hand = None

        print(f"HAND ERROR ({len(hand)}/16)")

        time.sleep(0.5)

        continue

    # ----------------------------
    # 沒變就不更新 OLED
    # ----------------------------

    if hand != last_hand:

        tenpai, waits = check(hand)

        show(
            hand=hand,
            tenpai=tenpai,
            waits=waits if waits else ["--"]
        )

        print("=" * 40)
        print("HAND   :", "".join(hand))
        print("TENPAI :", "YES" if tenpai else "NO")
        print("WAIT   :", waits)
        print("=" * 40)

        last_hand = hand.copy()

    time.sleep(0.2)

from ai_edge_litert.interpreter import Interpreter
from PIL import Image
import numpy as np
import cv2

class_names = [
    "1","2","3","4","5",
    "6","7","8","9"
]

interpreter = Interpreter(model_path="best_int8.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def detect(img):

    # BGR -> RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # resize
    pil = Image.fromarray(img)
    pil = pil.resize((640, 640))

    x = np.array(pil, dtype=np.float32) / 255.0
    x = np.expand_dims(x, 0)

    interpreter.set_tensor(input_details[0]["index"], x)
    interpreter.invoke()

    output = interpreter.get_tensor(output_details[0]["index"])[0]

    boxes = output[:4]
    scores = output[4:]

    objs = []

    for i in range(output.shape[1]):

        cls = np.argmax(scores[:, i])
        conf = float(scores[cls, i])

        if conf < 0.50:
            continue

        cx = float(boxes[0, i])
        cy = float(boxes[1, i])
        w = float(boxes[2, i])
        h = float(boxes[3, i])

        x1 = (cx - w / 2) * 640

        objs.append({
            "x": x1,
            "conf": conf,
            "label": class_names[cls]
        })

    # 依 confidence 排序
    objs.sort(key=lambda o: o["conf"], reverse=True)

    filtered = []

    # 同一張牌(中心 x 很近)只保留最高 confidence
    for obj in objs:

        keep = True

        for f in filtered:

            if abs(obj["x"] - f["x"]) < 20:
                keep = False
                break

        if keep:
            filtered.append(obj)

    # 再依 x 排序
    filtered.sort(key=lambda o: o["x"])

    result = [o["label"] for o in filtered]

    # 最多只保留16張
    result = result[:16]

    print("Detect:", result)
    print("Count :", len(result))

    return result

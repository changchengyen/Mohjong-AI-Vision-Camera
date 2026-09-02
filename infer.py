from ai_edge_litert.interpreter import Interpreter
from PIL import Image
import numpy as np

# 類別名稱
class_names = [
    "1-dot","2-dot","3-dot","4-dot","5-dot",
    "6-dot","7-dot","8-dot","9-dot"
]

# 載入模型
interpreter = Interpreter(model_path="best_int8.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# 讀圖
img = Image.open("test0.jpg").convert("RGB")
img = img.resize((640,640))

img = np.array(img,dtype=np.float32)/255.0
img = np.expand_dims(img,0)

# 推論
interpreter.set_tensor(input_details[0]["index"],img)
interpreter.invoke()

output = interpreter.get_tensor(output_details[0]["index"])[0]

# output.shape = (13,8400)

boxes = output[:4]
scores = output[4:]

print("Detecting...\n")

count = 0

for i in range(output.shape[1]):

    cls = np.argmax(scores[:,i])
    conf = scores[cls,i]

    if conf > 0.85:

        x = boxes[0,i]
        y = boxes[1,i]
        w = boxes[2,i]
        h = boxes[3,i]

        print(
            f"{class_names[cls]}  "
            f"conf={conf:.3f}  "
            f"x={x:.3f} y={y:.3f} w={w:.3f} h={h:.3f}"
        )

        count += 1

print(f"\nTotal detections: {count}")

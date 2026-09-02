# Mohjong AI Vision Camera 麻將智能眼鏡雛形

基於 Raspberry Pi、Esp32 Camera 與 AI 視覺辨識的麻將影像分析專題。

(2026年大二下學期選修大三通訊系嵌入式系統之課堂專題)
此作品於2026/06/15測試成功，並於2026/06/17於課堂中進行最終報告
## Project Overview

This project uses a Raspberry Pi and an ESP32-CAM for image acquisition. TensorFlow Lite models are used for Mahjong tile recognition, and the results, including the unsorted hand, whether the hand is in tenpai, and the tiles needed to complete the hand, are displayed on an OLED.

## System Architecture

Camera → Wi-Fi Communication → Raspberry Pi → AI Image Detection → TensorFlow Lite → Result Processing → OLED Display

## Files

| File | Description |
|---|---|
| `main.py` | 主程式 |
| `detector.py` | 影像偵測 |
| `infer.py` | AI 模型推論 |
| `oled.py` | OLED 顯示控制 |
| `oled_fill.py` | OLED 測試／填充 |
| `oled_test.py` | OLED 測試 |
| `tenpai.py` | 麻將聽牌判定 |
| `test_model.py` | 模型測試 |
| `test_ssd.py` | SSD 測試 |
| `ch_test.py` | 測試 CH1115 OLED 是否能正常顯示 |
| `best_int8.tflite` | TensorFlow Lite AI 模型 |

## Hardware

- Raspberry Pi Zero 2 W
- Esp32 CAM
- Esp32-CAM-MB
- ov3660 camera
- [祥昌電子] 1.3吋 OLED 128x64 黑底藍字
- ADATA 64GB micro SD
## Environment

- (CODE)  Visual Studio Code
- (CODE)  Python 3.11.9
- (CAM) Arduino IDE 2.3.8
- (CAM) CameraWebServer
- (AI)  YOLO / Ultralytics
- (AI)  TensorFlow Lite
- (AI)  TensorFlow 2.19.0
- (AI)  roboflow
- (IMG) OpenCV (cv2)
- (RASPBERRY)  Raspberry Pi OS / Linux
- (RASPBERRY)  Python virtual environment (venv)
  
## model training methods

Take raw picture of objects:

For all classes of Mahjong dot tiles, images were collected under both single-tile and multi-tile arrangements. The dataset includes randomly distributed and unordered tiles, scattered tiles, upside-down tiles, and tiles captured from various viewing angles, such as top-down and side views. To improve dataset diversity, the lighting conditions and backgrounds were varied as much as possible.

Label the objects:

The collected images were subsequently uploaded to Roboflow for class definition and classification. After establishing the classes, the Mahjong tiles in each image were manually annotated with bounding boxes according to their corresponding classes.

Train the model:

The annotated dataset was exported from Roboflow in YOLO format and used to train the object detection model through the terminal. The YOLO model was trained to detect and classify Mahjong dot tiles based on their corresponding bounding boxes and classes.

The dataset structure is as follows:

```text
dataset/
├── train/
│   ├── images/
│   └── labels/
├── valid/
│   ├── images/
│   └── labels/
├── test/
│   ├── images/
│   └── labels/
└── data.yaml
```
The model was trained using the following command:

```
yolo detect train data=data.yaml model=yolo11n.pt epochs=100 imgsz=640
```





## Usage

Clone this repository:

```bash
git clone https://github.com/unknownhost/Mohjong-AI-Vision-Camera.git
cd Mohjong-AI-Vision-Camera

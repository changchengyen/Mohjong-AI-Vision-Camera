# Mohjong AI Vision Camera 麻將智能眼鏡雛形

基於 Raspberry Pi、Esp32 Camera 與 AI 視覺辨識的麻將影像分析專題。
(2026年大二下學期選修大三通訊系嵌入式系統之課堂專題)
## Project Overview

本專題使用 Raspberry Pi 搭配 Esp32 Camera 進行影像擷取，
並透過 TensorFlow Lite 模型進行麻將相關影像辨識，
最後將辨識結果顯示於 OLED。

## System Architecture

Camera
↓
Raspberry Pi
↓
AI Image Detection
↓
TensorFlow Lite
↓
Result Processing
↓
OLED Display

## Main Components

- Raspberry Pi
- Camera
- OLED Display
- TensorFlow Lite
- Python
- AI Image Detection

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
| `ch_test.py` | 中文相關測試 |
| `best_int8.tflite` | TensorFlow Lite AI 模型 |

## Hardware

- Raspberry Pi Zero 2 W
- Esp32 CAM
- Esp32-CAM-MB
- ov3660 camera
- [祥昌電子] 1.3吋 OLED 128x64 黑底藍字
- ADATA 64GB micro SD
## Environment

- Raspberry Pi OS
- Python 3.11.9
- (CAM) Arduino IDE 2.3.8
- (CAM) CameraWebServer
- (AI)  YOLO / Ultralytics
- (AI)  TensorFlow Lite
- (AI)  TensorFlow 2.19.0
- (IMG) OpenCV (cv2)
  

## Usage

Clone this repository:

```bash
git clone https://github.com/unknownhost/Mohjong-AI-Vision-Camera.git
cd Mohjong-AI-Vision-Camera

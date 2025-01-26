# YOLO Projects 1
* This repo has projects using YOLO

### Project 1: YOLOv5 Object Detection

#### Steps
* Clone the repo
```bash
git clone https://github.com/ultralytics/yolov5.git
```
* Install the requirements
```bash
cd .\yolov5\
pip install -r requirements.txt
```
* Download the weights and detect using webcam
```bash
# 0 for webcam
cd yolov5
python detect.py --weights yolov5s.pt --source 0 --device "cpu"
```
* Detect using an image
```bash
python detect.py --weights yolov5s.pt --img 640 --conf 0.25 --source data/images/zidane.jpg
```

# Facade Detection and Segmentation



## Workflow

![App Screenshot](https://github.com/Nanditharangu/Facade_Detection/blob/main/samples/IMG_9908.jpg?raw=true)


## Inference

### Environment setup

```bash
  virtualenv -p /usr/bin/python3 fac_det
  source fac_det/bin/activate
  pip install -r requirements.txt
```
### Download the model weights

[Yolo model](https://drive.google.com/file/d/1qHJ3BA8LrN5YYr-kBj8iJiu9JaGF4xyp/view?usp=sharing)

[SAM model](https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth)

Make sure the file strcture looks as below
```
├── Facade_Detection
│   ├── src
│   │   ├── models
│   │   |   ├── best.pt
│   │   |   └── sam_vit_b_01ec64.pth

```
### Run the app
```bash
uvicorn app:app --reload  
```
A http link will be displayed on the terminal. Open the link in a browser with /docs. (Example - http://127.0.0.1:8000/docs)

Upload an Image and click Execute
    
## Training YOLO 

Ultralytics YOLO model has been fine-tuned on [building-facade-segmentation-instance Computer Vision Project](https://universe.roboflow.com/building-facade/building-facade-segmentation-instance) dataset.

Training script [here](https://drive.google.com/file/d/1ic9YkDPTS5oWLhD-kW_DdXhjb4Gd4aLU/view?usp=sharing)
## Inference through Docker

### pull docker image

```bash
  docker pull rangunanditha/facade_detection
```
### run docker image

```bash
  docker run -p 8000:8000 rangunanditha/facade_detection
```
A http link will be displayed on the terminal. Open the link in a browser with /docs. (Example - http://0.0.0.0:8000/docs)

Upload an Image and click Execute


## Demo Video

https://github.com/user-attachments/assets/3f0e4a66-0b7e-4f5b-a309-8aceaaf5fa7f

## Sample results


![im1](https://github.com/Nanditharangu/Facade_Detection/blob/main/samples/2bdbce7e-7f70-4f6c-85a0-da592658cf06.jpg?raw=True)

![im2](https://github.com/Nanditharangu/Facade_Detection/blob/main/samples/2bf555eb-15d4-43c2-b9ae-7895f43d309a.jpg?raw=True)





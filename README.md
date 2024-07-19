
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

### Run the app
```bash
uvicorn app:app --reload  
```
A http link will be displayed on the terminal. Open the link in a browser with /docs. 

Upload an Image and click Execute
    
## Training YOLO model

Ultralytics YOLO model has been fine-tuned on [building-facade-segmentation-instance Computer Vision Project](https://universe.roboflow.com/building-facade/building-facade-segmentation-instance) dataset.

Training script [here](https://drive.google.com/file/d/1ic9YkDPTS5oWLhD-kW_DdXhjb4Gd4aLU/view?usp=sharing)
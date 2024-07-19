
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

[Yolo model](https://linktodocumentation)

[SAM model](https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth)

### Run the app
```bash
uvicorn app:app --reload  
```
A http link will be displayed on the terminal. Open the link in a browser with /docs. 

Upload an Image and click Execute
    
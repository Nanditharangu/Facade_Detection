import cv2
import numpy as np
import ultralytics
from ultralytics import YOLO
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor
import matplotlib.pyplot as plt
ultralytics.checks()

def show_box(box, ax):

    x0, y0 = box[0], box[1]
    w, h = box[2] - box[0], box[3] - box[1]
    ax.add_patch(plt.Rectangle((x0, y0), w, h, edgecolor='green', facecolor=(0,0,0,0), lw=2))

def E3_compliance(w2h, box):

    if 1/3 <= w2h <= 1/2:
        # print(f"Window is vertically rectangular with width-to-height ratio: {w2h:.2f}")
        pass
    else:
        # print(f"window does not meet the width-to-height ratio requirement: {w2h:.2f}")
        show_box(box, plt.gca())


def E2_compliance(facade_area, window_area, box):

    if facade_area > 0:
        ratio = (facade_area / (window_area + facade_area)) * 100
        if 40 <= ratio <= 60:
            # print(f"The facade area is within 40% to 60% of overall facade area: {ratio:.2f}%")
            pass
        else:
            # print(f"The facade area is not within the desired range: {ratio:.2f}%")
            show_box(box, plt.gca())
    else:
        print("No masks found for facade")

def main(file):

    # IMAGE_PATH = 'src/data/evaluation/543.jpeg'
    IMAGE_PATH = file
    YOLO_PATH = 'src/models/best.pt'
    SAM_PATH = "src/models/sam_vit_h_4b8939.pth"
    SAM_MODEL_TYPE = "vit_h"
    yolo_model = YOLO(YOLO_PATH)
    sam = sam_model_registry[SAM_MODEL_TYPE](checkpoint=SAM_PATH)
    sam_model = SamPredictor(sam)

    objects = yolo_model.predict(source = IMAGE_PATH, classes = [2, 9], conf = 0.4)
    image = cv2.cvtColor(cv2.imread(IMAGE_PATH), cv2.COLOR_BGR2RGB)
    sam_model.set_image(image)

    for result in objects:
        boxes = result.boxes.cpu().numpy()
        bbs = boxes.xyxy.tolist()
        class_list = boxes.cls.tolist()

    all_masks = []
    all_boxes = []
    for bbox in bbs:
        input_box = np.array(bbox)
        masks, _, _ = sam_model.predict(
            point_coords=None,
            point_labels=None,
            box=input_box[None, :],
            multimask_output=False,
        )
        all_masks.append(masks[0])
        all_boxes.append(input_box)

    plt.figure(figsize=(10, 10))
    plt.imshow(image)
    window_area = 0
    facade_area = 0

    for mask, detection_class, box in zip(all_masks, class_list, all_boxes):
        mask_uint8 = (mask * 255).astype(np.uint8)
        contours, _ = cv2.findContours(mask_uint8, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        mask_area = np.sum(mask)

        if detection_class == 2:
            color = 'red'
            facade_area += mask_area
            f_box = box
        elif detection_class == 9:
            color = 'blue'
            window_area += mask_area
        
        for contour in contours:
            plt.plot(contour[:, 0, 0], contour[:, 0, 1],color=color, linewidth=2)

            if detection_class == 9:
                x, y, w, h = cv2.boundingRect(contour)
                width_to_height_ratio = w / h
                E3_compliance(width_to_height_ratio, box)

    E2_compliance(facade_area, window_area, f_box)

    plt.axis('off')
    #plt.show()

    filename = file.split("/")[-1]
    plt.savefig(f'results/{filename}')


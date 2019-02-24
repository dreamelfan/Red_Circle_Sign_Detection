import numpy as np
import cv2
from matplotlib import pyplot as plt


# ============= augmentation helper functions ================
def visualize_image(img):
    """
        Show image using opencv
    """
    # Check if input is a image path
    if isinstance(img, str):
        img = cv2.imread(img)

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def format_bbox(bbox, bbox_format="pascal_voc"):
    """
        Helper function to convert bbox coordinates format
    """
    if bbox_format == "pascal_voc":
        return int(bbox['xmin']), int(bbox['ymin']), int(bbox['xmax']), int(bbox['ymax']) 


def visualize_bbox(img, bbox, class_id, class_idx_to_name, color=(255, 0, 0), thickness=2): 
    """
        Show bounding box in an image
    """ 
    # Check if input is a image path
    if isinstance(img, str):
        img = cv2.imread(img)

    # draw bounding box 
    x_min, y_min, x_max, y_max = format_bbox(bbox)
    cv2.rectangle(img, (x_min, y_min), (x_max, y_max), color=color, thickness=thickness)

    # add class info
    class_name = class_idx_to_name[class_id]
    ((text_width, text_height), _) = cv2.getTextSize(class_name, cv2.FONT_HERSHEY_SIMPLEX, 0.35, 1)    
    cv2.rectangle(img, (x_min, y_min - int(1.3 * text_height)), (x_min + text_width, y_min), BOX_COLOR, -1)

    text_color = (255, 255, 255)
    cv2.putText(img, class_name, (x_min, y_min - int(0.3 * text_height)), cv2.FONT_HERSHEY_SIMPLEX, 0.35,text_color, lineType=cv2.LINE_AA)
    return img


def visualize(annotations, category_id_to_name):
    """
        Show images with bounding boxes
    """
    img = annotations['image'].copy()
    for idx, bbox in enumerate(annotations['bboxes']):
        img = visualize_bbox(img, bbox, annotations['category_id'][idx], category_id_to_name)
    plt.figure(figsize=(12, 12))
    plt.imshow(img)


# ============ convert labels ==============
# in case YOLO is to be used
def convert_labels(img, bbox, return_string=False):
    """
        Converts (x1, y1, x2, y2) KITTI format to (x, y, width, height) normalized YOLO format.
    """
    # Check if input is a image path
    if isinstance(img, str):
        img = cv2.imread(img)

    img_size = img.shape
    x1, y1, x2, y2 = format_bbox(bbox)

    # find the center of bbox
    x = (x1 + x2) * 0.5 / img_size[1]
    y = (y1 + y2) * 0.5 / img_size[0]

    # width and hight of bbox
    w = abs(x1 - x2) / img_size[1]
    h = abs(y1 - y2) / img_size[0]

    # return YOLO label format
    if return_string:
        return "{} {} {} {}".format(x,y,w,h)
    else:
        return x, y, w, h


# ================ test for TT100K dataset ==================
if __name__ == "__main__":
    test_image_path = "/data/TT100K/other/58204.jpg"
    test_image = cv2.imread(test_image_path)
    visualize_image(test_image) 


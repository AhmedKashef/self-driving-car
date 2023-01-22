from utils import get_data

from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
import os
import sys
from math import sqrt


def viz(ground_truth, prediction):
    """
    create a grid visualization of images with color coded bboxes
    args:
    - ground_truth [list[dict]]: ground truth data
    """

    fig, ax = plt.subplots(int(sqrt(len(ground_truth)) + 1), int(sqrt(len(ground_truth)) + 1), figsize=(60, 60))

    rectangles = list()
    for i, element in enumerate(ground_truth):
        x = int(i / int(sqrt(len(ground_truth))))
        y = i % int(sqrt(len(ground_truth)))

        image_path = os.path.join(os.path.join(sys.path[0], "data/images"), element["filename"])
        img = Image.open(image_path)

        pred_element = [x for x in prediction if x["filename"] == element["filename"]]
        ax[x, y].imshow(img)

        for box in element["boxes"]:
            y1, x1, y2, x2 = box

            width = abs(x2 - x1)
            height = abs(y2 - y1)

            rect = Rectangle((x1, y1), width, height, linewidth=1, edgecolor='g', facecolor=None, fill=False, alpha=0.8)
            rect.set_label("Ground_Truth")
            rectangles.append(rect)
            ax[x, y].add_patch(rect)
        if any(pred_element):

            for box in pred_element[0]["boxes"]:
                y1, x1, y2, x2 = box

                width = abs(x2 - x1)
                height = abs(y2 - y1)

                rect = Rectangle((x1, y1), width, height, linewidth=1, edgecolor='r', facecolor=None, fill=False, alpha=0.8)
                ax[x, y].add_patch(rect)
                rect.set_label("Ground_Truth")
                rectangles.append(rect)
        ax[x, y].set_title(element["filename"])
        ax[x, y].legend(rectangles,[rect.get_label() for rect in rectangles])
        rectangles.clear()

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    ground_truth, prediction = get_data()
    viz(ground_truth, prediction)

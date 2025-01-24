import numpy as np
import matplotlib.pyplot as plt

def draw_rectangles_and_contour():

    rectangles = [
        [1, 1, 8, 6],
        [6, 2, 10, 8],
        [3, 1, 7, 5],
        [4, 11, 11, 14],
        [2, 6, 5, 12],
        [8, 7, 12, 12]
    ]

    width, height = 15, 15
    scale = 50


    img_rectangles = np.ones((height * scale, width * scale, 3), dtype=np.uint8) * 255
    img_contour = img_rectangles.copy()

    for (x1, y1, x2, y2) in rectangles:
        px1, py1 = x1 * scale, y1 * scale
        px2, py2 = x2 * scale, y2 * scale


        img_rectangles[py1, px1:px2] = [0, 0, 255]

        img_rectangles[py2 - 1, px1:px2] = [0, 0, 255]

        img_rectangles[py1:py2, px1] = [0, 0, 255]

        img_rectangles[py1:py2, px2 - 1] = [0, 0, 255]


    mask = np.zeros((height * scale, width * scale), dtype=np.uint8)
    for (x1, y1, x2, y2) in rectangles:
        px1, py1 = x1 * scale, y1 * scale
        px2, py2 = x2 * scale, y2 * scale
        mask[py1:py2, px1:px2] = 255


    boundary_mask = np.zeros_like(mask, dtype=np.uint8)
    h, w = mask.shape

    for y in range(1, h - 1):
        for x in range(1, w - 1):
            if mask[y, x] == 255:
                if (mask[y - 1, x] == 0 or
                    mask[y + 1, x] == 0 or
                    mask[y, x - 1] == 0 or
                    mask[y, x + 1] == 0):
                    boundary_mask[y, x] = 255


    boundary_pixels = np.argwhere(boundary_mask == 255)
    contour_points = [(x, y) for (y, x) in boundary_pixels]


    print("List of boundary points in (x=..., y=...) format:")
    for (x, y) in contour_points:
        print(f"(x={x}, y={y})")


    img_contour[boundary_mask == 255] = [255, 0, 0]  # BGR=(255,0,0)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.title("Input Rectangles")
    plt.imshow(img_rectangles)
    plt.xticks(np.arange(0, (width + 1) * scale, scale), np.arange(0, width + 1))
    plt.yticks(np.arange(0, (height + 1) * scale, scale), np.arange(0, height + 1))
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.gca().invert_yaxis()
    plt.axis('on')

    plt.subplot(1, 2, 2)
    plt.title("Computed Contour")
    plt.imshow(img_contour)
    plt.xticks(np.arange(0, (width + 1) * scale, scale), np.arange(0, width + 1))
    plt.yticks(np.arange(0, (height + 1) * scale, scale), np.arange(0, height + 1))
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.gca().invert_yaxis()
    plt.axis('on')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    draw_rectangles_and_contour()
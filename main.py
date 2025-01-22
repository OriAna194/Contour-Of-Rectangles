import numpy as np
import matplotlib.pyplot as plt

def draw_rectangles_and_contour_no_cv2():
    # Define input rectangles (coordinates: (x1, y1, x2, y2))
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

    # 1. Create a blank "canvas" for drawing rectangles (3-channel image, white background).
    img_rectangles = np.ones((height * scale, width * scale, 3), dtype=np.uint8) * 255
    # 2. Create another canvas for drawing the final contour in color.
    img_contour = img_rectangles.copy()

    # (A) Draw rectangle edges in red on img_rectangles
    for (x1, y1, x2, y2) in rectangles:
        px1, py1 = x1 * scale, y1 * scale
        px2, py2 = x2 * scale, y2 * scale

        # Top edge
        img_rectangles[py1, px1:px2] = [0, 0, 255]
        # Bottom edge
        img_rectangles[py2 - 1, px1:px2] = [0, 0, 255]
        # Left edge
        img_rectangles[py1:py2, px1] = [0, 0, 255]
        # Right edge
        img_rectangles[py1:py2, px2 - 1] = [0, 0, 255]

    # (B) Create a binary mask where rectangles fill with 255
    mask = np.zeros((height * scale, width * scale), dtype=np.uint8)
    for (x1, y1, x2, y2) in rectangles:
        px1, py1 = x1 * scale, y1 * scale
        px2, py2 = x2 * scale, y2 * scale
        mask[py1:py2, px1:px2] = 255

    # (C) Identify boundary pixels
    boundary_mask = np.zeros_like(mask, dtype=np.uint8)
    h, w = mask.shape

    for y in range(1, h - 1):
        for x in range(1, w - 1):
            if mask[y, x] == 255:
                # Mark as boundary if any of its 4 neighbors is 0
                if (mask[y - 1, x] == 0 or
                    mask[y + 1, x] == 0 or
                    mask[y, x - 1] == 0 or
                    mask[y, x + 1] == 0):
                    boundary_mask[y, x] = 255

    # (D) Extract the boundary pixels into a list of (x, y) coords
    # Note: np.argwhere gives (row, col) => (y, x).
    boundary_pixels = np.argwhere(boundary_mask == 255)
    # Convert to (x, y) tuples:
    contour_points = [(x, y) for (y, x) in boundary_pixels]

    # -- Here is the updated print block:
    print("List of boundary points in (x=..., y=...) format:")
    for (x, y) in contour_points:
        print(f"(x={x}, y={y})")

    # Color the boundary in blue on img_contour
    img_contour[boundary_mask == 255] = [255, 0, 0]  # BGR=(255,0,0)

    # (E) Plot the results
    plt.figure(figsize=(12, 6))

    # Left: The input rectangles with red edges
    plt.subplot(1, 2, 1)
    plt.title("Input Rectangles (with Grid)")
    plt.imshow(img_rectangles)
    plt.xticks(np.arange(0, (width + 1) * scale, scale), np.arange(0, width + 1))
    plt.yticks(np.arange(0, (height + 1) * scale, scale), np.arange(0, height + 1))
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.gca().invert_yaxis()
    plt.axis('on')

    # Right: The computed contour in blue
    plt.subplot(1, 2, 2)
    plt.title("Computed Contour (with Grid)")
    plt.imshow(img_contour)
    plt.xticks(np.arange(0, (width + 1) * scale, scale), np.arange(0, width + 1))
    plt.yticks(np.arange(0, (height + 1) * scale, scale), np.arange(0, height + 1))
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.gca().invert_yaxis()
    plt.axis('on')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    draw_rectangles_and_contour_no_cv2()
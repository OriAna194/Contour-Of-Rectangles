# 📐 Finding the Contour of a Set of Rectangles

⚠️ **Important Note**: While the implementation follows the resources provided by our teacher, the code is currently **not producing the expected results**. The uploaded image demonstrates the incorrect output generated so far. Any insights or fixes are welcome!

---

## 🚀 What This Code Does

Given a set of rectangles like this:

```
rectangles = [
    (1, 1, 4, 4),  # Rectangle 1: (x1, y1, x2, y2)
    (2, 3, 6, 5),  # Rectangle 2
    (5, 1, 7, 6),  # Rectangle 3
    (3, 2, 5, 3)   # Rectangle 4
]
```

The program does the following:

1. **Input**: Reads rectangles defined by their bottom-left and top-right coordinates.
2. **Sweep Line Algorithm**: Scans through the x-coordinates of the rectangles to find the active edges (using a segment tree to track overlaps).
3. **Contour Construction**: It should build a contour by:
   - Finding vertical edges
   - Adding horizontal edges to close the shape.
4. **Visualization**: Displays the rectangles and the resulting contour side by side.

---

## 🛠 How It Works

- **`SegmentTree` Class**:
   - Manages active y-intervals.
   - Supports insertions (when encountering a new rectangle) and deletions (when exiting a rectangle).

- **`compute_contour` Function**:
   - Implements the **sweep line algorithm**.
   - Uses the segment tree to find active vertical edges.

- **`construct_closed_contour` Function**:
   - Should close the contour by adding horizontal edges to the vertical ones.

- **`draw_input_and_contour` Function**:
   - Visualizes the input rectangles and the resulting contour side by side using **matplotlib**.

---

⚠️ **Current Issue**: Instead of the expected result, the output currently shows an incorrect contour. See the uploaded image for reference.





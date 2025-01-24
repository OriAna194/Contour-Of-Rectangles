# Rectangle Boundary Detection Using NumPy and Matplotlib

## Project Overview
This project demonstrates how to compute and visualize the boundaries of multiple rectangles on a grid using **NumPy** and **Matplotlib**. It was developed as part of the **Computational Geometry** course in university, showcasing fundamental techniques for geometric processing and visualization in Python.

### Features
- Draws multiple rectangles on a grid with marked boundaries.
- Computes the contours (boundary points) of overlapping or adjacent rectangles.
- Visualizes results in an easy-to-interpret format:
  - Input rectangles are displayed with red edges.
  - Computed boundaries are highlighted in blue.
- Outputs a list of boundary points for further analysis.

---

## Technologies Used
- **Python 3.8+**
- **NumPy:** Efficient matrix operations and array manipulation.
- **Matplotlib:** Visualization of grids, rectangles, and boundaries.

---

## How It Works
1. **Input Rectangles:** A predefined set of rectangles specified by their coordinates `(x1, y1, x2, y2)`.
2. **Binary Mask Creation:** A blank grid is created and filled where rectangles are present.
3. **Boundary Detection:** Each pixel in the grid is checked to determine if it lies on the boundary of a rectangle.
4. **Contour Extraction:** Boundary pixels are collected as `(x, y)` coordinates.
5. **Visualization:**
   - Red edges represent the input rectangles.
   - Blue lines highlight the computed boundaries.

---

## Running the Project
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/rectangle-boundary-detection.git

import matplotlib.pyplot as plt


class SegmentTree:

    def __init__(self, ymin, ymax):
        self.ymin = ymin
        self.ymax = ymax
        self.tree = {}
        self.intervals = []

    def _update(self, node, node_ymin, node_ymax, y1, y2, delta):
        if y2 <= node_ymin or y1 >= node_ymax:
            return
        if y1 <= node_ymin and y2 >= node_ymax:
            self.tree[node] = self.tree.get(node, 0) + delta
        else:
            mid = (node_ymin + node_ymax) // 2
            self._update(node * 2, node_ymin, mid, y1, y2, delta)
            self._update(node * 2 + 1, mid, node_ymax, y1, y2, delta)

        if self.tree.get(node, 0) > 0:
            self.intervals.append((node_ymin, node_ymax))

    def insert(self, y1, y2):
        self.intervals = []
        self._update(1, self.ymin, self.ymax, y1, y2, 1)
        return self._merge_intervals()

    def delete(self, y1, y2):
        self.intervals = []
        self._update(1, self.ymin, self.ymax, y1, y2, -1)
        return self._merge_intervals()

    def _merge_intervals(self):
        self.intervals.sort()
        merged = []
        for start, end in self.intervals:
            if not merged or merged[-1][1] < start:
                merged.append((start, end))
            else:
                merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        return merged


def compute_contour(rectangles):
    events = []
    ymin, ymax = float('inf'), float('-inf')


    for x1, y1, x2, y2 in rectangles:
        events.append((x1, 'start', y1, y2))
        events.append((x2, 'end', y1, y2))
        ymin = min(ymin, y1)
        ymax = max(ymax, y2)

    events.sort()


    segment_tree = SegmentTree(ymin, ymax)
    vertical_edges = []

    prev_x = None
    for x, event_type, y1, y2 in events:
        if prev_x is not None and x != prev_x:
            active_intervals = segment_tree.intervals
            for y1, y2 in active_intervals:
                vertical_edges.append(((prev_x, y1), (prev_x, y2)))
        if event_type == 'start':
            segment_tree.insert(y1, y2)
        elif event_type == 'end':
            segment_tree.delete(y1, y2)
        prev_x = x

    return vertical_edges


def construct_closed_contour(vertical_edges):
    vertices = []
    for (x, y1), (_, y2) in vertical_edges:
        vertices.append((x, y1))
        vertices.append((x, y2))

    vertices.sort(key=lambda v: (v[1], v[0]))

    horizontal_edges = []
    for i in range(0, len(vertices), 2):
        x1, y = vertices[i]
        x2, _ = vertices[i + 1]
        horizontal_edges.append(((x1, y), (x2, y)))

    return vertical_edges + horizontal_edges


def draw_input_and_contour(rectangles):
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))


    ax1 = axes[0]
    for x1, y1, x2, y2 in rectangles:
        ax1.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], 'k-')
    ax1.set_title("a) Input Rectangles")
    ax1.set_aspect('equal', adjustable='datalim')
    ax1.grid(color='gray', linestyle='--', linewidth=0.5)


    ax2 = axes[1]
    vertical_edges = compute_contour(rectangles)
    contour_edges = construct_closed_contour(vertical_edges)
    for (x1, y1), (x2, y2) in contour_edges:
        ax2.plot([x1, x2], [y1, y2], 'r-', linewidth=1.5)
    ax2.set_title("b) Contour of the Union")
    ax2.set_aspect('equal', adjustable='datalim')
    ax2.grid(color='gray', linestyle='--', linewidth=0.5)

    plt.show()



rectangles = [
    (1, 1, 4, 4),
    (2, 3, 6, 5),
    (5, 1, 7, 6),
    (3, 2, 5, 3)
]
draw_input_and_contour(rectangles)

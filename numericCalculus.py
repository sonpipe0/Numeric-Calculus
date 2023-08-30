from typing import List, Tuple


class Interpolation:
    def __init__(self):
        self.points: List[Tuple[int, int]] = []

    def add_point(self, x: int, y: int) -> None:
        point: Tuple[int, int] = (x, y)
        self.points.append(point)
        return

    def remove_point(self, x: int) -> None:
        for i in range(len(self.points)):
            if x == self.points[i]:
                self.points.remove(self.points[i])
        raise ValueError("Not Found")

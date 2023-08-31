from typing import List, Tuple, Callable
import matplotlib.pyplot as plt
import numpy as np


class Interpolation:
    def __init__(self):
        self.points: List[Tuple[int, int]] = []
        self.minX: int = 0
        self.maxX: int = 0

    def add_point(self, x: int, y: int) -> None:
        point: Tuple[int, int] = (x, y)
        # ensure that x0 <= x1
        index: int = 0
        for j in self.points:
            if x > j[0]:
                index += 1
            elif x == j[0]:
                raise ValueError("Already in List")
            else:
                break
        self.points.insert(index, point)
        self.minX = self.points[0][0]
        self.maxX = self.points[len(self.points) - 1][0]
        return

    def remove_point(self, x: int) -> None:
        for i in range(len(self.points)):
            if x == self.points[i][0]:
                self.points.remove(self.points[i])
        raise ValueError("Not Found")


class Lagrange(Interpolation):
    def __init__(self):
        super().__init__()
        return

    def interpolate(self) -> Callable[[int], int]:
        def function(x: int) -> int:
            interpolation_sum: int = 0
            for i in range(len(self.points)):
                term: int = 1
                for j in range(len(self.points)):
                    if i != j:
                        term *= (x - self.points[j][0]) / (self.points[i][0] - self.points[j][0])
                interpolation_sum += term * self.points[i][1]
            return interpolation_sum

        return function

    def show(self) -> None:
        x_values = np.linspace(self.minX, self.maxX, int(self.maxX - self.minX) * 100)
        y_values = [self.interpolate()(x) for x in x_values]

        plt.plot(x_values, y_values)
        plt.scatter([point[0] for point in self.points], [point[1] for point in self.points], color='red', marker='o')
        plt.xlabel('x')
        plt.ylabel('Interpolated Value')
        plt.title("LAGRANGE INTERPOLATION")
        plt.grid(True)
        plt.show()


if __name__ == '__main__':
    '''interpolator = Lagrange()
    while True:
        var0 = int(input("write x: "))
        var1 = int(input("write y: "))
        interpolator.add_point(var0, var1)
        end = input("do you want to end \n [Y]     [N]: ")
        if end == 'Y':
            break

    interpolator.show()'''
    interpolator = Lagrange()

    test_points = [(-2, 14), (-1, 6), (0, 3), (1, 2), (2, 15)]

    for point in test_points:
        interpolator.add_point(point[0], point[1])

    interpolator.show()

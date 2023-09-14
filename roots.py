from typing import Optional, Union


class Roots:
    def __init__(self, multiplicity: int, n: int, x0: Union[int, float], e: float) -> None:
        self.multiplicity = multiplicity
        self.n = n
        self.x0 = x0
        self.e = e

    def function(self, x):
        return x ** self.multiplicity - self.n

    def solve(self) -> Optional[float]:
        while abs(self.function(self.x0)) >= self.e:
            derivative = self.multiplicity * self.x0 ** (self.multiplicity - 1)
            if derivative == 0:
                return None
            self.x0 = self.x0 - self.function(self.x0) / derivative
        return self.x0


if __name__ == '__main__':
    twoAtThePowerOfAThird = Roots(3, 2, 3, 0.0000000000001)
    root = twoAtThePowerOfAThird.solve()
    if root is not None:
        print("Root:", root)
    else:
        print("Cannot find root (division by zero encountered).")
from typing import Union, List
from math import sqrt


class Scalar:
    pass


class Vector:
    pass


class Scalar:
    def __init__(self: Scalar, val: float):
        self.val = float(val)

    def __mul__(self: Scalar, other: Union[Scalar, Vector]) -> Union[Scalar, Vector]:
        if isinstance(other, Scalar):
            return Scalar(self.val * other.val)
        if isinstance(other, Vector):
            _entries = [self.val * x for x in other.entries]
            return Vector(*_entries)
        else:
            raise TypeError(f"Second value should be Scalar or Value, found {type(other)}")

    def __add__(self: Scalar, other: Scalar) -> Scalar:
        if isinstance(other, Scalar):
            return Scalar(self.val + other.val)
        else:
            raise TypeError(f"Second value should be Scalar, found {type(other)}")

    def __sub__(self: Scalar, other: Scalar) -> Scalar:
        if isinstance(other, Scalar):
            return Scalar(self.val - other.val)
        else:
            raise TypeError(f"Second value should be Scalar, found {type(other)}")

    def __truediv__(self: Scalar, other: Scalar) -> Scalar:
        if isinstance(other, Scalar):
            return Scalar(self.val / other.val)
        else:
            raise TypeError(f"Second value should be Scalar, found {type(other)}")

    def __rtruediv__(self: Scalar, other: Vector) -> Vector:
        if isinstance(other, Scalar):
            _entries = list(map(lambda x: x.val / self.val, other))
            return Vector(*_entries)
        else:
            raise TypeError(f"Second value should be Vector, found {type(other)}")

    def __repr__(self: Scalar) -> str:
        return "Scalar(%r)" % self.val

    def sign(self: Scalar) -> int:
        if self.val == 0:
            return 0
        elif self.val > 0:
            return 1
        else:
            return -1

    def __float__(self: Scalar) -> float:
        return self.val


class Vector:
    def __init__(self: Vector, *entries: List[float]):
        self.entries = entries

    def zero(size: int) -> Vector:
        return Vector(*[0 for i in range(size)])

    def __add__(self: Vector, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError(f"Second value should be Vector, found {type(other)}")
        if len(self.entries) != len(other.entries):
            raise Exception(f"The lengths of items do not match: {len(self.enties)} and {len(other.entries)}")
        _entries = [x + y for x, y in zip(self.entries, other.entries)]
        return Vector(*_entries)

    def __sub__(self: Vector, other: Vector) -> Vector:
        return self + (-1) * other

    def __mul__(self: Vector, other: Vector) -> Scalar:
        if not isinstance(other, Vector):
            raise TypeError(f"Second value should be Vector, found {type(other)}")
        if len(self.entries) != len(other.entries):
            raise Exception(f"The lengths of items do not match: {len(self.enties)} and {len(other.entries)}")
        dot = 0
        for i in range(len(self.entries)):
            dot += (self.entries[i] * other.entries[i])
        return Scalar(dot)

    def magnitude(self: Vector) -> Scalar:
        _sum = 0
        for x in self.entries:
            _sum += x * x
        return Scalar(sqrt(_sum))

    def unit(self: Vector) -> Vector:
        return self / self.magnitude()

    def __len__(self: Vector) -> int:
        return len(self.entries)

    def __repr__(self: Vector) -> str:
        return "Vector%s" % repr(self.entries)

    def __iter__(self: Vector):
        return iter(self.entries)

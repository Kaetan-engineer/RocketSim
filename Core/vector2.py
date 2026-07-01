from __future__ import annotations
from dataclasses import dataclass
import math
from typing import Any

@dataclass
class Vector2():
    x: float
    y: float

    def __repr__(self) -> str:
        return f"Vector2(x={self.x}, y={self.y})"
    
    def __str__(self) -> str:
        return f"{self.x}, {self.y}"

    def __add__(self, other: "Vector2") -> "Vector2":
        return Vector2(
            self.x + other.x,
            self.y + other.y
        )
    
    def __iadd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other: "Vector2") -> "Vector2":
        return Vector2(
            self.x - other.x,
            self.y - other.y
        )
    
    def __mul__(self, other: float) -> "Vector2":
        if isinstance(other, Vector2):
            return NotImplemented
        
        return Vector2(
            self.x * other,
            self.y * other
        )
    
    def __rmul__(self, other: float) -> "Vector2":
        return self * other
    
    def __truediv__(self, other: float) -> "Vector2":
        if other == 0:
            raise ZeroDivisionError("Cannot divide a number by zero")
        return Vector2(
            self.x / other,
            self.y / other
        )
    
    def __abs__(self):
        if self.x < 0 and self.y < 0:
            return self * -1
        elif self.x < 0:
            return Vector2(
                self.x * -1,
                self.y * 1
            )
        else:
            return Vector2(
                self.x * 1,
                self.y * -1
            )
        
    def __pow__(self, other):
        return Vector2(
            self.x ** other,
            self.y ** other
        )
    
    def __neg__(self):
        return Vector2(-self.x, -self.y)
    
    def __eq__(self, value) -> bool:
        if isinstance(value, Vector2):
            return self.x == value.x and self.y == value.y
        return False
    
    def __lt__(self, other) -> bool:
        if isinstance(other, Vector2):
            return self.x < other.x and self.y < other.y
        return False

    def __gt__(self, other) -> bool:
        if isinstance(other, Vector2):
            return self.x > other.x and self.y > other.y
        return False

    def __bool__(self) -> bool:
        return self.x != 0 and self.y != 0
    
    def __len__(self) -> int:
        return 2

    @property
    def magnitude(self) -> float:
        return math.hypot(self.x**2, self.y**2)

    def normalized(self) -> Vector2:
        if self.magnitude < 1e-9:
            raise ValueError("Cannot normalize a zero-length vector")
        return self / self.magnitude
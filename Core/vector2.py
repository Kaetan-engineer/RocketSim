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

    def __add__(self, other: "Vector2") -> "Vector2":
        return Vector2(
            self.x + other.x,
            self.y + other.y
        )
    
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
    
    def __rmul__(self, other: float):
        return self * other
    
    def __truediv__(self, other: float) -> "Vector2":
        if other == 0:
            raise ZeroDivisionError("Cannot divide a number by zero")
        return Vector2(
            self.x / other,
            self.y / other
        )
    
    @property
    def magnitude(self) -> float:
        return math.sqrt((self.x**2) + (self.y**2))
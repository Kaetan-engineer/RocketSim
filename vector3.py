from dataclasses import dataclass
from math import sqrt

@dataclass
class Vector3:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    @property
    def magnitude(self) -> float:
        return sqrt(
            self.x**2 +
            self.y**2 +
            self.z**2
        )
    
    def __add__(self, other):
        return Vector3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )
    
    def __sub__(self, other):
        return Vector3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )
    
    def __mul__(self, scalar):
        return Vector3(
            self.x * scalar,
            self.y * scalar,
            self.z * scalar
        )
    
    def __truediv__(self, scalar):
        return Vector3(
            self.x / scalar,
            self.y / scalar,
            self.z / scalar
        )
    
    def __repr__(self) -> str:
        return (
            f"Vector3("
            f"x={self.x:.2f}, "
            f"x={self.y:.2f}, "
            f"x={self.z:.2f})"
        )
    
    def normalize(self):
        mag = self.magnitude

        if mag == 0:
            return Vector3()
        
        return self * (1 / mag)
    
    def dot(self, other):
        return (
            self.x * other.x,
            self.y * other.y,
            self.z * other.z
        )
    
    def cross(self, other):
        return Vector3(
            self.y * other.z / self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> "Distance" :
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            return NotImplemented

    def __iadd__(self, other: object) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, other: object) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            return NotImplemented

    def __truediv__(self, other: object) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        else:
            return NotImplemented

    def __lt__(self, other: object) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return NotImplemented

    def __gt__(self, other: object) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return NotImplemented

    def __eq__(self, other: object) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return NotImplemented

    def __le__(self, other: object) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return NotImplemented

    def __ge__(self, other: object) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return NotImplemented

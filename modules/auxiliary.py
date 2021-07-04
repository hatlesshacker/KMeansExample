""" File for storing helper Classes and Functions"""

import random
from typing import Union


# Class to initialize Cluster
class Cluster:
    def __init__(self, title: Union[str, int]) -> None:
        self.epi_x: float = random.randint(1, 10)
        self.epi_y: float = random.randint(1, 10)
        self.points: list[Point] = []
        self.title = title


# Class to initialize Point
class Point:
    def __init__(self, x: int, y: int, cl: Union[str, int] = 'u'):
        self.x = x
        self.y = y
        self.cl = cl


# Class for Global Boolean Vars
class BooleanVar:
    def __init__(self, value: bool = False) -> None:
        """Initializing a Boolean Variable"""
        self.value = value

    def set(self, value: bool) -> None:
        """Set the variable to VALUE"""
        self.value = value

    def get(self) -> bool:
        """Retrieve VALUE from the variable"""
        return self.value


def s_down(x: float):
    return int(x * 100) / 100

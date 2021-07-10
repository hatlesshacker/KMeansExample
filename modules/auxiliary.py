""" File for storing helper Classes and Functions"""

from random import randint
from typing import Union


# Class to initialize Cluster
class Cluster:
    def __init__(self, n: int) -> None:
        self.title: str = f"Cluster {n}"
        self.points: tuple = ()
        self.epi_x: Union[int, float] = randint(1, 10)
        self.epi_y: Union[int, float] = randint(1, 10)

    def __repr__(self):
        return f'({self.epi_x:.2f}, {self.epi_y:.2f})'


# Class to initialize Point
class Point:
    def __init__(self, x: int, y: int, cluster: Union[str, Cluster] = 'u'):
        self.x = x
        self.y = y
        self.cluster = cluster

    def __repr__(self):
        return f'({self.x:.2f}, {self.y:.2f})'


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

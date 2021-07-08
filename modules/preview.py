""" File for performing plotting operations in matplotlib"""
import csv
import itertools

import matplotlib.pyplot as plt  # type: ignore

from auxiliary import Cluster


# For Basic Preview
def preview(records_file: str) -> None:
    print("Previewing the records: ")
    x_val, y_val = [], []
    with open(records_file, newline="") as File:
        for x, y in csv.reader(File):
            if not (x == '' or y == ''):
                x_val.append(int(x))
                y_val.append(int(y))
    plt.scatter(x_val, y_val)
    plt.show()


# To preview with colors and legend
def rich_preview(clusters: list[Cluster]) -> None:
    colour = itertools.cycle(("red", "blue", "green", "black", "pink", "magenta", "yellow", "cyan", "darkgreen"))
    for cluster in clusters:
        points = cluster.points
        plt.scatter([point.x for point in points], [point.y for point in points],
                    color=next(colour), label=cluster.title)
    plt.legend(loc="upper left")
    plt.show()

""" File for performing plotting operations in matplotlib"""
import csv

import matplotlib.pyplot as plt  # type: ignore

from auxiliary import Cluster


# For Basic Preview
def preview(records_file: str) -> None:
    print("Previewing the records: ")
    x_val, y_val = [], []
    with open(records_file, newline="") as File:
        for row in csv.reader(File):
            x1, y1 = row[0], row[1]
            if not (x1 == "" or y1 == ""):
                x_val.append(x1)
                y_val.append(y1)
    plt.scatter(x_val, y_val)
    plt.show()


# Get tuple of colours
def get_colors() -> tuple[str, ...]:
    return "red", "blue", "green", "black"


# To preview with colors and legend
def rich_preview(clusters: list[Cluster]) -> None:
    for color, cluster in zip(get_colors(), clusters):
        points = cluster.points
        plt.scatter([point.x for point in points], [point.y for point in points], color=color, label=cluster.title)
    plt.legend(loc="upper left")
    plt.show()

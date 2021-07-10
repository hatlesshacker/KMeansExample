""" File for Point related functions"""

import csv
import random

from auxiliary import Cluster, Point


# Returns distance between cluster and point
def distance(cluster: Cluster, point: Point) -> float:
    epi_x, epi_y = cluster.epi_x, cluster.epi_y
    pt_x, pt_y = point.x, point.y
    return ((epi_x - pt_x) ** 2 + (epi_y - pt_y) ** 2) ** 0.5


# Retrieves all points from csv file and returns the raw point list
def get_points(filename: str) -> tuple[list[int], list[int]]:
    x_val, y_val = [], []
    with open(filename, newline="") as File:
        for x, y in csv.reader(File):
            if not (x == "" or y == ""):
                x_val.append(int(x))
                y_val.append(int(y))

    return x_val, y_val


# Takes raw points and returns properly set point list
def setup(raw: tuple[list[int], list[int]]) -> tuple[Point, ...]:
    return *(Point(x, y) for x, y in zip(raw[0], raw[1])),


# Takes point list and returns next point to be worked on
def get_next(points: tuple[Point, ...]) -> Point:
    # Points that have not been assigned to any cluster
    for point in points:
        if point.cluster == 'u':
            return point
    return random.choice(points)  # All points have been assigned clusters


# Assigns the next point to nearest cluster
def assign_next(clusters: list[Cluster], points: tuple[Point, ...]) -> None:
    point: Point = get_next(points)
    # DISTANCES BETWEEN THE POINT AND CLUSTERS
    distances: dict[float, Cluster] = {distance(cluster, point): cluster for cluster in clusters}
    point.cluster = distances[min(distances)]  # Assigning to nearest cluster


# Previews Coordinates of epicenter and point in a cluster
def view(clusters: list[Cluster]) -> None:
    for cluster in clusters:
        print(f" - Cluster {cluster.title}: {cluster} has {len(cluster.points)} points.")
    print()
    cl: Cluster = clusters[int(input("Enter cluster no.: ")) - 1]
    print(*cl.points, sep=', ')

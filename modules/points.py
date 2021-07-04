""" File for Point related functions"""

import csv
import math
import random

from auxiliary import Cluster, Point


# Returns distance between epicenter and point
def distance(epi_x: float, epi_y: float, pt_x: int, pt_y: int) -> float:
    return math.sqrt(math.pow(epi_x - pt_x, 2.0) + math.pow(epi_y - pt_y, 2.0))


# Returns list of points in cluster
def get_points_cl(points: list[Point], cluster_no: int) -> list[Point]:
    return [point for point in points if point.cl == cluster_no]


# Retrieves all points from csv file
# Returns the raw point list
def get_points(filename: str) -> list[list[int]]:
    x_val, y_val = [], []
    with open(filename, newline="") as File:
        for x, y in csv.reader(File):
            if not (x == "" or x == ""):
                x_val.append(int(x))
                y_val.append(int(y))

    return [x_val, y_val]


# Takes raw points
# Returns properly set point list
def setup(raw: list) -> list[Point]:
    return [Point(raw[0][i], raw[1][i]) for i in range(len(raw[0]))]


# Takes point list
# Returns next point to be worked on
def get_next(points: list[Point]) -> int:
    # Points that have not been assigned to any cluster
    for point in points:
        if point.cl == 'u':
            return points.index(point)

    # All points have been assigned clusters
    return random.randint(0, len(points) - 1)


# Assigns the next point to nearest cluster
def assign_next(clusters: list[Cluster], points: list[Point]) -> None:
    point: Point = points[get_next(points)]

    # DISTANCES BETWEEN POINT AND CLUSTERS
    distances = [distance(cluster.epi_x, cluster.epi_y, point.x, point.y) for cluster in clusters]
    point.cl = distances.index(min(distances))  # Assigning to nearest cluster


# Previews Coordinates of epicenter and point in a cluster
def view(clusters: list[Cluster]) -> None:
    cluster: Cluster = clusters[int(input("Enter cluster no.: ")) - 1]
    points: list[Point] = cluster.points
    print(f"{cluster.title} has {len(points)} elements.")
    print(f"({cluster.epi_x, cluster.epi_y})")
    for point in points:
        print(f"<{point.x, point.y}>", end=" ")

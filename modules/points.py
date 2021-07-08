""" File for Point related functions"""

import csv
import math
import random

from auxiliary import Cluster, Point


# Returns distance between cluster and point
def distance(cluster: Cluster, point: Point) -> float:
    epi_x, epi_y = cluster.epi_x, cluster.epi_y
    pt_x, pt_y = point.x, point.y
    return math.sqrt(math.pow(epi_x - pt_x, 2) + math.pow(epi_y - pt_y, 2))


# Returns list of points in cluster
def get_points_cl(points: list[Point], cluster: Cluster) -> list[Point]:
    return [point for point in points if point.cluster == cluster]


# Retrieves all points from csv file and returns the raw point list
def get_points(filename: str) -> list[list[int]]:
    x_val, y_val = [], []
    with open(filename, newline="") as File:
        for x, y in csv.reader(File):
            if not (x == "" or y == ""):
                x_val.append(int(x))
                y_val.append(int(y))

    return [x_val, y_val]


# Takes raw points and returns properly set point list
def setup(raw: list) -> list[Point]:
    return [Point(x, y) for x, y in zip(raw[0], raw[1])]


# Takes point list and returns next point to be worked on
def get_next(points: list[Point]) -> Point:
    # Points that have not been assigned to any cluster
    for point in points:
        if point.cluster == 'u':
            return point
    return random.choice(points)  # All points have been assigned clusters


# Assigns the next point to nearest cluster
def assign_next(clusters: list[Cluster], points: list[Point]) -> None:
    point: Point = get_next(points)
    # DISTANCES BETWEEN THE POINT AND CLUSTERS
    distances = {distance(cluster, point): cluster for cluster in clusters}
    point.cluster = distances[min(distances)]  # Assigning to nearest cluster


# Previews Coordinates of epicenter and point in a cluster
def view(clusters: list[Cluster]) -> None:
    for cluster in clusters:
        print(f" - Cluster {cluster.title}: {cluster} has {len(cluster.points)} points.")
    print()

    cluster: Cluster = clusters[int(input("Enter cluster no.: ")) - 1]
    print(*cluster.points, sep=', ')

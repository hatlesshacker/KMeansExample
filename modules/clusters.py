""" File for Cluster related functions"""

import points as pt
from auxiliary import Point, Cluster


def s_down(x: int) -> float:
    return int(x * 10000) / 10000


# To finalize points in clusters
def finalize(clusters: list[Cluster], points: list[Point]) -> None:
    for n, cluster in enumerate(clusters):
        cluster.points.extend(pt.get_points_cl(points, n))


# To set new epicenter
def update_epicenter(clusters: list[Cluster], points: list[Point]) -> None:
    for n, cluster in enumerate(clusters):
        points = pt.get_points_cl(points, n)
        if len(points):  # Only for clusters with points
            cluster.epi_x = sum([point.x for point in points]) / len(points)
            cluster.epi_y = sum([point.y for point in points]) / len(points)

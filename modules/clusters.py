""" File for Cluster related functions"""

from statistics import mean

import points as pt
from auxiliary import Point, Cluster


# To finalize points in clusters
def finalize(clusters: list[Cluster], points: list[Point]) -> None:
    for cluster in clusters:
        cluster.points = pt.get_points_cl(points, cluster)


# To set new epicenter
def update_epicenter(clusters: list[Cluster], points: list[Point]) -> None:
    for cluster in clusters:
        pts = pt.get_points_cl(points, cluster)
        if len(pts):  # Only for clusters with points
            cluster.epi_x = mean([point.x for point in pts])
            cluster.epi_y = mean([point.y for point in pts])

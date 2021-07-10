""" File for Cluster related functions"""

from statistics import mean

from auxiliary import Point, Cluster


# To finalize points in clusters
def finalize(clusters: list[Cluster], points: tuple[Point, ...]) -> None:
    for cluster in clusters:
        cluster.points = *(filter(lambda point: point.cluster == cluster, points)),


# To set new epicenter
def update_epicenter(clusters: list[Cluster], points: tuple[Point, ...]) -> None:
    for cluster in clusters:
        pts = *(filter(lambda point: point.cluster == cluster, points)),
        if len(pts):  # Only for clusters with points
            cluster.epi_x = mean(point.x for point in pts)
            cluster.epi_y = mean(point.y for point in pts)

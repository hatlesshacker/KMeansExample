""" File for predicting Probabilities"""
import points
from auxiliary import Cluster, s_down


# Predicts Probability of a student for being in a cluster
def predict(clusters: list[Cluster]) -> None:
    x = int(input("Enter Student's Attendance: "))
    y = int(input("Enter Student's Marks: "))

    epi_xs = [cluster.epi_x for cluster in clusters]
    epi_ys = [cluster.epi_y for cluster in clusters]

    distances = [s_down(points.distance(epi_x, epi_y, x, y)) for epi_x, epi_y in zip(epi_xs, epi_ys)]

    for cluster, dist in zip(clusters, distances):
        print(f"Probability for {cluster.title}: {s_down((1 - dist / sum(distances)) * 100)}")

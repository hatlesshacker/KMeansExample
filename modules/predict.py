""" File for predicting Probabilities"""
import points
from auxiliary import Cluster, Point


# Predicts Probability of a student for being in a cluster
def predict(clusters: list[Cluster]) -> None:
    x = int(input("Enter Student's Attendance: "))
    y = int(input("Enter Student's Marks: "))

    distances = [points.distance(cluster, Point(x, y)) for cluster in clusters]
    for cluster, dist in zip(clusters, distances):
        print(f"Probability for Cluster {cluster.title}: {1 - dist / sum(distances):.2%}")

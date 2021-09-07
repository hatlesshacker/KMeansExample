""" File for performing plotting operations in matplotlib"""
import csv
from itertools import cycle

import matplotlib.pyplot as plt  # type: ignore

from auxiliary import Cluster


# For Basic Preview
def preview(records_file: str) -> None:
    print("Previewing the records: ")
    x_val, y_val = [], []
    with open(records_file, newline="") as File:
        for x, y in csv.reader(File):
            if all((int(x), int(y))):
                x_val.append(int(x))
                y_val.append(int(y))
    plt.title("BASIC PREVIEW OF DATA")
    plt.scatter(x_val, y_val)
    plt.xlabel("Student's Marks")
    plt.ylabel("Student's Attendance")
    plt.show()


# Generator to fetch unlimited colors
def fetch_colors():
    yield from cycle(("magenta", "blue", "green", "black",
                      "pink", "orange", "cyan", "darkgreen"))


# To preview with colors and legend
def rich_preview(clusters: list[Cluster]) -> None:
    for cluster, color in zip(clusters, fetch_colors()):
        points = cluster.points
        plt.scatter([point.x for point in points], [point.y for point in points],
                    c=color, label=cluster.title)
    # For Plotting Epicenters
    plt.scatter([cluster.epi_x for cluster in clusters], [cluster.epi_y for cluster in clusters], s=200,
                c='yellow', marker='^', edgecolor='red', label='Epicenters', )
    plt.title("RICH PREVIEW FOR DATA")
    plt.xlabel("Student's Marks")
    plt.ylabel("Student's Attendance")
    plt.legend(loc="upper left")
    plt.show()


# To bar_plot number of points in each cluster
def bar_plot(clusters: list[Cluster]) -> None:
    plt.title("BAR PLOT VISUALIZATION OF CLUSTER POINTS")
    n_points = [len(cluster.points) for cluster in clusters]
    for i, (n, color) in enumerate(zip(n_points, fetch_colors())):
        plt.bar(i, n, width=.5, color=color)
        plt.annotate(xy=(i - .05, n + .1), text=n)
    plt.xticks(range(len(n_points)), [cluster.title for cluster in clusters])
    plt.xlabel("Clusters")
    plt.ylabel("Number of Students")
    plt.grid(True)
    plt.show()


# To pie plot percentage weightage of clusters
def pie_plot(clusters: list[Cluster]) -> None:
    plt.title("PIE PLOT VISUALIZATION OF CLUSTER POINTS")
    colors = cycle(("mediumorchid", "teal", "slategray", "lightcoral", "darksalmon", "palegreen"))
    n_points = [len(cluster.points) for cluster in clusters]
    plt.pie(n_points, shadow=True,
            labels=[cluster.title for cluster in clusters],
            autopct=lambda pct: f"{pct:.2f}%\n({round(sum(n_points) * pct / 100)} points)",
            colors=(next(colors) for _ in range(len(clusters))),
            explode=[.3 if n == min(n_points) else 0 for n in n_points])
    plt.gcf().gca().add_artist(plt.Circle((.02, .027), 0.2, fc='grey'))  # Shadow
    plt.gcf().gca().add_artist(plt.Circle((0, 0), .2, fc='white'))  # center Circle
    plt.show()

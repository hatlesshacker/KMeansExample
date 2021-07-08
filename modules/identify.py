"""For for setting identifiers to clusters"""

from auxiliary import Cluster


# Function to set title of clusters
def name_clusters(clusters: list[Cluster], setup: bool) -> None:
    if setup:
        if input("Names have already been set. Do you want to repeat? (y/n)") == "n":
            return

    print(f"\n{len(clusters)} clusters have been identified")
    for cluster in clusters:
        print(f" - Cluster {cluster.title}: {cluster} has {len(cluster.points)} points.")
    print()

    for _, cluster in enumerate(clusters, 1):
        cluster.title = input(f"Enter title for cluster {_}: ")

    print("Names set.")

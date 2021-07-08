"""
CHANGE LOG:
- 8th July 2021
- Tested with all files under data/
- Fixed prediction functionality in clusters.py
    -> HOW ?: Resolved some conflict of global and
            local vars in update_epicenter
    -> Removed s_down function and made minor changes
- In auxiliary.py:
    -> Renamed class var Points.cl to Point.cluster
    -> Removed s_down function
    -> Added __repr__() magic functions in 2 Classes
- In points.py:
    -> distance takes cluster and point directly to return distances
    -> get_next directly returns Point instead of index of point
    -> View now displays cluster contents before asking for user input
- In predict.py:
    -> Replaced use of s_down to f-string in predict function
- In preview.py:
    -> Fixed preview() function
    -> Removed get_colours() and added itertools.cycle() iterator
    -> Added few more colours to cycle through
"""

import modules.clusters as ct
import modules.identify as identify
import modules.points as pt
import modules.predict as predict
import modules.preview as preview
from modules.auxiliary import BooleanVar, Point, Cluster

# Globals
trained = BooleanVar()
named = BooleanVar()
clusters: list[Cluster] = []


# STEP 1: Obtain points
# STEP 2: Create clusters
# STEP 3: Get next point to work on
# STEP 4: Assign point to cluster
# STEP 5: Update epicenters
# STEP 6: Repeat STEP 3 until epicenters don't change
# STEP 7: Finalize Clusters

# To initialize and set Points to Clusters
def train(csv: str) -> None:
    points: list[Point] = pt.setup(pt.get_points(csv))  # STEP 1: Obtain points
    no_clusters: int = int(input("\nEnter the number of clusters clearly visible in plot: "))

    clusters.clear()
    clusters.extend([Cluster(n + 1) for n in range(no_clusters)])  # STEP 2: Create clusters
    for _ in range(len(points) * 5):  # Run assignment
        pt.assign_next(clusters, points)
        ct.update_epicenter(clusters, points)

    while True:  # STEP 3: Get next point to work on
        # record sum of previous epicenters:
        pre_x = sum([cluster.epi_x for cluster in clusters])
        pre_y = sum([cluster.epi_y for cluster in clusters])

        pt.assign_next(clusters, points)  # STEP 4: Assign point to cluster
        ct.update_epicenter(clusters, points)  # STEP 5: Update epicenters

        # record sum of new epicenters:
        new_x = sum([cluster.epi_x for cluster in clusters])
        new_y = sum([cluster.epi_y for cluster in clusters])

        # STEP 6: Repeat STEP 3 until epicenters don't change
        delta_xy = abs(pre_x - new_x) + abs(pre_y - new_y)
        if delta_xy == 0:
            break

    ct.finalize(clusters, points)  # STEP 7: Finalize Clusters
    print("Hopefully, now the epicenters are correctly arranged")
    trained.set(True)


if __name__ == '__main__':
    print(" ** \n Welcome to KMeansExample.\n **\n")
    csv_file = input("Please enter the csv file containing the student records: ")
    print(f"Working on student records at {csv_file}..")
    while True:
        print("\n  * (1) for Previewing the records")
        print("  * (2) for Proceeding with training")
        print("  * (3) for Exiting the predictor")

        if trained.get():
            print("  * (4) for Getting Prediction")
            print("  * (5) for Rich preview")
            print("  * (6) for Naming clusters")
            print("  * (7) for Viewing points")

        choice = int(input("Enter action: "))

        if choice == 1:  # Previewing the records
            preview.preview(csv_file)

        elif choice == 2:  # Training data
            train(csv_file)

        elif choice == 3:  # Exiting Program
            break

        elif choice == 4:  # Predict Cluster of Student
            predict.predict(clusters)

        elif choice == 5:  # Plots more detailed preview
            preview.rich_preview(clusters)

        elif choice == 6:  # Naming Clusters
            identify.name_clusters(clusters, named.get())
            named.set(True)

        elif choice == 7:  # Plots a basic View
            pt.view(clusters)

    print("\nThank you for using the predictor! ")

"""
CHANGE LOG:
- 10th July 2021
- Minor changes in code
- Added:
    -> tkinter GUI prompt for choosing csv files
    -> Visualisation of Cluster epicenters

- In main.py:
    -> Increased assignment from 5 times to 7 times for better results
    -> Removed 'csv' parameter from train()
        as it's already globally available
    -> Changed point list to tuple d-type for faster execution and reduce memory
- In auxiliary.py
    -> Changed Cluster points from mutable list to immutable tuple type
       for better execution time and memory
- In clusters.py
    -> Replaced usage of get_points_cl to filter functions
- In points.py
    -> Replaced usage of math module with exponential operators
    -> Removed get_points_cl function as it is deprecated now
"""

from tkinter import Tk
from tkinter.filedialog import askopenfilename as aofn

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
# STEP 7: Finally assign all points to clusters

# To initialize and set Points to Clusters
def train() -> None:
    points: tuple[Point, ...] = pt.setup(pt.get_points(csv_file))  # STEP 1: Obtain points
    n_clusters: int = int(input("\nEnter the number of clusters clearly visible in plot: "))

    clusters.clear()
    clusters.extend([Cluster(n + 1) for n in range(n_clusters)])  # STEP 2: Create clusters
    for _ in range(len(points) * 7):  # Run assignment
        pt.assign_next(clusters, points)
        ct.update_epicenter(clusters, points)

    while True:  # STEP 3: Get next point to work on
        # record sum of previous epicenters:
        pre_x = sum(cluster.epi_x for cluster in clusters)
        pre_y = sum(cluster.epi_y for cluster in clusters)

        pt.assign_next(clusters, points)  # STEP 4: Assign point to cluster
        ct.update_epicenter(clusters, points)  # STEP 5: Update epicenters

        # record sum of new epicenters:
        new_x = sum(cluster.epi_x for cluster in clusters)
        new_y = sum(cluster.epi_y for cluster in clusters)

        # STEP 6: Repeat STEP 3 until epicenters don't change
        delta_xy = abs(pre_x - new_x) + abs(pre_y - new_y)
        if delta_xy == 0:
            break

    # STEP 7: Finally assigning all points to clusters
    ct.finalize(clusters, points)
    print("Hopefully, now the epicenters are correctly arranged")
    trained.set(True)


if __name__ == '__main__':
    Tk().withdraw()
    print(" ** \n Welcome to KMeansExample.\n **\n")
    file_path = aofn(initialdir='data', title="Select a csv file", filetypes=(("csv files", "*.csv"),))
    csv_file = file_path[file_path.rfind('/') - 4:]

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
            train()

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

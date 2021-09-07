"""
CHANGE LOG:
- 7th September 2021
- Major changes in code
- Added:
    -> Bar Plot Visualization of number of points in each cluster
    -> Pie Plot Visualization of Weightage of Clusters in overall

- In main.py:
    -> 2 new menu functionalities of bar & pie plot
    -> Added Notifications for Ongoing Training Process

- In auxiliary.py:
    -> Added a new @property in Cluster: epicenter() to return epicenter
    -> Added a new @property in Points: coordinates() to return coordinate

- In identify.py:
    -> Added a prompt to retain previous Cluster title

- In points.py:
    -> inside view() function:
        - Added prompt to return to main menu
        - Added Error safety for IndexError in list
        - Now Each Points of Cluster prints on new line

- In previews.py:
    -> Added Headings for each plots
    -> Added a new generator to yield colors: fetch_colors()
    -> Added 2 new functions to visualize data:
        - bar_plot()
        - pie_plot()


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
TRAINED = BooleanVar()
NAMED = BooleanVar()
CLUSTERS: list[Cluster] = []


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
    print("Please wait while the Training Process is ongoing...")
    CLUSTERS.clear()
    CLUSTERS.extend([Cluster(n + 1) for n in range(n_clusters)])  # STEP 2: Create clusters
    for _ in range(len(points) * 7):  # Run assignment
        pt.assign_next(CLUSTERS, points)
        ct.update_epicenter(CLUSTERS, points)

    while True:  # STEP 3: Get next point to work on
        # record sum of previous epicenters:
        pre_x = sum(cluster.epi_x for cluster in CLUSTERS)
        pre_y = sum(cluster.epi_y for cluster in CLUSTERS)

        pt.assign_next(CLUSTERS, points)  # STEP 4: Assign point to cluster
        ct.update_epicenter(CLUSTERS, points)  # STEP 5: Update epicenters

        # record sum of new epicenters:
        new_x = sum(cluster.epi_x for cluster in CLUSTERS)
        new_y = sum(cluster.epi_y for cluster in CLUSTERS)

        # STEP 6: Repeat STEP 3 until epicenters don't change
        delta_xy = abs(pre_x - new_x) + abs(pre_y - new_y)
        if delta_xy == 0:
            break

    # STEP 7: Finally assigning all points to clusters
    ct.finalize(CLUSTERS, points)
    print("Hopefully, the new epicenters are correctly arranged")
    TRAINED.set(True)


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

        if TRAINED.get():
            print("  * (4) for Getting Prediction")
            print("  * (5) for Rich preview")
            print("  * (6) for Naming clusters")
            print("  * (7) for Viewing points")
            print("  * (8) for Bar plot visualization of Clusters")
            print("  * (9) for Pie plot visualization of Clusters")

        choice = int(input("Enter action: "))

        if choice == 1:  # Previewing the records - Plots a basic view
            preview.preview(csv_file)

        elif choice == 2:  # Training data
            train()

        elif choice == 3:  # Exiting Program
            break

        elif choice == 4:  # Predict Cluster of Student
            predict.predict(CLUSTERS)

        elif choice == 5:  # Plots more detailed preview
            preview.rich_preview(CLUSTERS)

        elif choice == 6:  # Naming Clusters
            identify.name_clusters(CLUSTERS, NAMED.get())
            NAMED.set(True)

        elif choice == 7:  # Plots a basic View
            pt.view(CLUSTERS)

        elif choice == 8:  # Plots a bar graph representation
            preview.bar_plot(CLUSTERS)

        elif choice == 9:  # Plots a pie chart representation
            preview.pie_plot(CLUSTERS)

        else:
            print("This function is not available yet")

    print("\nThank you for using the predictor! ")

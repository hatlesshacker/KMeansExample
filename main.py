"""
CHANGE LOG:
>> 4th July 2021
>> Optimised import statements
>> Refactored and Reduced Code
>> Edited README.md
>> Removed:
    - Global Booleans
    - Debug Print statements
    - Redundant Comments
    - Redundant import statements
    - Global list of Clusters and Points
    - Dictionaries for Clusters and Points
    - Number of Cluster and Points
>> Added:
    - Function comments
    - Using mypy type checker added Type Hinting
    - Every STEP comments in main->train() function
    - List comprehensions and enumerate() to reduce code
    - Initialized 'modules' folder to segregate all files
    - Created 'auxiliary.py' to keep commonly used
        - classes:
            - BooleanVar -> to tackle global boolean variables
            - Cluster -> to make Cluster Objects
            - Point -> to make Point objects
        - functions:
            - s_down
>> Renamed:
    - Few variables using PEP 8 convention
    - Few functions using PEP 8 convention
    - 'ident.py' to identify.py
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

glob_nos_clusters = 0
glob_cluster_list = []


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
    no_clusters: int = int(input("\nEnter the number of clusters to clearly visualize in plot: "))

    for n in range(no_clusters):  # STEP 2: Create clusters
        clusters.append(Cluster(n + 1))

    for _ in range(len(points) * 5):  # Run assignment
        pt.assign_next(clusters, points)
        ct.update_epicenter(clusters, points)

    while True:  # STEP 3: Get next point to work on
        # record previous epicenters:
        prev_x = sum([cluster.epi_x for cluster in clusters])
        prev_y = sum([cluster.epi_y for cluster in clusters])

        pt.assign_next(clusters, points)  # STEP 4: Assign point to cluster
        ct.update_epicenter(clusters, points)  # STEP 5: Update epicenters

        # record new epicenters:
        new_x = sum([cluster.epi_x for cluster in clusters])
        new_y = sum([cluster.epi_y for cluster in clusters])

        # STEP 6: Repeat STEP 3 until epicenters don't change
        if abs(prev_x - new_x) + abs(prev_y - new_y) == 0:
            break

    ct.finalize(clusters, points)  # STEP 7: Finalize Clusters

    print("Hopefully, now the epicenters are correctly arranged")
    trained.set(True)


if __name__ == '__main__':
    print(" ** \n Welcome to KMeansExample.\n **\n")
    csv_file = input("Please enter the csv file containing the student records: ")  # 'data/simple.csv'
    print(f"Working on student records at {csv_file}..")
    while True:
        print("\n  * (1) for previewing the records")
        print("  * (2) for proceeding with training")
        print("  * (3) for Exiting the predictor")

        if trained.get():
            print("  * (4) for Getting Prediction")
            print("  * (5) for Rich preview")
            print("  * (6) for Naming clusters")
            print("  * (7) for Viewing points")

        choice = int(input("Enter action: "))  # 2

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

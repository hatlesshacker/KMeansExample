import matplotlib.pyplot as plt
import csv
import random

import points
import ident
import preview
import clusters
import predict

glob_trained = False
glob_named = False
csvfile = ""

glob_nos_clusters = 0
glob_cluster_list = []

glob_nos_points = 0
glob_points_list = []


# STEP 1: Obtain and register points globally
# STEP 2: Create clusters and register them globally
# STEP 3: Get next point to work on
# STEP 4: Assign point to cluster
# STEP 5: Update epicenters
# STEP 6: Repeat 3 until epicenters don't change


def train(csvfile):

    # STEP 1
    global glob_points_list
    global glob_nos_points
    points_raw = points.getpoints(csvfile)
    glob_points_list = points.setup(points_raw)
    glob_nos_points = len(glob_points_list)

    # STEP 2
    global glob_nos_clusters
    global glob_cluster_list

    glob_cluster_list = []
    glob_nos_clusters = 0

    glob_nos_clusters = int(
        input("\nEnter the number of clusters clearly visible in the plot: ")
    )
    for i in range(1, glob_nos_clusters + 1):
        temp_dict = {}
        temp_dict["epi_x"] = random.randint(1, 10)
        temp_dict["epi_y"] = random.randint(1, 10)
        temp_dict["points"] = []
        temp_dict["title"] = i

        glob_cluster_list.append(temp_dict)
    # print("- Initialized ", glob_nos_clusters, " clusters")

    # print ("INIT DEBUG \n")
    # for k in glob_cluster_list:
    #    print (k['epi_x'], k['epi_y'], end=" ")
    #    print()

    for l in range(glob_nos_points * 5):
        # Run assignment
        glob_points_list = points.nextassign(glob_cluster_list, glob_points_list)
        glob_cluster_list = clusters.update_epi(glob_cluster_list, glob_points_list)

    # STEP 3
    while True:
        prev_x = prev_y = 0
        new_x = new_y = 0
        change = 0

        # record previous epicenters:
        for i in glob_cluster_list:
            prev_x += i["epi_x"]
            prev_y += i["epi_y"]

        # Run assignment
        glob_points_list = points.nextassign(glob_cluster_list, glob_points_list)
        glob_cluster_list = clusters.update_epi(glob_cluster_list, glob_points_list)

        # record new epicenters:
        for j in glob_cluster_list:
            new_x += j["epi_x"]
            new_y += j["epi_y"]

        change = abs(prev_x - new_x) + abs(prev_y - new_y)
        if change == 0:
            break

    print("FIN DEBUG \n")
    for k in glob_cluster_list:
        print(k["epi_x"], k["epi_y"], end=" ")
        print()
    # print ("\n\nPOINTS:: ")
    # for p in glob_points_list:
    #    print(p)

    glob_cluster_list = clusters.finalize(glob_cluster_list, glob_points_list)

    print("Hopefully, now the epicenters are correctly arranged")
    global glob_trained
    glob_trained = True


print(" ** \n Welcome to KMeansExample.\n **\n")
csvfile = input("Please enter the csv file containing the student records: ")
# csvfile = 'data/simple.csv'
print("Working on student records at ", csvfile, " ..")

while True:
    print("\n\n")
    print("  * (1) for previewing the records")
    print("  * (2) for proceeding with training")
    print("  * (3) for getting a prediction")
    print("  * (4) for Exiting the predictor")

    if glob_trained == True:
        print("  * (5) for Rich preview")
        print("  * (6) for Naming clusters")
        print("  * (7) for Viewing points")

    i = int(input("Enter action: "))

    if i == 1:
        print("Previewing the records: ")
        preview.preview(csvfile)

    elif i == 2:
        train(csvfile)

    elif i == 3:
        predict.predict(glob_cluster_list)

    elif i == 4:
        break

    elif i == 5:
        pass
        preview.richprev(glob_cluster_list)

    elif i == 6:
        ret = ident.nameclusters(glob_cluster_list, glob_named)
        glob_cluster_list = ret[0]
        glob_named = ret[1]
        print("Names set.")

    elif i == 7:
        points.view(glob_cluster_list)

print("\nThank you for using the predictor! ")

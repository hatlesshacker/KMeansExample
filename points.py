import csv
import random
import clusters as clusterclass



# returns an array of points currently present in a given cluster.
def getpoints_cl(points , cl_no):
	retarray = []
	for point in points:
		if point['cl'] == cl_no:
			retarray.append(point)

	return retarray




# retrieves all points from a given csv file,
# and returns the raw point list.
def getpoints(filename):
    xvals=[]    
    yvals=[]
    retarray=[]

    with open(filename, newline='') as File:
	    reader=csv.reader(File)
	    for row in reader:
		    x1 = row[0]
		    y1 = row[1]

		    if x1 == '' or y1 == '':
			    continue

		    xvals.append(x1)
		    yvals.append(y1)

    retarray.append(xvals)
    retarray.append(yvals)

    return retarray




# takes the raw points list as argument andf returns the
# properly setup points list that is to be used later.
def setup(raw):
	xvals = raw[0]
	yvals = raw[1]
	length = len(raw[0])
	retarray = []

	for i in range (1, length+1):
		temp_point = {}
		temp_point['x']  = xvals[i-1]
		temp_point['y']  = yvals[i-1]
		temp_point['cl'] = 'u'

		retarray.append(temp_point)

	return retarray




# takes the formated points list as argument and returns
# the next point that is to be worked on.
def getnext(points):
	# first look for points that have so fatr not been assigned to any cluster.
	for p in points:
		if p['cl'] == 'u':
			return points.index(p)
		else:
			continue

	# If we reached this far, all points have been assigned to some cluster.
	idx = random.randint(0, len(points)-1)
	return idx




# assigns the next point to its nearest cluster.
def nextassign(clusters, points):
	point_idx = getnext(points)
	point = points[point_idx]
	#print("DBG::", point)

	distances = []    
	#LOOP TO CALCULATE DISTANCES FROM EACH CLUSTER
	for i in range(1, len(clusters)+1):
		min_idx = 0
		epi_x = clusters[i-1] ['epi_x']
		epi_y = clusters[i-1] ['epi_y']
		temp_dist = clusterclass.dist(int(epi_x), int(epi_y), int(point['x']), int(point['y']))
		distances.append(temp_dist)
        
	min_idx = distances.index(min(distances))
	#print(distances)
	points[point_idx] ['cl'] = min_idx
	return points


def view(clusters):
    cl_no = int(input("Enter the cluster number: "))
    cluster = clusters[cl_no-1]
    points = cluster['points'] [0]
    print(cluster['title'], "has ", len(points), "elements.")
    ex = cluster['epi_x']
    ey = cluster['epi_y']
    print("(", ex, ",", ey, ")")
    for i in points:
        print("<", i['x'], i['y'], ">", end=" ")

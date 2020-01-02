import matplotlib.pyplot as plt
import csv

def preview(records_file):
    xvals = []
    yvals = []
    with open(records_file, newline='') as File:
	    reader=csv.reader(File)
	    for row in reader:
		    x1 = row[0]
		    y1 = row[1]

		    if x1 == '' or y1 == '':
			    continue

		    xvals.append(x1)
		    yvals.append(y1)

    plt.scatter(xvals,yvals)
    plt.show()

def getcolors(n):
    #recieve n number of colors from the user
    colors=[]
    for i in range (1, n+1):
        colors.append(input("  - Enter a color: "))
    
    #return colors
    return ['red', 'blue', 'green', 'black']


def richprev(clusters):
    i = 0
    clrs = getcolors(len(clusters))
    for cluster in clusters:
        xvals = []
        yvals = []
        points = cluster['points']
        points = points[0]
        #EXTRACT X VALUES
        for x in points:
            xvals.append(x['x'])
        #REXTRACT Y VALUES
        for y in points:
            yvals.append(y['y'])

        
        plt.scatter(xvals,yvals, color=clrs[i])
        i+=1
    plt.show()

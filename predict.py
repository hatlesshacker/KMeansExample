import clusters as cluster_dist

def sdown(x):
    y = x*100
    z = int(y)
    return (z/100)


def predict(clusters):
    x = int(input("Enter Student's Attendance: "))
    y = int(input("Enter Student's Marks: "))

    epi_x = []
    epi_y = []

    for _c in clusters:
        epi_x.append(_c['epi_x'])
        epi_y.append(_c['epi_y'])

    distances = []

    for i in range(1, len(epi_x)+1):
        distances.append(sdown(cluster_dist.dist(epi_x[i-1], epi_y[i-1], x, y)))
    
    net_dist = 0
    for __d in distances:
        net_dist += __d
    
    probs = []
    j=0
    for k in clusters:
        print("Probablity for ", k['title'], ": ", sdown(((1-(distances[j]/net_dist))*100)))
        j += 1
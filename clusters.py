import points as pointsclass
import math


def sdown(x):
    y = x * 10000
    z = int(y)
    return z / 10000


def dist(epi_x, epi_y, pt_x, pt_y):
    # return (((epi_x-pt_x)**2) + ((epi_y-pt_y)**2))**0.5
    return math.sqrt(math.pow(epi_x - pt_x, 2.0) + math.pow(epi_y - pt_y, 2.0))


def finalize(clusters, points):
    nos = len(clusters)
    for i in range(1, nos + 1):
        pts = pointsclass.getpoints_cl(points, i - 1)
        clusters[i - 1]["points"].append(pts)
    return clusters


def update_epi(clusters, points):

    for i in range(1, len(clusters) + 1):
        xsum = 0
        ysum = 0

        pts = pointsclass.getpoints_cl(points, i - 1)
        net = len(pts)

        # Ignore clusters with no points
        if net == 0:
            continue

        for x in pts:
            xsum += int(x["x"])
        for y in pts:
            ysum += int(y["y"])

        xav = xsum / net
        yav = ysum / net

        clusters[i - 1]["epi_x"] = xav
        clusters[i - 1]["epi_y"] = yav

        # print(i, clusters[i-1]['epi_x'], clusters[i-1]['epi_y'])

    return clusters

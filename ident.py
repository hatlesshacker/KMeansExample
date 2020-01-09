def sdown(x):
    y = x * 100
    z = int(y)
    return z / 100


def nameclusters(clusters, setup):

    if setup == True:
        rep = input("Names have already been set. Do you want to repeat? (y/n)")
        if rep == "n":
            return [clusters, setup]
        else:
            pass

    i = 1
    print()

    print(len(clusters), "clusters have been identified.")
    for c0 in clusters:
        pts = len(c0["points"][0])
        print(" - Cluster", i, "has ", pts, "elements.")
        i += 1
    print()

    i = 1
    for c1 in clusters:
        print(
            " - Cluster", i, ": ", "(", sdown(c1["epi_x"]), ",", sdown(c1["epi_y"]), ")"
        )
        i += 1
    print()

    i = 1
    for c2 in clusters:
        print(" - Enter title for cluster ", i, end="")
        c2["title"] = input(": ")
        i += 1

    return [clusters, True]

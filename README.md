# KMeansExample

    updated on: 8th July 2021 

<a href="https://madewithlove.org.in" target="_blank">Made with <span style="color: #e74c3c">&hearts;</span> in
India</a>

KMeansExample is a simple implementation of the K Means clustering Algorithm in Python. Some features of it include:

- Accurate division of clusters
- Graphic preview of clusters
- Naming of clusters
- Making Predictions

### Requirements

KMeansExample Requires these bare-minimum things to work:

* [python 3.x] - Python 3 and above
* [matplotlib] for previewing the data . If not installed  `pip install matplotlib`

### Installation

KMeansExample doesn't need to be installed, just run main.py with no parameters.

```sh
$ python3 main.py
```

### Using

```sh
$ python3 main.py
 ** 
 Welcome to KMeansExample.
 **

Please enter the csv file containing the student records:
```

enter the name of the CSV file containing the data. Few CSV files have already been provided with this repository.

```sh
$ python3 main.py 
 ** 
 Welcome to KMeansExample.
 **

Please enter the csv file containing the student records: data/test.csv
Working on student records at  data/test.csv  ..



  * (1) for Previewing the records
  * (2) for Proceeding with training
  * (3) for Exiting the predictor
Enter action: 

```

hereafter, the menu interface will guide you.

### Todos

- Add GUI prompt while choosing CSV file from directory
- Reduce and Optimise Code using Numpy
- Display epicenters of Clusters in Rich Preview

### License

- See [LICENSE]

### ChangeLog

- See [CHANGELOG]

### Preview
- Rich plotting of Clusters in a dataset _students.csv_
![Preview]

**Syed Nasim, 2021**

[matplotlib]: https://pypi.org/project/matplotlib/

[python 3.x]: https://www.python.org/download/releases/3.0/

[LICENSE]: LICENSE

[CHANGELOG]: CHANGELOG.md

[Preview]: data/img/students.png
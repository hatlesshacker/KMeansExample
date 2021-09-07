# CHANGELOG

    updated on: 7th September 2021

### _7th September 2021_

- Major changes in code
- Added:
  - Bar Plot Visualization of number of points in each cluster
  - Pie Plot Visualization of Weightage of Clusters in overall
- In main.py:
  - 2 new menu functionalities of bar & pie plot
  - Added Notifications for Ongoing Training Process
- In auxiliary.py:
  - Added a new @property in Cluster: `epicenter()` to return epicenter
  - Added a new @property in Points: `coordinates()` to return coordinate
- In identify.py:
  - Added a prompt to retain previous Cluster title
- In points.py:
  - Inside view() function:
    - Added prompt to return to main menu
    - Added Error safety for IndexError in list
  - Now Each Points of Cluster prints on new line
- In previews.py:
  - Added Headings for each plots
  - Added a new generator to yield colors: `fetch_colors()`
  - Added 2 new functions to visualize data:
    - `bar_plot()`
    - `pie_plot()`

### _10th July 2021_

- Minor changes in code
- Added:
  - tkinter GUI prompt for choosing csv files
  - Visualisation of Cluster epicenters
- In main.py:
  - Increased assignment from 5 times to 7 times for better results
  - Removed 'csv' parameter from `train()` as it's already globally available
  - Changed point list to tuple d-type for faster execution and reduce memory
- In auxiliary.py:
  - Changed Cluster points from mutable list to immutable tuple type for better execution time and memory
- In clusters.py:
  - Replaced usage of `get_points_cl()` to filter functions
- In points.py:
  - Replaced usage of math module with exponential operators
  - Removed `get_points_cl()` function as it is deprecated now

### _8th July 2021_

- Tested with all files under data/
- Fixed prediction functionality in clusters.py
  - HOW ?: Resolved some conflict of global and local vars in `update_epicenter()`
  - Removed `s_down()` and made minor changes
- In auxiliary.py:
  - Renamed class var Points.cl to Point.cluster
  - Removed `s_down()`
  - Added `__repr__()` magic functions in 2 Classes
- In points.py:
  - distance takes cluster and point directly to return distances
  - `get_next()` directly returns Point instead of index of point
  - View now displays cluster contents before asking for user input
- In predict.py:
  - Replaced use of `s_down()` with f-string in predict function
- In preview.py:
  - Fixed `preview()` function
  - Removed `get_colours()` and added `itertools.cycle()` iterator
  - Added few more colours to cycle through

### _4th July 2021_

- Optimised import statements
- Refactored and Reduced Code
- Edited README.md
- Added:
  - Function comments
  - Using mypy type checker added Type Hinting
  - Every STEP comments in main -> `train()` function
  - List comprehensions and `enumerate()` to reduce code
  - Initialized 'modules' folder to segregate all files
  - Created 'auxiliary.py' to keep commonly used
    - classes:
      - BooleanVar -> to tackle global boolean variables
      - Cluster -> to make Cluster Objects
      - Point -> to make Point objects
    - functions:
      - s_down
- Removed:
  - Global Booleans
  - Debug Print statements
  - Redundant Comments
  - Redundant import statements
  - Global list of Clusters and Points
  - Dictionaries for Clusters and Points
  - Number of Cluster and Points
- Renamed:
  - Few variables using PEP 8 convention
  - Few functions using PEP 8 convention
  - 'ident.py' to identify.py

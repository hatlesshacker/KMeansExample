# CHANGELOG

    updated on: 8th July 2021 

### _8th July 2021_

- Tested with all files under data/
- Fixed prediction functionality in clusters.py
  - HOW ?: Resolved some conflict of global and 
           local vars in ```update_epicenter()``` 
  - Removed ```s_down()``` and made minor changes
- In auxiliary.py:
  - Renamed class var Points.cl to Point.cluster
  - Removed ```s_down()```
  - Added ```__repr__()``` magic functions in 2 Classes
- In points.py:
  - distance takes cluster and point directly to return distances
  - ```get_next()``` directly returns Point instead of index of point
  - View now displays cluster contents before asking for user input
- In predict.py:
  - Replaced use of ```s_down()``` with f-string in predict function
- In preview.py:
  - Fixed ```preview()``` function
  - Removed ```get_colours()``` and added ```itertools.cycle()``` iterator
  - Added few more colours to cycle through

### _4th July 2021_

- Optimised import statements
- Refactored and Reduced Code
- Edited README.md
- Removed:
  - Global Booleans
  - Debug Print statements
  - Redundant Comments
  - Redundant import statements
  - Global list of Clusters and Points
  - Dictionaries for Clusters and Points
  - Number of Cluster and Points
- Added:
  - Function comments
  - Using mypy type checker added Type Hinting
  - Every STEP comments in main -> train() function
  - List comprehensions and enumerate() to reduce code
  - Initialized 'modules' folder to segregate all files
  - Created 'auxiliary.py' to keep commonly used
    - classes:
      - BooleanVar -> to tackle global boolean variables
      - Cluster -> to make Cluster Objects
      - Point -> to make Point objects
    - functions:
      - s_down
- Renamed:
  - Few variables using PEP 8 convention
  - Few functions using PEP 8 convention
  - 'ident.py' to identify.py
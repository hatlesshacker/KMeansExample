# CHANGE LOG

    updated on: 4th July 2021 

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
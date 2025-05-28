#  Family Relationship Resolver

## Features

- Determines familial relationships between two people in a family.
- Supports parent, grandparent, spouse, uncle, aunt, and more.
- Uses breadth-first traversal to trace lineage and marriage paths.
- Gender-aware relationship naming (e.g., "uncle" vs. "aunt").
- Extensible via relationship path dictionary in `relationships.py`.
- The program takes three required command-line arguments: a path to a JSON file of people and relationships (such as family.json) and two names from the JSON file.

## Input Format

The input JSON file must contain:
- A dictionary of `individuals` (name and gender)
- A dictionary of `parents` (child and list of parent names)
- A list of `couples` (name pairs)

  **Example:**
```json
{
  "individuals": {
    "Alice": "female",
    "Bob": "male",
    "Carol": "female"
  },
  "parents": {
    "Bob": ["Alice", "Carol"]
  },
  "couples": [
    ["Alice", "Carol"]
  ]
}
```
## Output Format

The program prints the relationship between two people:

`Alice is Bob's mother`

If no relationship is found:

`Alice is not related to Bob`

## How to Run

- Make sure you have Python 3.x installed.
- No external libraries required (only argparse, re, and sys).
- Import the `relationships.py` file for relationships. 
- My program is designed to run from the terminal.
- To run it, open a terminal and ensure you are in the directory where your scripts and JSON file are saved.

The examples below assume you are using macOS and your program is called `kinship.py` and the file hosting the relationship is called `relationships.py` as well as the JSON file being named `family.json`.

If you are using Windows, replace `python3` with `python`.

### Command-line Argument to Run Program

This will print the relationship between any two names in the JSON file: 

`python3 kinship.py family.json Nora Avery`

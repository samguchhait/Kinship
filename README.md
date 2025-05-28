#  Family Relationship Resolver

## Features

- Determines familial relationships between two people in a family.
- Supports parent, grandparent, spouse, uncle, aunt, and more.
- Uses breadth-first traversal to trace lineage and marriage paths.
- Gender-aware relationship naming (e.g., "uncle" vs. "aunt").

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
- My program is designed to run from the terminal.
- To run it, open a terminal and ensure you are in the directory where your script and sample file are saved.






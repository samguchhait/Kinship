import argparse
import json
from relationships import relationships
from sys import argv

class Person:
    """ Represents a person in a family.

    Attributes:
        name (str): a persons name.
    """
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.parents = []
        self.spouse = None

    def add_parent(self, parent):
        self.parents.append(parent)

    def set_spouse(self, spouse):
        self.spouse = spouse

    def connections(self):
        cdict = {self: ""}
        queue = [self]

        while queue:
            person = queue.pop(0)
            personpath = cdict[person]

            for parent in person.parents:
                if parent not in cdict:
                    cdict[parent] = personpath + "P"
                    queue.append(parent)

            if "S" not in personpath and person.spouse and person.spouse not in cdict:
                cdict[person.spouse] = personpath + "S"
                queue.append(person.spouse)
        return cdict

    def relation_to(self, other_person):
        connections_self = self.connections()
        connections_other = other_person.connections()
        shared_relatives = set(connections_self.keys()) & set(connections_other.keys())

        if not shared_relatives:
            return None

        combined_paths = [connections_self[relative] + ":" + connections_other[relative] for relative in shared_relatives]
        lcr_path = min(combined_paths, key=len)

        if lcr_path in relationships:
            kinship_term = relationships[lcr_path][self.gender]
            return kinship_term
        else:
            return "distant relative"

class Family:
    def __init__(self, family_data):
        self.people = {}

        for name, gender in family_data["individuals"].items():
            person = Person(name, gender)
            self.people[name] = person

        for name, parents in family_data["parents"].items():
            child = self.people[name]
            for parent_name in parents:
                parent = self.people[parent_name]
                child.add_parent(parent)

        for couple in family_data["couples"]:
            person1, person2 = map(self.people.get, couple)
            person1.set_spouse(person2)
            person2.set_spouse(person1)

    def relation(self, name1, name2):
        person1 = self.people[name1]
        person2 = self.people[name2]
        return person1.relation_to(person2)

def main(filepath, name1, name2):
    with open(filepath, "r", encoding="utf-8") as f:
        family_data = json.load(f)

    family = Family(family_data)
    relationship = family.relation(name1, name2)

    if relationship is None:
        print(f"{name1} is not related to {name2}")
    else:
        print(f"{name1} is {name2}'s {relationship}")

def parse_args(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", help="Path to the JSON file with family data")
    parser.add_argument("name1", help="Name of the first person")
    parser.add_argument("name2", help="Name of the second person")
    return parser.parse_args(arguments)

if __name__ == "__main__":
    args = parse_args(argv[1:])
    main(args.filepath, args.name1, args.name2)

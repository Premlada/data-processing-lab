
import csv
from pathlib import Path


class DataLoader:
    """Handles loading CSV data files."""

    def __init__(self, base_path=None):
        if base_path is None:
            self.base_path = Path(__file__).parent.resolve()
        else:
            self.base_path = Path(base_path)

    def load_csv(self, filename):
        filepath = self.base_path / filename
        data = []

        with filepath.open(encoding="utf-8-sig", newline="") as f:
            rows = csv.DictReader(f)
            for row in rows:
                data.append(dict(row))

        return data


class DB:
    """Stores and searches tables."""

    def __init__(self):
        self.tables = []

    def insert(self, table):
        self.tables.append(table)

    def search(self, table_name):
        for table in self.tables:
            if table.table_name == table_name:
                return table
        return None


class Table:
    """Represents a table of data."""

    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def filter(self, condition):
        filtered_data = [
            row for row in self.table
            if condition(row)
        ]
        return Table(self.table_name + "_filtered", filtered_data)

    def aggregate(self, aggregation_function, aggregation_key):
        values = [
            row[aggregation_key]
            for row in self.table
        ]

        try:
            values = [float(value) for value in values]
        except (ValueError, TypeError):
            pass

        return aggregation_function(values)

    def join(self, other_table, key):
        joined_data = []

        for row1 in self.table:
            for row2 in other_table.table:
                if row1[key] == row2[key]:
                    joined_row = row1.copy()

                    for column, value in row2.items():
                        if column != key:
                            joined_row[column] = value

                    joined_data.append(joined_row)

        return Table(
            self.table_name + "_" + other_table.table_name + "_joined",
            joined_data
        )

    def __str__(self):
        return self.table_name + ":" + str(self.table)


# Load CSV files
loader = DataLoader()

cities = loader.load_csv("Cities.csv")
table1 = Table("cities", cities)

countries = loader.load_csv("Countries.csv")
table2 = Table("countries", countries)


# Create database
my_DB = DB()
my_DB.insert(table1)
my_DB.insert(table2)


# Search cities table
my_table1 = my_DB.search("cities")

print("List all cities in Italy:")
my_table1_filtered = my_table1.filter(
    lambda x: x["country"] == "Italy"
)
print(my_table1_filtered)
print()


print("Average temperature for all cities in Italy:")
print(
    my_table1_filtered.aggregate(
        lambda x: sum(x) / len(x),
        "temperature"
    )
)
print()


# Search countries table
my_table2 = my_DB.search("countries")

print("List all non-EU countries:")
my_table2_filtered = my_table2.filter(
    lambda x: x["EU"] == "no"
)
print(my_table2_filtered)
print()


print("Number of countries that have coastline:")
print(
    my_table2.filter(
        lambda x: x["coastline"] == "yes"
    ).aggregate(
        lambda x: len(x),
        "coastline"
    )
)
print()


# Join cities and countries
my_table3 = my_table1.join(my_table2, "country")

print("First 5 entries of the joined table (cities and countries):")
for item in my_table3.table[:5]:
    print(item)
print()


print("Cities whose temperatures are below 5.0 in non-EU countries:")
my_table3_filtered = my_table3.filter(
    lambda x: x["EU"] == "no"
).filter(
    lambda x: float(x["temperature"]) < 5.0
)
print(my_table3_filtered.table)
print()


print("The min and max temperatures for cities in EU countries that do not have coastlines")

my_table3_filtered = my_table3.filter(
    lambda x: x["EU"] == "yes"
).filter(
    lambda x: x["coastline"] == "no"
)

print(
    "Min temp:",
    my_table3_filtered.aggregate(
        lambda x: min(x),
        "temperature"
    )
)

print(
    "Max temp:",
    my_table3_filtered.aggregate(
        lambda x: max(x),
        "temperature"
    )
)
print()

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


class Table:
    """Represents a table of data."""

    def __init__(self, name, table):
        self.name = name
        self.table = table

    def filter(self, condition):
        filtered_data = [
            row for row in self.table
            if condition(row)
        ]
        return Table(self.name, filtered_data)

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


# Load data
loader = DataLoader()
cities = loader.load_csv("Cities.csv")

my_table1 = Table("cities", cities)


# 1. Average temperature of all cities
my_value = my_table1.aggregate(
    lambda x: sum(x) / len(x),
    "temperature"
)
print(my_value)
print()


# 2. All cities in Germany
my_cities = my_table1.filter(
    lambda x: x["country"] == "Germany"
)

cities_list = [
    [city["city"], city["country"]]
    for city in my_cities.table
]

print("All the cities in Germany:")
for city in cities_list:
    print(city)
print()


# 3. Cities in Spain with temperature above 12°C
my_cities = my_table1.filter(
    lambda x: x["country"] == "Spain"
    and float(x["temperature"]) > 12.0
)

cities_list = [
    [city["city"], city["country"], city["temperature"]]
    for city in my_cities.table
]

print("All the cities in Spain with temperature above 12°C:")
for city in cities_list:
    print(city)
print()


# 4. Count unique countries
my_countries = my_table1.aggregate(
    lambda x: len(set(x)),
    "country"
)

print("The number of unique countries is:")
print(my_countries)
print()

# 5. Average temperature in Germany
my_value = my_table1.filter(
    lambda x: x["country"] == "Germany"
).aggregate(
    lambda x: sum(x) / len(x),
    "temperature"
)

print("The average temperature of all the cities in Germany:")
print(my_value)
print()


# 6. Maximum temperature in Italy
my_value = my_table1.filter(
    lambda x: x["country"] == "Italy"
).aggregate(
    lambda x: max(x),
    "temperature"
)

print("The max temperature of all the cities in Italy:")
print(my_value)
print()

import csv
import os

# Load Cities.csv
__location__ = os.path.dirname(os.path.abspath(__file__))

cities = []
with open(
    os.path.join(__location__, "Cities.csv"),
    newline="",
    encoding="utf-8-sig"
) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))


# Function to filter dictionaries
def filter_items(condition, dict_list):
    return [item for item in dict_list if condition(item)]


# Function to aggregate values
def aggregate(aggregation_key, aggregation_function, dict_list):
    values = [item[aggregation_key] for item in dict_list]
    return aggregation_function(values)


# Print first 5 cities only
for city in cities[:5]:
    print(city)


# 1. Print the average temperature of all the cities
print("The average temperature of all the cities:")
average_temperature = aggregate(
    "temperature",
    lambda temps: sum(float(t) for t in temps) / len(temps),
    cities
)
print(average_temperature)
print()


# 2. Print all cities in Germany
print("All cities in Germany:")
germany = filter_items(
    lambda city: city["country"] == "Germany",
    cities
)
for city in germany:
    print(city["city"])
print()


# 3. Print all cities in Spain with a temperature above 12°C
print("Cities in Spain with temperature above 12°C:")
spain = filter_items(
    lambda city: city["country"] == "Spain"
    and float(city["temperature"]) > 12,
    cities
)
for city in spain:
    print(city["city"])
print()


# 4. Count the number of unique countries
print("Number of unique countries:")
number_of_countries = aggregate(
    "country",
    lambda countries: len(set(countries)),
    cities
)
print(number_of_countries)
print()


# 5. Print the average temperature for all the cities in Germany
print("The average temperature in Germany:")
average_germany = aggregate(
    "temperature",
    lambda temps: sum(float(t) for t in temps) / len(temps),
    germany
)
print(average_germany)
print()


# 6. Print the max temperature for all the cities in Italy
print("The maximum temperature in Italy:")
italy = filter_items(
    lambda city: city["country"] == "Italy",
    cities
)
max_italy = aggregate(
    "temperature",
    lambda temps: max(float(t) for t in temps),
    italy
)
print(max_italy)
print()

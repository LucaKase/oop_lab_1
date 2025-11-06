import csv
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities
for city in cities[:5]:
    print(city)
# Let's write a function to filter out only items that meet the condition
# Hint: condition will be associated with an anonymous function, e.x., lamdbda x: max(x)


def filter(condition, dict_list):
    temps = []
    for item in dict_list:
        if condition(item):
            temps.append(item)
    return temps


# Let's write a function to do aggregation given an aggregation function and an aggregation key

def aggregate(aggregation_key, aggregation_function, dict_list):
    temps = []
    for item in dict_list:
        try:
            temps.append(float(item[aggregation_key]))
        except ValueError:
            temps.append(item[aggregation_key])
    return aggregation_function(temps)


# Print the average temperature of all the cities
average_temp = aggregate("temperature", lambda x: sum(x)/len(x), cities)
print("Average Temperature of all cities:", average_temp)

# Print all cities in Germany
germany_cities = filter(lambda x: x["country"] == "Germany", cities)
german_cities = []
for item in germany_cities:
    german_cities.append(item["city"])
print("German Cities:", german_cities)

# Print all cities in Spain with a temperature above 12°C
spain = filter(lambda x: x["country"] == "Spain" and float(
    x["temperature"]) > 12, cities)
spain_cities = []
for item in spain:
    spain_cities.append(item["city"])
print("Cities in spain above 12 degrees:", spain_cities)

# Count the number of unique countries
unique_countries = len(set(aggregate("country", lambda x: x, cities)))
print("Number of unique Countries:", unique_countries)

# Print the average temperature for all the cities in Germany
avg_temp_germany = aggregate(
    "temperature", lambda x: sum(x)/len(x), germany_cities)
print("Average Temperature for all cities in Germany:", avg_temp_germany)

# Print the max temperature for all the cities in Italy
italy_cities = filter(lambda x: x["country"] == "Italy", cities)
max_temp_italy = aggregate("temperature", max, italy_cities)
print("Max Temperature in Italy:", max_temp_italy)

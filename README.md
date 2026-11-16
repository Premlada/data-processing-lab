# OOP Data Processing

## 1. Lab Overview

This lab converts procedural data processing code into Object-Oriented Programming (OOP).

It uses Python classes to load CSV files and process tabular data. The program supports filtering and aggregating data.

## 2. Project Structure

```text
data-processing-lab/
├── README.md
├── Cities.csv
└── data_processing.py
```

## 3. Design Overview

### DataLoader Class

Responsible for loading data from CSV files.

- `__init__()` initializes the base directory.
- `load_csv()` reads a CSV file and returns a list of dictionaries.

### Table Class

Responsible for managing and processing tabular data.

- `__init__()` initializes the table name and data.
- `filter()` filters rows based on a given condition and returns a new Table.
- `aggregate()` extracts values from a specified column and applies an aggregation function.

## 4. How to Test and Run

1. Make sure Python 3 is installed.
2. Place `Cities.csv` and `data_processing.py` in the same directory.
3. Open the terminal in the project directory.
4. Run the following command:

```bash
python3 data_processing.py
```

The program displays the results of the data processing operations, including average temperature, filtering cities by country, counting unique countries, and finding maximum temperature.
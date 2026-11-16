## 5. Commit 4: Database and Table Join

### DB Class

The DB class stores and searches tables.

- `__init__()` initializes an empty list of tables.
- `insert()` adds a Table object to the database.
- `search()` finds a table by its name.

### Table Class (Additional Method)

- `join()` combines two tables using a common key and returns a new Table object.

### Additional Dataset

- `Countries.csv` contains country information, including population, EU membership, and coastline status.

### Testing

Run the program using:

```bash
python3 data_processing.py
```

The program tests filtering, aggregation, database searching, and joining cities and countries tables.
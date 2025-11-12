# Data Processing

This Lab is all about reading csv files, processing the input and making some data analysis in different ways. Starting of with procedural and then finishing with OOP. Using different methods to join, aggregate, filter etc. data. Currently using data about cities and countries.

## File Structure

- `data_proccessing.py`: Includes the DataLoader, Table and DB Classes. Furthermore also the Test-Code.
- `Cities.csv`: Includes the raw data of the cities.
- `Countries.csv`: Includes the raw data of the countries.

## DataLoader Class

Located in `data_proccessing.py`, the `DataLoader` class includes:

### Attributes

- `base_path`: The base path to the file.

### Methods

- `load_csv()`: Load a CSV file and return its contents as a list of dictionaries.

## Table Class

Located in `data_proccessing.py`, the `Table` class includes:

### Attributes

- `table` (list): the list of dictionaries.
- `table_name` (str): Name of the data.

### Methods

- `filter()`: returns a new table object with the filtered data, based on the lambda function /condition in the parameters
- `aggregate()`: aggregates the data based on the lambda function and the specific key in the parameters
- `join()`: Creates a new list of dictionaries, a real copy of the object itself the cities table (not with reference to the original table). Based on the "joinParameter" joins / adds the new attributes from the table in the parameters aka the countries table to the corresponding dictionary and then returns a new table object that gets created with the new list including all dictionaries with the combined attributes

## DB Class

Located in `data_proccessing.py`, the `DB` class includes:

### Attributes

- `db` (list): the list of table objects.

### Methods

- `insert()`: adds / appends the table object in the parameters to the db attribute
- `search()`: goes through every object in the db attribute and returns the table object with same name as the name-parameter

## Running the Code

To run the simulation, execute `data_processing.py`:
The output in the terminal should be the same as the result.txt

```bash
python3 data_processing.py
```

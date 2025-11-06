# Data Processing

This Lab is all about reading csv files, processing the input and making some data analysis in different ways. Starting of with procedural and then finishing with OOP.

## File Structure

- `data_proccessing.py`: Includes the DataLoader and Table Classes. Furthermore also the Test-Code.
- `cities.csv`: Includes the raw data.

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
- `name` (str): Name of the data.

### Methods

- `filter()`: returns a new table object with the filtered data, based on the lambda function /condition in the parameters
- `aggregate()`: aggregates the data based on the lambda function and the specific key in the parameters

## Running the Code

To run the simulation, execute `data_processing.py`:

```bash
python3 data_processing.py
```

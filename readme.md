# JSON File Manipulation

This Python script provides functionality to manipulate JSON files including reading, writing, updating, adding, and deleting data.

## Description

The script consists of several functions for various JSON file operations:
- `read_json(filename)`: Loads a JSON file and returns its content as a Python object.
- `write_to_json(filename, data)`: Writes data to a JSON file.
- `update_json(filename, index, key, value)`: Updates a specific key-value pair in the JSON file.
- `add_data(filename, new_data)`: Adds a new key-value pair to the JSON file.
- `delete_data(filename)`: Deletes a specified key from all objects in the JSON file.

Each function includes error handling to manage scenarios such as file not found and general exceptions.

## Usage

1. Clone the repository:
2. Either create your own .json file or use the same 
3. python json_crud.py:

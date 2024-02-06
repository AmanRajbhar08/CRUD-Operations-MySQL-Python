# CRUD Operations with MySQL and Python

This project demonstrates basic CRUD (Create, Read, Update, Delete) operations using MySQL database and Python.

## Setup

1. Install MySQL database server.
2. Create a database named `your_database`.
3. Execute the SQL script `create_table.sql` to create the 'Registration' table.
4. Install MySQL Connector/Python library: `pip install mysql-connector-python`.

## Running the Code

1. Open `crud_operations.py` script.
2. Replace `your_username`, `your_password`, and `your_database` with your MySQL credentials.
3. Run the Python script using Python interpreter (`python crud_operations.py`).

## Usage

- `create_record(name, email, dob)`: Creates a new registration record.
- `read_records()`: Retrieves all registration records from the database.
- `update_record(id, name, email, dob)`: Updates an existing registration record.
- `delete_record(id)`: Deletes a registration record by ID.

## Example

```python
# Example usage
create_record("Aman", "Aman@gmail.com", "1990-01-01")
read_records()
update_record(1, "Rahul", "Rahul@gmail.com.com", "1985-01-01")
delete_record(1)

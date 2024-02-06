import mysql.connector
from mysql.connector import errorcode

# Connect to MySQL
try:
    conn = mysql.connector.connect(
        host='localhost',
        user='your_username',
        password='your_password',
        database='your_database'
    )
    cursor = conn.cursor()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Access denied. Check your username and password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    else:
        print(err)

# Create a new record with input validation
def create_record(name, email, dob):
    if not name or not email or not dob:
        print("Error: Name, email, and date of birth are required.")
        return

    try:
        sql = "INSERT INTO Registration (Name, Email, DateOfBirth) VALUES (%s, %s, %s)"
        val = (name, email, dob)
        cursor.execute(sql, val)
        conn.commit()
        print("Record inserted successfully")
    except mysql.connector.Error as err:
        print("Error:", err)
        conn.rollback()

# Retrieve records
def read_records():
    try:
        sql = "SELECT * FROM Registration"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            print(row)
    except mysql.connector.Error as err:
        print("Error:", err)

# Update a record with input validation
def update_record(id, name, email, dob):
    if not name or not email or not dob:
        print("Error: Name, email, and date of birth are required.")
        return

    try:
        sql = "UPDATE Registration SET Name = %s, Email = %s, DateOfBirth = %s WHERE ID = %s"
        val = (name, email, dob, id)
        cursor.execute(sql, val)
        conn.commit()
        print("Record updated successfully")
    except mysql.connector.Error as err:
        print("Error:", err)
        conn.rollback()

# Delete a record with input validation
def delete_record(id):
    if not id:
        print("Error: ID is required.")
        return

    try:
        sql = "DELETE FROM Registration WHERE ID = %s"
        val = (id,)
        cursor.execute(sql, val)
        conn.commit()
        print("Record deleted successfully")
    except mysql.connector.Error as err:
        print("Error:", err)
        conn.rollback()

# Close the cursor and connection
def close_connection():
    cursor.close()
    conn.close()

# Example usage
if __name__ == "__main__":
    # Create a record
    create_record("AMAN", "Aman@gmail.com", "1990-01-01")

    # Read records
    read_records()

    # Update a record
    update_record(1, "Rahul", "Rahul@gmail.com", "1985-01-01")

    # Delete a record
    delete_record(1)

    # Close connection
    close_connection()

import mysql.connector

# Replace these values with your own MySQL server credentials
host = "localhost"
user = "root"
password = "12345"
database = "store"

# Data to be inserted into the inventory table
data_to_insert = [
    ("Rin", "D01", 50, 55, 88, "2024-03-12"),
    ("Vim", "D02", 8, 10, 83, "2024-03-05"),
    ("Dove", "S01", 150, 200, 28, "2025-01-01"),
    ("Sunslik", "S02", 150, 194, 28, "2025-01-01"),
    ("Lays", "F01", 16, 20, 190, "2024-04-01"),
    ("Doritos", "F02", 20, 25, 65, "2024-09-12"),
    ("Fortune", "O01", 145, 155, 39, "2024-10-06"),
    ("Dhara", "O02", 130, 143, 85, "2024-12-06"),
    ("Close Up", "T01", 45, 65, 99, "2026-03-12"),
    ("Dabur", "T02", 35, 50, 20, "2024-01-13"),
    ("Harpic", "C01", 90, 100, 21, "2024-01-13"),
    ("All Out", "R01", 40, 49, 40, "2024-01-13"),
    ("Comfort", "D03", 123, 140, 13, "2024-01-13"),

]

# Establish a connection to the MySQL server
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Loop through the data and insert into the inventory table
        for row in data_to_insert:
            insert_query = """
            INSERT INTO inventory (product_name, product_code, cost_price, selling_price, quantity, expiry_date)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, row)

        # Commit the changes
        connection.commit()
        print("Data inserted successfully.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")

import mysql.connector

# Replace these values with your own MySQL server credentials
host = "localhost"
user = "root"
password = "12345"
database = "store"

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

        # SQL query to create the inventory table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS inventory (
            product_id INT AUTO_INCREMENT PRIMARY KEY,
            product_name VARCHAR(255) NOT NULL,
            product_code VARCHAR(50) UNIQUE NOT NULL,
            cost_price DECIMAL(10, 2) NOT NULL,
            selling_price DECIMAL(10, 2) NOT NULL,
            quantity INT NOT NULL,
            expiry_date DATE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """

        # Execute the query
        cursor.execute(create_table_query)
        print("Table 'inventory' created successfully.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")

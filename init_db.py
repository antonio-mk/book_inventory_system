import sqlite3

# Function to initialize the database
def initialize_db():
    # Connect to the SQLite database (creates the file if it doesn't exist)
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()

    # Create the "Inventory" table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Inventory (
            entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT NOT NULL,
            Author TEXT NOT NULL,
            Genre TEXT NOT NULL,
            PublicationDate DATE NOT NULL,
            ISBN TEXT UNIQUE NOT NULL
        )
    ''')
    print("Database initialized and 'Inventory' table created (if it didn't exist).")

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Run the initialization function if the script is executed directly
if __name__ == "__main__":
    initialize_db()

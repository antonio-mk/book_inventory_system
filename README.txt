Prerequisites:

Ensure Python 3.x is installed on your system.
Also ensure flask is installed. (This is a step bellow)


Steps to Run the System

Download the Project Files
Copy the project folder to your system.
Ensure the folder structure is intact, with the following files and directories:
project/
├── app.py
├── init_db.py
├── books.db (created after database initialization)
├── frontend/
│ ├── index.html
│ ├── styles.css
│ └── scripts.js

Open a terminal or command prompt and type the bellow lines.

Navigate to the project folder:
cd path_to_project_folder

Install the required library:
pip install flask

Run the database initialization script:
python init_db.py

You should see a message:
Database initialized and 'Inventory' table created (if it didn't exist).

Run the Flask application:
python app.py

The terminal will display something like:

"Running on http://127.0.0.1:5000 (Press CTRL+C to quit)"
Keep this terminal open while the application is running.

Open the Application in a Browser

Open your web browser.

Navigate to:
http://127.0.0.1:5000

How to Use the System

Adding a Book:

Fill in the form with the following details:
Title
Author
Genre
Publication Date (format: YYYY-MM-DD)
ISBN (13 characters)
Click Add Book. You will see a confirmation message if the book is added successfully.

Filtering Books:

Use the search bar to filter books by title, author, genre, or publication date.
Click Filter to view the results.

Exporting Data:

Click Export JSON to download the data as a JSON file.

Stopping the Server:

In the terminal where the server is running, press CTRL+C to stop it.
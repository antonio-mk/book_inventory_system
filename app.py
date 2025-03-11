from flask import Flask, request, jsonify, send_from_directory, Response
import sqlite3
import os
import json

app = Flask(__name__)

# Set the folder where the frontend files are stored
FRONTEND_FOLDER = os.path.join(os.getcwd(), "frontend")


# Serve the index.html
@app.route("/")
def serve_index():
    return send_from_directory(FRONTEND_FOLDER, "index.html")


# Serve static files (CSS, JS)
@app.route("/<path:filename>")
def serve_static_files(filename):
    return send_from_directory(FRONTEND_FOLDER, filename)


# Add Book Route
@app.route("/add", methods=["POST"])
def add_book():
    try:
        # Parse JSON input from the frontend
        data = request.json
        title = data.get("title")
        author = data.get("author")
        genre = data.get("genre")
        publication_date = data.get("publication_date")
        isbn = data.get("isbn")

        # Validate input data
        if not all([title, author, genre, publication_date, isbn]):
            return jsonify({"success": False, "message": "All fields are required."}), 400

        # Insert data into the database
        conn = sqlite3.connect("books.db")
        cursor = conn.cursor()
        query = """
        INSERT INTO Inventory (Title, Author, Genre, PublicationDate, ISBN)
        VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(query, (title, author, genre, publication_date, isbn))
        conn.commit()
        conn.close()

        return jsonify({"success": True, "message": "Book added successfully!"})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"success": False, "message": str(e)}), 500


# Get Books Route (Filter and Fetch)
@app.route("/books", methods=["GET"])
def get_books():
    try:
        filters = {
            "title": request.args.get("title"),
            "author": request.args.get("author"),
            "genre": request.args.get("genre"),
            "publication_date": request.args.get("publication_date")
        }

        # Build the SQL query dynamically based on filters
        query = "SELECT Title, Author, Genre, PublicationDate, ISBN FROM Inventory WHERE 1=1"
        params = []

        for column, value in filters.items():
            if value:
                query += f" AND {column.capitalize()} LIKE ?"
                params.append(f"%{value}%")

        conn = sqlite3.connect("books.db")
        cursor = conn.cursor()
        cursor.execute(query, params)
        books = cursor.fetchall()
        conn.close()

        # Format results as a list of dictionaries
        books_list = [
            {
                "title": book[0],
                "author": book[1],
                "genre": book[2],
                "publication_date": book[3],
                "isbn": book[4]
            }
            for book in books
        ]
        return jsonify(books_list)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"success": False, "message": str(e)}), 500


# Export books as JSON
@app.route("/export", methods=["GET"])
def export_books():
    try:
        conn = sqlite3.connect("books.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Inventory")
        books = cursor.fetchall()
        conn.close()

        books_list = [
            {
                "entry_id": book[0],
                "title": book[1],
                "author": book[2],
                "genre": book[3],
                "publication_date": book[4],
                "isbn": book[5]
            }
            for book in books
        ]

        json_data = json.dumps(books_list, indent=4)
        return Response(
            json_data,
            mimetype="application/json",
            headers={"Content-Disposition": "attachment;filename=books.json"}
        )
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"success": False, "message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)

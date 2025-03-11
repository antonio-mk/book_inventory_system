# 📚 Book Inventory Management System  

## 📖 Overview  
This is a simple inventory management system for books. It allows users to add new books, filter existing books, and export book data. The project is built using Flask for the backend and a simple HTML, CSS, and JavaScript frontend.  

## ✨ Features  
- ✅ Add new books to the inventory  
- 🔍 Filter books by title, author, genre, and publication date  
- 📤 Export book data in JSON format  
- 🖥️ Simple and user-friendly web interface  

## 🛠️ Prerequisites  
Ensure you have:  
- 🐍 Python 3.x installed on your system  
- 🚀 Flask installed (this is covered in the steps below)  

## 📂 Project Structure  
```
project/
├── app.py
├── init_db.py
├── books.db (created after database initialization)
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── scripts.js
```

## 📥 Installation  

1️⃣ **Clone the repository:**  
   ```sh
   git clone https://github.com/yourusername/book-inventory.git
   cd book-inventory
   ```

2️⃣ **(Optional) Create a virtual environment and activate it:**  
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3️⃣ **Install dependencies:**  
   ```sh
   pip install -r requirements.txt
   ```

4️⃣ **Initialize the database:**  
   ```sh
   python init_db.py
   ```
   You should see a message:  
   _"Database initialized and 'Inventory' table created (if it didn't exist)."_  

## 🚀 Running the Project  

### 🖥️ Backend (Flask Server)  
Run the backend using:  
```sh
python app.py
```
The terminal will display something like:  
```
Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```
Keep this terminal open while the application is running.  

### 🌍 Open the Application in a Browser  
1️⃣ Open your web browser.  
2️⃣ Navigate to:  
   ```
   http://127.0.0.1:5000
   ```
   
### 🏠 Frontend Options  
1️⃣ Open `frontend/index.html` manually in a browser, or  
2️⃣ Serve the frontend using Python’s built-in HTTP server:  
   ```sh
   cd frontend
   python -m http.server 8000
   ```
   Then, open `http://127.0.0.1:8000` in your browser.  

---

## 📌 How to Use the System  

### ➕ Adding a Book  
1️⃣ Fill in the form with the following details:  
   - 📖 **Title**  
   - ✍️ **Author**  
   - 📚 **Genre**  
   - 📅 **Publication Date** (format: YYYY-MM-DD)  
   - 🔢 **ISBN** (13 characters)  
2️⃣ Click **Add Book**  
3️⃣ You will see a confirmation message if the book is added successfully.  

### 🔍 Filtering Books  
- Use the search bar to filter books by title, author, genre, or publication date.  
- Click **Filter** to view the results.  

### 📤 Exporting Data  
- Click **Export JSON** to download the data as a JSON file.  

### ⏹️ Stopping the Server  
In the terminal where the server is running, press **CTRL+C** to stop it.  

---

## 🌐 API Endpoints  

### ➕ Add a Book  
**Endpoint:** `POST /add`  
**Request Body (JSON):**  
```json
{
    "title": "Example Book",
    "author": "John Doe",
    "genre": "Fiction",
    "publication_date": "2023-01-01",
    "isbn": "1234567890123"
}
```
**Response:**  
```json
{"success": true, "message": "Book added successfully!"}
```

### 🔍 Filter Books  
**Endpoint:** `GET /filter`  
**Query Parameters:**  
- `title` (optional)  
- `author` (optional)  
- `genre` (optional)  
- `publication_date` (optional)  

**Example Request:**  
```
GET /filter?author=John%20Doe
```
**Response:**  
```json
[{
    "entry_id": 1,
    "title": "Example Book",
    "author": "John Doe",
    "genre": "Fiction",
    "publication_date": "2023-01-01",
    "isbn": "1234567890123"
}]
```

### 📤 Export Books (JSON)  
**Endpoint:** `GET /export`  
**Response:**  
```json
{
    "books": [
        {
            "entry_id": 1,
            "title": "Example Book",
            "author": "John Doe",
            "genre": "Fiction",
            "publication_date": "2023-01-01",
            "isbn": "1234567890123"
        }
    ]
}
```

---

## ❗ Troubleshooting  
### 🔒 Database is Locked  
If you encounter a `"database is locked"` error:  
1️⃣ Ensure no other process is accessing `books.db`.  
2️⃣ Close any running instances.  
3️⃣ Restart the Flask server.  

---

## 📝 License  
This project is licensed under the MIT License.  

## 🛠️ Issues & Support  
If you encounter any issues or have suggestions, please open an issue in the GitHub repository.  

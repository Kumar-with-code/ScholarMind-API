# ScholarMind API 🎓

A robust, modular RESTful Student Management API built with **FastAPI**, **SQLAlchemy ORM**, and **Pydantic v2** featuring full CRUD functionality, database persistence, and automated Swagger/OpenAPI documentation.

---

## 🚀 Features

- **Full CRUD Operations**: Create, Read (all & by ID with pagination), Update, and Delete student records.
- **Data Validation & Serialization**: Strict schema enforcement using **Pydantic v2**.
- **ORM & Database Support**: Powered by **SQLAlchemy** (configured for SQLite by default, easily adaptable to PostgreSQL or MySQL).
- **Modular Project Architecture**: Separate route modules, models, schemas, and configurations for high scalability.
- **Automatic API Documentation**: Interactive Swagger UI (`/docs`) and ReDoc (`/redoc`).
- **Environment Management**: Configuration powered by `pydantic-settings` and `python-dotenv`.

---

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **ASGI Server**: [Uvicorn](https://www.uvicorn.org/)
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
- **Validation**: [Pydantic v2](https://docs.pydantic.dev/)
- **Database**: SQLite (default)
- **Settings Management**: Pydantic Settings & Python Dotenv

---

## 📁 Project Structure

```text
ScholarMind-API/
├── app/
│   ├── routes/
│   │   ├── base.py              # Aggregates all route modules into api_router
│   │   ├── create_student.py    # POST /students
│   │   ├── get_student.py       # GET /students & GET /students/{id}
│   │   ├── update_student.py    # PUT /students/{id}
│   │   └── delete_student.py    # DELETE /students/{id}
│   ├── config.py                # Environment configuration & settings
│   ├── database.py              # Database engine, SessionLocal, and dependency
│   ├── model_db_schema.py       # SQLAlchemy Student database model
│   └── schema.py                # Pydantic schemas (Create, Update, Response)
├── .env                         # Local environment variables (ignored by git)
├── .env.example                 # Environment variables template
├── .gitignore                   # Git ignore patterns
├── main.py                      # Application entrypoint & root router
├── README.md                    # Project documentation
└── requirements.txt             # Python package dependencies
```

---

## 🗄️ Data Model

### Student Table (`students`)

| Column | Type | Constraints / Description |
| :--- | :--- | :--- |
| `id` | Integer | Primary Key, Auto-increment, Indexed |
| `student_name` | String | Student's full name (Indexed, Required) |
| `student_class` | String | Grade or Class (Required) |
| `student_section` | String | Section (Required) |
| `student_dob` | Date | Date of Birth (`YYYY-MM-DD`, Required) |
| `created_at` | DateTime | Timestamp when record was created |
| `updated_at` | DateTime | Timestamp when record was last updated |

---

## ⚙️ Installation & Setup

### 1. Prerequisites
- **Python 3.10+**
- **Git**

### 2. Clone the Repository
```bash
git clone https://github.com/Kumar-with-code/ScholarMind-API.git
cd ScholarMind-API
```

### 3. Create and Activate a Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv ewb
.\ewb\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv ewb
source ewb/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables
Copy the `.env.example` file to `.env`:
```bash
cp .env.example .env
```
*(On Windows PowerShell, use `Copy-Item .env.example .env`)*

By default, `.env` contains:
```env
DATABASE_URL=sqlite:///./students.db
```

---

## 🏃 Running the Application

Start the development server with live reload:
```bash
uvicorn main:app --reload
```

The server will be running at:
- **API Base URL**: `http://127.0.0.1:8000`
- **Interactive Swagger Documentation**: `http://127.0.0.1:8000/docs`
- **ReDoc Documentation**: `http://127.0.0.1:8000/redoc`

---

## 📖 API Endpoints Reference

| Method | Endpoint | Description | Status Code |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Root endpoint / API health check | `200 OK` |
| `POST` | `/students` | Create a new student | `201 Created` |
| `GET` | `/students/?skip=0&limit=100` | Fetch list of students with pagination | `200 OK` |
| `GET` | `/students/{student_id}` | Fetch a single student by ID | `200 OK` / `404 Not Found` |
| `PUT` | `/students/{student_id}` | Update an existing student | `200 OK` / `404 Not Found` |
| `DELETE` | `/students/{student_id}` | Delete a student by ID | `200 OK` / `404 Not Found` |

---

## 💡 Request & Response Examples

### 1. Create a Student (`POST /students`)
**Request Body:**
```json
{
  "student_name": "John Doe",
  "student_class": "10",
  "student_section": "A",
  "student_dob": "2008-05-15"
}
```

**Response (`201 Created`):**
```json
{
  "student_name": "John Doe",
  "student_class": "10",
  "student_section": "A",
  "student_dob": "2008-05-15",
  "id": 1,
  "created_at": "2026-10-14T14:15:30.123456",
  "updated_at": "2026-10-14T14:15:30.123456"
}
```

### 2. Update a Student (`PUT /students/{student_id}`)
You can update all or only specific fields.

**Request Body:**
```json
{
  "student_class": "11",
  "student_section": "B"
}
```

**Response (`200 OK`):**
```json
{
  "student_name": "John Doe",
  "student_class": "11",
  "student_section": "B",
  "student_dob": "2008-05-15",
  "id": 1,
  "created_at": "2026-10-14T14:15:30.123456",
  "updated_at": "2026-10-14T14:20:00.654321"
}
```

### 3. Delete a Student (`DELETE /students/{student_id}`)
**Response (`200 OK`):**
```json
{
  "message": "Student deleted successfully"
}
```

---

## 📤 Pushing to Your GitHub / Remote Repository

Follow these steps in your terminal to initialize and push your code:

```bash
# 1. Check git status to ensure only project source files are staged
git status

# 2. Add all relevant project files
git add .

# 3. Create your initial commit
git commit -m "feat: initial commit with student management API and documentation"

# 4. Set the main branch (recommended)
git branch -M main

# 5. Link your remote repository
git remote add origin https://github.com/Kumar-with-code/ScholarMind-API.git

# 6. Push code to your remote repository
git push -u origin main
```

---

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).

![Tests](https://github.com/ricardocanela/qventus-parts/actions/workflows/tests.yml/badge.svg)

# ⚙️ Parts API

A fully Dockerized Django RESTful API for managing parts inventory and analyzing the most common words used in part descriptions.

---

## 📦 Features

- ✅ Full CRUD for `Part` model  
- 📊 Analytics endpoint: retrieves the top 5 most common words from all part descriptions  
- 🧪 Automated testing using `pytest` and `pytest-django`  
- 🐳 Docker & Docker Compose for easy setup  

---

## 🚀 Getting Started

### 🐳 Run with Docker

```bash
git clone <your-repo-url>
cd parts_api
docker-compose up --build
```

The API will be available at: [http://localhost:8000/api/](http://localhost:8000/api/)

---

## 🔍 API Endpoints

### 🔹 List all parts  
`GET /api/parts/`

---

### 🔹 Create a new part  
`POST /api/parts/`

```json
{
  "name": "Aviation Motor A1",
  "sku": "MT-A1",
  "description": "High-performance motor for light aircraft",
  "weight_ounces": 450,
  "is_active": true
}
```

---

### 🔹 Retrieve part details  
`GET /api/parts/<id>/`

---

### 🔹 Update a part  
`PUT /api/parts/<id>/`

---

### 🔹 Delete a part  
`DELETE /api/parts/<id>/`

---

### 🔹 Top 5 Most Common Words  
`GET /api/common-words/`

**Example Response:**

```json
{
  "testing": 2,
  "part": 2,
  "for": 2,
  "used": 1,
  "only": 1
}
```

---

## 🧪 Running Tests

```bash
docker-compose exec web pytest --cov
```

**Tests cover:**

- All CRUD operations  
- Validation checks  
- Analytics endpoint  
- Model string representation  

---

## 🛠️ Database Configuration

PostgreSQL is used by default (via Docker).  
If needed, switch to SQLite by editing `src/parts_api/settings/base.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

---

## ⚙️ Environment Variables

Example `.env` file:

```env
export PYTHONPATH=src
```

---

## 📈 Future Improvements

- 🔐 Authentication and permission controls (e.g., JWT)  
- 🔎 Filtering, search, and ordering on part listing  
- 📑 Pagination support  
- 📊 Admin dashboard for metrics  
- 🧾 Swagger or ReDoc integration for auto-documentation  

---

## 👨‍💻 Author

**Ricardo Canela**  
Backend Engineer · Python · Django · REST APIs · Docker  
[LinkedIn](https://www.linkedin.com/in/ricardo-lima-canela/) · [GitHub](https://github.com/ricardocanela)

---

## 📄 License

MIT License © 2025 Ricardo Canela

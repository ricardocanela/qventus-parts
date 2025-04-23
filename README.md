![CI](https://github.com/ricardocanela/qventus-parts/actions/workflows/tests.yml/badge.svg)

# ⚙️ Parts API

A fully Dockerized Django RESTful API for managing a parts inventory and analyzing the most common words used in part descriptions.

> 🧪 This project uses **GitHub Actions** to automatically run tests on every push and pull request to the `main` branch.

---

## 📦 Features

- ✅ Full CRUD for the `Part` model  
- 📊 Analytics endpoint: retrieves the top 5 most common words across all part descriptions  
- 🧪 Automated tests with `pytest` and `pytest-django`  
- 🐳 Docker & Docker Compose for simplified local setup  

---

## 🚀 Getting Started

### 🐳 Run with Docker and docker-compose

```bash
git clone <this-repo-url>
cd qventus-parts
docker-compose up --build
```

Once started, the API will be available at: [http://localhost:8000/api/](http://localhost:8000/api/)

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

### 🔹 Get Top 5 Most Common Words  
`GET /api/common-words/`

**Example Response:**

```json
{
  "motor": 3,
  "high": 2,
  "performance": 2,
  "aircraft": 2,
  "light": 1
}
```

---

## 🧪 Running Tests

Run tests inside the container:

```bash
docker-compose exec web pytest --cov
```

**Test coverage includes:**

- CRUD operations  
- Validation checks  
- Analytics endpoint (`/api/common-words/`)  
- Model string representation  

> Tests are powered by `pytest` + `pytest-django`, with database fixtures and test isolation.

---

## 🛠️ Database Configuration

The project uses **PostgreSQL by default**, managed through Docker Compose.  

---

### 🧪 Sample Data Seeding

When you run the project with Docker, the application automatically checks if the `parts` table is empty and inserts **sample data** if needed.

This ensures the API has meaningful data available for testing and exploration right after startup.

No manual steps required.

> ✅ The seed script is executed via `python manage.py shell < src/seed_data.py` during container initialization (see `entrypoint.sh`).

The inserted sample records are:

| Name           | SKU             | Description                                 | Weight (oz) | Active |
|----------------|------------------|---------------------------------------------|-------------|--------|
| Heavy coil     | SDJDDH8223DHJ    | Tightly wound nickel-gravy alloy spring     | 22          | ✅     |
| Reverse lever  | DCMM39823DSJD    | Attached to provide inverse leverage        | 9           | ❌     |
| Macrochip      | OWDD823011DJSD   | Used for heavy-load computing               | 2           | ✅     |




## 📈 Future Improvements

- 🔐 JWT Authentication and permission controls  
- 🔎 Filtering, search, and ordering on part listings  
- 📑 Pagination support  
- 📊 Admin dashboard for analytics  
- 🧾 API documentation via Swagger or ReDoc  

---

## 👨‍💻 Author

**Ricardo Canela**  
Backend Engineer · Python · Django · REST APIs · Docker  
[LinkedIn](https://www.linkedin.com/in/ricardo-lima-canela/) · [GitHub](https://github.com/ricardocanela)

---

## 📄 License

MIT License © 2025 Ricardo Canela


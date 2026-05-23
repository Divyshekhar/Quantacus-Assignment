# Product Intelligence Dashboard API

Backend service for an ecommerce seller intelligence platform built using **FastAPI**, **SQLModel**, and **PostgreSQL**.

This project helps sellers analyze product listings, validate listing quality, compare competitor prices, and generate actionable alerts.

---

# Features

- Product CSV Upload
- Product Video Upload (Mocked Extraction)
- Product Validation Engine
- Product Quality Dashboard
- Competitor Price Comparison
- Alerts System
- Job Tracking APIs
- Enhanced Product Title Suggestions
- Swagger/OpenAPI Documentation

---

# Tech Stack

- FastAPI
- SQLModel
- PostgreSQL
- Pandas
- Uvicorn
- Python 3.12+
- uv

---

# Project Structure

```text
backend/
│
├── app/
│   ├── core/
│   ├── db/
│   ├── jobs/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   ├── services/
│   ├── uploads/
│   ├── utils/
│   ├── validators/
│   └── main.py
│
├── .env
├── pyproject.toml
├── uv.lock
└── README.md
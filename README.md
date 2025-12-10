# Fiindo Recruitment Challenge

This is my solution for the Fiindo backend challenge.

The task was to build a small Python application that connects to the Fiindo API, processes stock and financial data, performs some calculations, and stores the results in a SQLite database.

---

## What the app does

- Fetches financial data from the Fiindo API  
- Filters companies by industry  
- Calculates:
  - PE ratio (price to earnings)
  - Revenue growth (quarter over quarter)
  - Net income (trailing twelve months)
  - Debt ratio (debt to equity)
- Groups everything by industry and calculates averages/sums  
- Saves everything into a local SQLite database (`fiindo_challenge.db`)

---

## Technologies used

- Python 3.11  
- SQLAlchemy (ORM for SQLite)  
- Requests (HTTP client for API)  
- Alembic (optional, for migrations)  
- Docker (for containerization)

---

## API info

- Base URL: `https://api.test.fiindo.com`
- Docs: [https://api.test.fiindo.com/api/v1/docs/](https://api.test.fiindo.com/api/v1/docs/)
- Authentication:  
  ```
  Authorization: Bearer barzan.sindi
  ```
- Only these industries are processed:
  - Banks - Diversified  
  - Software - Application  
  - Consumer Electronics

---

## Database structure

**ticker_statistics**
| Column | Type | Description |
|--------|------|-------------|
| symbol | String | Stock symbol |
| industry | String | Industry name |
| pe_ratio | Float | Price to earnings |
| revenue_growth | Float | QoQ revenue growth |
| net_income_ttm | Float | TTM net income |
| debt_ratio | Float | Debt to equity |

**industry_aggregations**
| Column | Type | Description |
|--------|------|-------------|
| industry | String | Industry name |
| avg_pe_ratio | Float | Average PE ratio |
| avg_revenue_growth | Float | Average revenue growth |
| total_revenue | Float | Total revenue per industry |

---

## Project structure

```
fiindo-recruitment-challange/
│
├── src/
│   ├── api_client.py
│   ├── processing.py
│   ├── db.py
│   ├── models.py
│   ├── main.py
│   └── fiindo_challenge.db
│
├── alembic/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## How to run it

### Local setup

Clone the repo:
```bash
git clone https://github.com/bsindi/fiindo-recruitment-challange.git
cd fiindo-recruitment-challange
```

Create a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the script:
```bash
python src/main.py
```

The database file `fiindo_challenge.db` will be created automatically.

---

### Run with Docker (optional)

Build the image:
```bash
docker-compose build
```

Run the container:
```bash
docker-compose up
```

It will automatically execute the app and create the SQLite database inside the container.

---

## Optional / Bonus

- Docker setup included  
- Basic structure ready for unit testing  
- Alembic migrations can be added later if needed  

---

**Author:** Barzan Sindi  
GitHub: [bsindi](https://github.com/bsindi)

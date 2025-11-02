# Azure SQL Demo (Flask)

This minimal Flask app exposes a `/products` endpoint backed by Azure SQL Database.

## Prerequisites
- Python 3.9+
- ODBC Driver 18 for SQL Server installed
- Network access to your Azure SQL server

## Setup
1. Create and populate a `products` table (adjust columns as needed):
   ```sql
   CREATE TABLE products (
     id INT PRIMARY KEY,
     name NVARCHAR(100) NOT NULL,
     price DECIMAL(10,2) NULL
   );
   ```
2. Copy `.env.example` to `.env` and set values.
3. Create a virtual environment and install deps:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r flask-app/requirements.txt
   ```
4. Run the app:
   ```bash
   python flask-app/app.py
   ```

Open http://localhost:5000/products

Note: On macOS, install the ODBC driver via Homebrew and accept the EULA.
from flask import Flask, jsonify
import os
import pyodbc


def get_connection():
    """Build and return a pyodbc connection using env vars.

    Env variables supported:
      - AZURE_SQL_CONNECTION_STRING (full ODBC string)
      - AZURE_SQL_SERVER, AZURE_SQL_DATABASE, AZURE_SQL_USERNAME, AZURE_SQL_PASSWORD
      - AZURE_SQL_DRIVER (default: {ODBC Driver 18 for SQL Server})
      - AZURE_SQL_ENCRYPT (default: yes)
      - AZURE_SQL_TRUST_SERVER_CERT (default: no)
    """
    conn_str = os.getenv("AZURE_SQL_CONNECTION_STRING")
    if not conn_str:
        server = os.getenv("AZURE_SQL_SERVER")
        database = os.getenv("AZURE_SQL_DATABASE")
        username = os.getenv("AZURE_SQL_USERNAME")
        password = os.getenv("AZURE_SQL_PASSWORD")
        if not all([server, database, username, password]):
            raise ValueError(
                "Missing required env vars. Set AZURE_SQL_CONNECTION_STRING or "
                "AZURE_SQL_SERVER/AZURE_SQL_DATABASE/AZURE_SQL_USERNAME/AZURE_SQL_PASSWORD"
            )
        driver = os.getenv("AZURE_SQL_DRIVER", "{ODBC Driver 18 for SQL Server}")
        encrypt = os.getenv("AZURE_SQL_ENCRYPT", "yes")
        trust_server_cert = os.getenv("AZURE_SQL_TRUST_SERVER_CERT", "no")
        conn_str = (
            f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};"
            f"Encrypt={encrypt};TrustServerCertificate={trust_server_cert}"
        )
    return pyodbc.connect(conn_str)


app = Flask(__name__)


@app.route("/products")
def products():
    # NOTE: Adjust the SELECT to match your schema; using TOP 10 for safe response size
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT TOP 10 id, name, price FROM products")
        rows = cursor.fetchall()
        return jsonify(
            [
                {
                    "id": r[0],
                    "name": r[1],
                    "price": float(r[2]) if r[2] is not None else None,
                }
                for r in rows
            ]
        )


@app.get("/")
def root():
    return {"status": "ok", "endpoints": ["/products"]}


if __name__ == "__main__":
    app.run(port=int(os.getenv("PORT", "5000")), host="0.0.0.0")

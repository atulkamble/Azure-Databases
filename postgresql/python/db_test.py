import os
import psycopg2


def main():
    conn = psycopg2.connect(
        dbname=os.getenv("PGDATABASE", "analyticsdb"),
        user=os.getenv("PGUSER", "pgadmin"),
        password=os.getenv("PGPASSWORD", "ChangeMe123!"),
        host=os.getenv("PGHOST", "pgsql-demo.postgres.database.azure.com"),
        port=os.getenv("PGPORT", "5432"),
        sslmode=os.getenv("PGSSLMODE", "require"),
    )
    cur = conn.cursor()
    cur.execute("SELECT version();")
    print(cur.fetchone())
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()

# 📘 **Azure Database Services – Theory, Projects, & Interview Notes (Full Practical Guide)**

This version adds **important Azure interview points**, **practical theory**, **real-world use cases**, and **sample mini projects** with CLI/Terraform — ideal for both **learning and interview prep**.

---

# ☁️ **Azure Database Services – Complete Hands-On + Interview Guide**

---

## 🧩 **1️⃣ Understanding Database as a Service (DBaaS)**

### 🧠 **Theory Points to Remember**

* DBaaS = Fully managed cloud-based database delivery model.
* Removes the need for infrastructure management (patching, scaling, HA, DR handled by Azure).
* You focus only on **data, schema, and query optimization**.
* Azure offers both **PaaS and IaaS database options**.

### 💬 **Interview Points**

| Question                             | Key Answer                                                                        |
| ------------------------------------ | --------------------------------------------------------------------------------- |
| What is DBaaS?                       | Cloud-managed database where provider handles maintenance, scaling, and security. |
| Difference between IaaS vs PaaS DB?  | IaaS = full control (SQL VM), PaaS = managed service (Azure SQL DB).              |
| How does Azure handle backups?       | Automatic backups (7–35 days), Point-in-Time Restore (PITR).                      |
| Can you scale Azure DBs dynamically? | Yes, via vCore or DTU models and Elastic Pools.                                   |

---

## 🟦 **2️⃣ Azure SQL Database (PaaS)**

### 🧠 **Theory**

* Fully managed relational DB engine (latest SQL features).
* Best for SaaS/web applications.
* Built-in **HA**, **geo-replication**, **point-in-time restore**, and **auto-tuning**.
* Models: **DTU** (Basic, Standard, Premium) or **vCore** (GP, BC, Hyperscale).
* Encryption: **TDE enabled by default**.

### 🎯 **Use Case:** Inventory Management App (Flask + Azure SQL)

#### 💻 **Python Mini Project**

```python
from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)
conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER=sqlsrv-demo.database.windows.net;DATABASE=sqldb-demo;UID=adminuser;PWD=Password123!')

@app.route('/products')
def products():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    return jsonify([{'id': r[0], 'name': r[1], 'price': r[2]} for r in rows])

if __name__ == '__main__':
    app.run(port=5000)
```

#### 🧠 **Interview Points**

| Question                                              | Key Answer                                                           |
| ----------------------------------------------------- | -------------------------------------------------------------------- |
| What is Azure SQL Database?                           | A PaaS offering that provides fully managed SQL Server capabilities. |
| Difference between Azure SQL DB and SQL Server on VM? | SQL on VM = IaaS (you manage), Azure SQL = PaaS (Azure manages).     |
| What is DTU vs vCore?                                 | DTU = bundled performance (CPU+IO+Memory), vCore = separate control. |
| What is Elastic Pool?                                 | Shared resource pool for multiple DBs with variable workloads.       |
| How is HA achieved?                                   | Built-in 3 replicas across Availability Zones.                       |

---

## 🟩 **3️⃣ Azure Database for MySQL**

### 🧠 **Theory**

* Managed MySQL 5.7/8.0 service with automatic patching, backups, and HA.
* Flexible Server model offers **zone redundancy** and **private endpoints**.
* Storage auto-grow enabled by default.
* SSL enforced.

### 🎯 **Use Case:** WordPress Blog with Azure MySQL

#### ⚙️ **Config Snippet (wp-config.php)**

```php
define('DB_NAME','wordpressdb');
define('DB_USER','mysqladmin');
define('DB_PASSWORD','Password123!');
define('DB_HOST','mysql-demo.mysql.database.azure.com');
```

#### 💬 **Interview Points**

| Question                                                          | Key Answer                                                    |
| ----------------------------------------------------------------- | ------------------------------------------------------------- |
| What is Azure Database for MySQL?                                 | PaaS version of MySQL, managed by Azure.                      |
| What is the difference between Single Server and Flexible Server? | Flexible = more control, HA, zone redundancy, private access. |
| How do you connect securely?                                      | Via SSL or Private Endpoint.                                  |
| How does scaling work?                                            | Manual or auto-scale storage; compute tier selectable.        |

---

## 🟧 **4️⃣ Azure Database for PostgreSQL**

### 🧠 **Theory**

* Open-source, fully managed PostgreSQL 11–16 engine.
* Supports JSON, time-series, analytics workloads.
* **Flexible Server** = high availability + private VNet access.
* Supports **logical replication** for analytics.

### 🎯 **Use Case:** Analytics Web App (Django + PostgreSQL) 

[Code](https://github.com/atulkamble/flask-azure-sql-inventory-app#)

#### ⚙️ **Django Config**

```python
DATABASES = {
 'default': {
  'ENGINE': 'django.db.backends.postgresql',
  'NAME': 'analyticsdb',
  'USER': 'pgadmin',
  'PASSWORD': 'Password123!',
  'HOST': 'pgsql-demo.postgres.database.azure.com',
  'PORT': '5432',
  'OPTIONS': {'sslmode': 'require'}
 }}
```

#### 💬 **Interview Points**

| Question                                                | Key Answer                                                              |
| ------------------------------------------------------- | ----------------------------------------------------------------------- |
| Why use PostgreSQL in Azure?                            | Open-source, flexible schema, JSON support.                             |
| What’s the difference between Single & Flexible Server? | Flexible Server offers more control, VNet integration, zone redundancy. |
| How do you monitor performance?                         | Azure Monitor, Query Performance Insight, pg_stat_activity.             |

---

## 🟣 **5️⃣ Azure Cosmos DB (NoSQL)**

### 🧠 **Theory**

* Globally distributed, multi-model NoSQL DB.
* APIs: SQL, MongoDB, Cassandra, Table, Gremlin.
* **Five consistency levels**: Strong → Eventual.
* Auto-scale throughput (RU/s).
* Global replication within minutes.

### 🎯 **Use Case:** IoT Sensor Data Storage

#### 💻 **Node.js Example**

```javascript
const { MongoClient } = require("mongodb");
const uri = "mongodb://cosmos-demo.mongo.cosmos.azure.com:10255/?ssl=true";
const client = new MongoClient(uri,{auth:{username:"atul",password:"Password123!"}});
(async()=>{
 await client.connect();
 const db = client.db("iotdb");
 await db.collection("readings").insertOne({device:"sensor-001",temp:26});
 console.log(await db.collection("readings").find().toArray());
 client.close();
})();
```

#### 💬 **Interview Points**

| Question                           | Key Answer                                                       |
| ---------------------------------- | ---------------------------------------------------------------- |
| What is Cosmos DB?                 | A globally distributed multi-model database.                     |
| What are RUs?                      | Request Units — measure of throughput.                           |
| What are consistency levels?       | Strong, Bounded Staleness, Session, Consistent Prefix, Eventual. |
| How is global replication handled? | Multi-region writes + automatic failover.                        |

---

## 🔴 **6️⃣ Azure Cache for Redis**

### 🧠 **Theory**

* In-memory key-value cache.
* Used for **session storage**, **leaderboards**, **real-time apps**.
* Supports SSL, clustering, and persistence.
* SKUs: Basic, Standard, Premium, Enterprise.

### 🎯 **Use Case:** Session Cache for Login App

#### 💻 **Python Example**

```python
import redis
r = redis.StrictRedis(host='redis-demo.redis.cache.windows.net',port=6380,password='Password123!',ssl=True)
r.set('session:user123','active')
print(r.get('session:user123'))
```

#### 💬 **Interview Points**

| Question                  | Key Answer                                            |
| ------------------------- | ----------------------------------------------------- |
| Why use Redis?            | To cache frequently accessed data and reduce latency. |
| What is TTL?              | Time To Live for cached keys.                         |
| Is Redis persistent?      | Yes (AOF/RDB in Premium tier).                        |
| What port does Redis use? | 6379 (SSL = 6380).                                    |

---

## 🟠 **7️⃣ Azure Synapse Analytics (DW)**

### 🧠 **Theory**

* Combines SQL DW + Big Data analytics.
* MPP (Massive Parallel Processing) for large datasets.
* Integrated with **ADF**, **Data Lake**, **Power BI**.
* Can pause/resume compute to save cost.

### 🎯 **Use Case:** Sales Data Aggregation Warehouse

#### 💻 **SQL Example**

```sql
SELECT product, SUM(amount) AS total_sales
FROM sales_data
GROUP BY product
ORDER BY total_sales DESC;
```

#### 💬 **Interview Points**

| Question                                                      | Key Answer                                              |
| ------------------------------------------------------------- | ------------------------------------------------------- |
| What is Synapse?                                              | Azure’s data warehouse and analytics platform.          |
| How does MPP work?                                            | Distributes queries across multiple compute nodes.      |
| What’s the difference between Dedicated and Serverless pools? | Dedicated = reserved compute, Serverless = on-demand.   |
| How do you optimize performance?                              | Use partitioning, materialized views, resource classes. |

---

## 🟩 **8️⃣ Azure SQL Managed Instance (MI)**

### 🧠 **Theory**

* Hybrid: between PaaS and IaaS.
* Full SQL Server compatibility (Agent, SSIS, linked servers).
* VNet integration only (private IP).
* Best for **lift-and-shift migrations**.

### 🎯 **Use Case:** ERP Database Migration

#### 💻 **Linked Server Example**

```sql
EXEC sp_addlinkedserver @server='LegacyERP', @provider='SQLNCLI', @datasrc='onprem-erp.company.local';
```

#### 💬 **Interview Points**

| Question                                | Key Answer                                             |
| --------------------------------------- | ------------------------------------------------------ |
| Difference: Managed Instance vs SQL DB? | MI = full SQL engine, VNet access, supports SQL Agent. |
| Can we use cross-database queries?      | Yes, supported in MI.                                  |
| How is HA achieved?                     | AlwaysOn with automatic failover.                      |
| Can MI connect on-prem?                 | Yes, via VNet peering or ExpressRoute.                 |

---

## 🟦 **9️⃣ SQL Server on Azure VM (IaaS)**

### 🧠 **Theory**

* Complete control over OS and SQL Server.
* Used for legacy workloads requiring OS-level customization.
* Must handle patching, backups, and scaling manually.

### 🎯 **Use Case:** Legacy ERP Application Hosting

#### ⚙️ **PowerShell Example**

```powershell
New-AzVM -ResourceGroupName rg-database-demo -Name sqlvm-demo `
  -Location eastus -Image 'MicrosoftSQLServer:SQL2019-WS2019:Enterprise:latest' `
  -AdminUsername azureuser -AdminPassword 'Password123!'
```

#### 💬 **Interview Points**

| Question                             | Key Answer                                              |
| ------------------------------------ | ------------------------------------------------------- |
| Why use SQL VM instead of Azure SQL? | When full OS control or legacy integration is required. |
| How to automate backups?             | Enable SQL IaaS Agent extension.                        |
| How to achieve HA?                   | Use AlwaysOn AG or Failover Cluster.                    |

---

## 🧾 **🔟 Common Interview Concepts & Commands**

| Concept           | Interview Tip                                        |
| ----------------- | ---------------------------------------------------- |
| High Availability | Built-in for PaaS DBs, manual for IaaS               |
| Scaling           | Vertical (vCores), Horizontal (Read Replicas)        |
| Geo-Replication   | Used for DR and read replicas                        |
| Security          | Use Azure AD auth + Private Endpoint                 |
| Backup            | PITR (7–35 days), LTR (1–10 years)                   |
| Encryption        | TDE (at rest), SSL/TLS (in transit)                  |
| Monitoring        | Query Performance Insight, Azure Monitor             |
| Automation        | Terraform, ARM, Azure CLI                            |
| Cost Optimization | Pause compute, use Elastic Pools, Reserved Instances |
| Migration Tool    | Azure Database Migration Service (DMS)               |

---

## 🧹 **Cleanup Command**

```bash
az group delete --name rg-database-demo --yes --no-wait
```

---

## 🪜 **📊 Summary Table**

| Service          | Type      | Common Use Case | Key Features               | Interview Focus           |
| ---------------- | --------- | --------------- | -------------------------- | ------------------------- |
| Azure SQL DB     | PaaS      | Web Apps        | Auto backup, Elastic Pools | DTU vs vCore, HA          |
| Managed Instance | Hybrid    | ERP Migration   | SQL Agent, VNet            | On-prem migration         |
| SQL on VM        | IaaS      | Legacy Apps     | Full control               | HA setup, patching        |
| MySQL            | PaaS      | WordPress       | Open Source DB             | Single vs Flexible Server |
| PostgreSQL       | PaaS      | Analytics       | JSON, Logical Replication  | SSL, tuning               |
| Cosmos DB        | NoSQL     | IoT / Global    | RU/s, multi-region         | Consistency, API types    |
| Redis            | Cache     | Session Store   | In-memory                  | TTL, persistence          |
| Synapse          | Analytics | Data Warehouse  | MPP, BI                    | Serverless vs Dedicated   |

---

## 🚀 **Next Steps**

Would you like me to:

1. 📁 **Create GitHub repo structure** (`azure-database-lab/`) with folders for `/sql`, `/mysql`, `/cosmos`, `/redis` each having code, Terraform, and README?
2. 📘 Or export this as a **professional “Interview + Lab PDF document”** with logo placeholders, tables, and diagrams (for Cloudnautic Academy)?

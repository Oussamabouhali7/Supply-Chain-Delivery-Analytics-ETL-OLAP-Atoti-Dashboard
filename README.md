# Supply Chain Delivery Analytics

## ETL, Data Warehouse, OLAP & Atoti Dashboard

## 📌 Overview

This project is a Business Intelligence and Data Analytics solution focused on **supply chain delivery data**.

The project covers the complete data workflow, from raw data integration and ETL to multidimensional modeling, OLAP analysis, and interactive visualization with Atoti.

The main objective is to analyze delivery quantities, order prices, suppliers, countries, and delivery times.

---

## 🎯 Objectives

- Extract and transform delivery data.
- Integrate delivery data with a country reference dataset.
- Build a multidimensional data model.
- Store structured data in PostgreSQL.
- Perform data analysis using Python and Pandas.
- Create an OLAP model using Atoti.
- Build interactive dashboards for delivery analysis.

---

## 📊 Dataset

The main delivery dataset contains the following fields:

| Column | Description |
|---|---|
| `id` | Delivery identifier |
| `NomFournisseur` | Supplier name |
| `AddressFournisseur` | Supplier address |
| `idPays` | Supplier country ID |
| `idPaysLivraison` | Delivery country ID |
| `DateLivraison` | Delivery date |
| `TempsLivraison` | Delivery time |
| `Qte` | Delivery quantity |
| `PrixCommande` | Order price |

A separate country reference file is used to map country IDs to country codes and names.

Example:

```text
"1";"AF";"Afghanistan"
🔄 ETL Process

The project follows a standard ETL workflow:

Raw Data
   ↓
Extract
   ↓
Transform & Integrate
   ↓
PostgreSQL
   ↓
Pandas / OLAP
   ↓
Atoti Dashboard

The ETL process includes:

Data extraction
Data cleaning
Country lookup and integration
Data transformation
Fact and dimension preparation
Loading into PostgreSQL

Talend is also used for data integration and ETL operations.

🏗️ Data Warehouse

The data warehouse follows a star schema centered around the Livraison fact table.

                 Fournisseur
                      │
                      ▼
                   Livraison
                  /         \
                 ▼           ▼
              Temps        Chemin
Fact Table

Livraison

Main measures:

Qte
PrixCommande
Dimensions

Fournisseur

Supplier name
Supplier address

Temps

Delivery date
Delivery time

Chemin

Supplier country
Delivery country
🐍 Python & Pandas

Python and Pandas are used to import, transform, and analyze the data.

The main datasets are loaded into Pandas DataFrames before being used for analytical processing.

import pandas as pd

livraison_df = pd.read_sql_query(
    "SELECT * FROM Livraison",
    connection
)
📈 OLAP Analysis with Atoti

Atoti is used to create the OLAP environment and explore the multidimensional data.

import atoti as tt

session = tt.create_session(
    config={"port": 9090}
)

session.link()

The analytical model connects the delivery fact table with the supplier, time, and geographical dimensions.

📊 Dashboard

The dashboard provides several analytical views:

Quantity by Country

Analysis of delivery quantities according to country.

Order Price by Country

Analysis of order prices according to country.

Order Price by Delivery Quantity

Analysis of the relationship between delivery quantity and order price.

🛠️ Technologies
Technology	Purpose
Python	Data processing
Pandas	Data analysis
PostgreSQL	Data warehouse
SQL	Database modeling
Talend	ETL & data integration
Atoti	OLAP & visualization
Jupyter Notebook	Development & analysis

🚀 Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/supply-chain-delivery-analytics.git
cd supply-chain-delivery-analytics

Install the required dependencies:

pip install -r requirements.txt

Configure the PostgreSQL database and update the database connection parameters.

Run the ETL process:

python etl/etl.py

Then launch the Jupyter Notebook:

jupyter notebook

Run the Atoti analysis to access the interactive dashboard.




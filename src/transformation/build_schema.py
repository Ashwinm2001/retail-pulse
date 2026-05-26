from google.cloud import bigquery

# =========================
# DIM CUSTOMER
# =========================
dim_customer_schema = [
    bigquery.SchemaField("customer_id", "STRING"),
    bigquery.SchemaField("customer_name", "STRING"),
    bigquery.SchemaField("segment", "STRING"),
    bigquery.SchemaField("city", "STRING"),
    bigquery.SchemaField("state", "STRING"),
    bigquery.SchemaField("country", "STRING"),
]

# =========================
# DIM PRODUCT
# =========================
dim_product_schema = [
    bigquery.SchemaField("product_id", "STRING"),
    bigquery.SchemaField("product_name", "STRING"),
    bigquery.SchemaField("category", "STRING"),
    bigquery.SchemaField("subcategory", "STRING"),
]

# =========================
# DIM STORE
# =========================
dim_store_schema = [
    bigquery.SchemaField("store_id", "STRING"),
    bigquery.SchemaField("store_name", "STRING"),
    bigquery.SchemaField("region", "STRING"),
    bigquery.SchemaField("city", "STRING"),
]

# =========================
# DIM DATE
# =========================
dim_date_schema = [
    bigquery.SchemaField("date", "DATE"),
    bigquery.SchemaField("year", "INTEGER"),
    bigquery.SchemaField("quarter", "INTEGER"),
    bigquery.SchemaField("month", "INTEGER"),
    bigquery.SchemaField("month_name", "STRING"),
    bigquery.SchemaField("week", "INTEGER"),
    bigquery.SchemaField("day", "INTEGER"),
    bigquery.SchemaField("day_name", "STRING"),
]

# =========================
# FACT SALES
# =========================
fact_sales_schema = [
    bigquery.SchemaField("transaction_id", "STRING"),
    bigquery.SchemaField("customer_id", "STRING"),
    bigquery.SchemaField("product_id", "STRING"),
    bigquery.SchemaField("store_id", "STRING"),
    bigquery.SchemaField("order_date", "DATE"),
    bigquery.SchemaField("sales_amount", "FLOAT"),
    bigquery.SchemaField("quantity", "INTEGER"),
    bigquery.SchemaField("profit", "FLOAT"),
]

# =========================
# CUSTOMER RFM
# =========================
customer_rfm_schema = [
    bigquery.SchemaField("customer_id", "STRING"),
    bigquery.SchemaField("recency", "INTEGER"),
    bigquery.SchemaField("frequency", "INTEGER"),
    bigquery.SchemaField("monetary", "FLOAT"),
    bigquery.SchemaField("rfm_segment", "STRING"),
]

# =========================
# SALES ANOMALIES
# =========================
sales_anomalies_schema = [
    bigquery.SchemaField("date", "DATE"),
    bigquery.SchemaField("sales", "FLOAT"),
    bigquery.SchemaField("expected_sales", "FLOAT"),
    bigquery.SchemaField("anomaly_score", "FLOAT"),
    bigquery.SchemaField("is_anomaly", "BOOLEAN"),
]

# =========================
# SALES FORECAST
# =========================
sales_forecast_schema = [
    bigquery.SchemaField("forecast_date", "DATE"),
    bigquery.SchemaField("predicted_sales", "FLOAT"),
    bigquery.SchemaField("lower_bound", "FLOAT"),
    bigquery.SchemaField("upper_bound", "FLOAT"),
]

# =========================
# LIVE TRANSACTIONS
# =========================
live_transactions_schema = [
    bigquery.SchemaField("transaction_id", "STRING"),
    bigquery.SchemaField("timestamp", "TIMESTAMP"),
    bigquery.SchemaField("customer_id", "STRING"),
    bigquery.SchemaField("product_id", "STRING"),
    bigquery.SchemaField("sales_amount", "FLOAT"),
]
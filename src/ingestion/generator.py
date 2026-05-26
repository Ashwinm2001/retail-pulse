from faker import Faker
import random
import datetime
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
import schedule
import time

# -----------------------------
# AUTHENTICATION
# -----------------------------
credentials = service_account.Credentials.from_service_account_file(
    "Credential/retail-pulse-496303-ca384c444638.json"
)

client = bigquery.Client(
    credentials=credentials,
    project="retail-pulse-496303"
)

# -----------------------------
# FAKER SETUP
# -----------------------------
fake = Faker()

PRODUCTS = [
    "FUR-CH-001",
    "OFF-ST-002",
    "TEC-PH-003",
    "OFF-BI-004"
]

CATEGORIES = {
    "FUR-CH-001": "Furniture",
    "OFF-ST-002": "Office",
    "TEC-PH-003": "Technology",
    "OFF-BI-004": "Office"
}

REGIONS = ["West", "East", "Central", "South"]

# -----------------------------
# GENERATE TRANSACTION
# -----------------------------
def generate_transaction():

    product = random.choice(PRODUCTS)

    qty = random.randint(1, 10)

    price = round(random.uniform(20, 800), 2)

    discount = round(
        random.choice([0, 0.1, 0.2, 0.3]),
        2
    )

    revenue = round(
        price * qty * (1 - discount),
        2
    )

    profit = round(
        revenue * random.uniform(0.05, 0.35),
        2
    )

    return {

        "order_id": fake.uuid4()[:8].upper(),

        "order_timestamp": datetime.datetime.now(
            datetime.timezone.utc
        ),

        "customer_name": fake.name(),

        "product_id": product,

        "category": CATEGORIES[product],

        "region": random.choice(REGIONS),

        "city": fake.city(),

        "quantity": qty,

        "revenue": revenue,

        "profit": profit,

        "discount_pct": discount
    }

# -----------------------------
# UPLOAD TO BIGQUERY
# -----------------------------
def upload_to_bigquery():

    try:

        rows = [
            generate_transaction()
            for _ in range(random.randint(10, 20))
        ]

        df = pd.DataFrame(rows)

        # Convert timestamp properly
        df["order_timestamp"] = pd.to_datetime(
            df["order_timestamp"]
        )

        table_id = (
            "retail-pulse-496303."
            "raw_data.live_transactions"
        )

        job = client.load_table_from_dataframe(
            df,
            table_id
        )

        job.result()

        print(
            f"SUCCESS: Uploaded {len(df)} rows"
        )

    except Exception as e:

        print("ERROR:", e)

# -----------------------------
# FIRST RUN IMMEDIATELY
# -----------------------------
upload_to_bigquery()

# -----------------------------
# SCHEDULER
# -----------------------------
schedule.every(1).minutes.do(
    upload_to_bigquery
)

print(
    "Streaming started. "
    "New data every 1 minute..."
)

# -----------------------------
# KEEP RUNNING
# -----------------------------
while True:

    schedule.run_pending()

    time.sleep(1)
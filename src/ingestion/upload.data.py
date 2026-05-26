import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

# Load credentials
credentials = service_account.Credentials.from_service_account_file(
    "Credential/retail-pulse-496303-ca384c444638.json"
)

# Create BigQuery client
client = bigquery.Client(
    credentials=credentials,
    project="retail-pulse-496303"
)

# Read Excel file
df = pd.read_excel("Data/superstore.xlsx")

# BigQuery table ID
table_id = "retail-pulse-496303.raw_data.superstore"

# Upload dataframe
job = client.load_table_from_dataframe(df, table_id)

# Wait for upload to complete
job.result()

print("Upload complete!")
print(f"Rows uploaded: {len(df)}")
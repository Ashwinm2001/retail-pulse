from google.cloud import bigquery
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    "Credential/retail-pulse-496303-ca384c444638.json"
)

client = bigquery.Client(
    credentials=credentials,
    project="retail-pulse-496303"
)

print("SUCCESS!")
print(client.project)
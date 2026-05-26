from google.cloud import bigquery
from google.oauth2 import service_account
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import pandas as pd
import os


# =====================================================
# BIGQUERY CONNECTION
# =====================================================

credentials = service_account.Credentials.from_service_account_file(
    r"E:\retail-pulse-project\Credential\retail-pulse-496303-ca384c444638.json"
)

client = bigquery.Client(
    credentials=credentials,
    project="retail-pulse-496303"
)

print("Connected to BigQuery!")

# =====================================================
# SENDGRID CONFIG
# =====================================================


SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

FROM_EMAIL = "ashwin2001hitech@gmail.com"
TO_EMAIL = "ashwinmanojinkl18@gmail.com"

# =====================================================
# EMAIL ALERT FUNCTION
# =====================================================

def send_alert(subject, data, alert_type):

    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=TO_EMAIL,
        subject=subject,
        html_content=f"""
        <h2>{subject}</h2>

        <p><b>Alert Type:</b> {alert_type}</p>

        <p><b>Alert Details:</b></p>

        <pre>{data}</pre>
        """
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)

        response = sg.send(message)

        print(f"Alert sent successfully! Status Code: {response.status_code}")

    except Exception as e:
        print("Failed to send email:", e)

# =====================================================
# REVENUE SPIKE / DROP CHECK
# =====================================================

def check_revenue_spike():

    print("Checking revenue spikes...")

    query = """
    WITH latest_day AS (

        SELECT
            MAX(DATE(order_date)) AS latest_date

        FROM raw_data.fact_sales
    ),

    today AS (

        SELECT
            SUM(sales) AS today_rev

        FROM raw_data.fact_sales
        CROSS JOIN latest_day

        WHERE DATE(order_date) = latest_date
    ),

    rolling_avg AS (

        SELECT
            AVG(daily_rev) AS avg_7d

        FROM (

            SELECT
                DATE(order_date) AS dt,
                SUM(sales) AS daily_rev

            FROM raw_data.fact_sales
            CROSS JOIN latest_day

            WHERE DATE(order_date)
                  BETWEEN DATE_SUB(latest_date, INTERVAL 7 DAY)
                  AND DATE_SUB(latest_date, INTERVAL 1 DAY)

            GROUP BY dt
        )
    )

    SELECT
        today_rev,
        avg_7d,

        ROUND(
            (today_rev - avg_7d) / avg_7d * 100,
            1
        ) AS pct_change

    FROM today, rolling_avg
    """

    result = client.query(query).to_dataframe().iloc[0]

    print(result)

    # Handle NULL values
    if pd.isna(result['pct_change']):

        print("No sufficient data available for revenue comparison.")
        return

    if result['pct_change'] > 30:

        send_alert(
            "Revenue Spike Detected",
            result,
            "spike"
        )

    elif result['pct_change'] < -20:

        send_alert(
            "Revenue Drop Alert",
            result,
            "drop"
        )

# =====================================================
# ANOMALY DETECTION CHECK
# =====================================================

def check_anomalies():

    print("Checking anomalies...")

    query = """
    SELECT *
    FROM raw_data.sales_anomalies
    WHERE is_anomaly = TRUE
    """

    result = client.query(query).to_dataframe()

    print(result)

    if not result.empty:

        send_alert(
            "Sales Anomaly Detected",
            result,
            "anomaly"
        )

# =====================================================
# DASHBOARD HEALTH CHECK
# =====================================================

def check_dashboard_health():

    print("Checking dashboard health...")

    query = """
    SELECT
        MAX(DATE(order_date)) AS latest_date
    FROM raw_data.fact_sales
    """

    result = client.query(query).to_dataframe().iloc[0]

    latest_date = str(result['latest_date'])

    today_date = str(pd.Timestamp.today().date())

    print("Latest Data:", latest_date)
    print("Today's Date:", today_date)

    if latest_date != today_date:

        send_alert(
            "Dashboard Data Delay",
            result,
            "health"
        )

# =====================================================
# MAIN EXECUTION
# =====================================================

if __name__ == "__main__":

    print("===================================")
    print("RETAIL PULSE ALERT ENGINE STARTED")
    print("===================================")

    check_revenue_spike()

    # Inventory check disabled because inventory column
    # does not exist in dim_product table

    check_anomalies()

    check_dashboard_health()

    print("===================================")
    print("ALL CHECKS COMPLETED")
    print("===================================")
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# =========================================
# STEP 1 — CREATE HTML EMAIL TEMPLATE
# =========================================

def build_email_html(alert_type, metrics):

    # Set colour based on alert type
    if alert_type == "spike":
        colour = "green"

    elif alert_type == "drop":
        colour = "red"

    else:
        colour = "orange"

    # HTML Email Design
    return f"""
    <html>

    <body style="font-family:Arial;padding:20px;">

        <h1 style="color:{colour};">
            Retail Pulse Alert
        </h1>

        <hr>

        <p>
            <strong>Today's Revenue:</strong>
            ${metrics['today_rev']}
        </p>

        <p>
            <strong>7-Day Average:</strong>
            ${metrics['avg_7d']}
        </p>

        <p>
            <strong>Percentage Change:</strong>
            {metrics['pct_change']}%
        </p>

        <br>

        <a href="https://app.powerbi.com/"
           style="
                background:{colour};
                color:white;
                padding:10px 20px;
                text-decoration:none;
                border-radius:5px;
           ">
           View Dashboard
        </a>

    </body>

    </html>
    """


# =========================================
# STEP 2 — SAMPLE METRICS
# =========================================

metrics = {
    "today_rev": 120000,
    "avg_7d": 95000,
    "pct_change": 26
}


# =========================================
# STEP 3 — BUILD HTML
# =========================================

html = build_email_html("spike", metrics)


# =========================================
# STEP 4 — SEND EMAIL
# =========================================

sender_email = "ashwin2001hitech@gmail.com"
receiver_email = "ashwinmanojinkl18@gmail.com"

message = Mail(
    from_email=sender_email,
    to_emails=receiver_email,
    subject="Retail Pulse Revenue Alert",
    html_content=html
)

try:
    sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))

    response = sg.send(message)

    print("Email sent successfully!")
    print(response.status_code)

except Exception as e:
    print(e)
import json
import random
import uuid
from datetime import datetime, timedelta

# Parameters
NUM_RECORDS = 95
OUTPUT_FILE = "fraud_alerts.json"

transaction_types = ["wire_transfer", "ATM_withdrawal", "online_purchase", "POS_purchase", "mobile_wallet"]
locations = ["Mumbai, India", "Delhi, India", "London, UK", "New York, USA", "Singapore", "Dubai, UAE"]
alert_types = [
    "High-value transfer anomaly",
    "Geolocation anomaly",
    "Unusual merchant category",
    "Suspicious login attempt",
    "Velocity anomaly"
]
risk_indicators_pool = [
    "High amount", "New IP", "Cross-border transfer",
    "Location mismatch", "Velocity anomaly",
    "Device change", "Unusual merchant", "Multiple failed logins"
]
outcomes = ["fraud", "false_positive", "pending"]

# 10 varied alert descriptions
alert_descriptions = [
    "Transaction exceeds threshold; IP mismatch with account history.",
    "ATM withdrawal from foreign country within short time window.",
    "Purchase from merchant category not seen in last 12 months.",
    "Multiple failed login attempts detected before transaction.",
    "Device fingerprint differs from usual customer device.",
    "High velocity of transactions observed in last hour.",
    "Cross-border transfer flagged outside normal pattern.",
    "Unusual time of transaction compared to account history.",
    "Large withdrawal after recent password reset.",
    "Login from suspicious geolocation followed by transaction."
]

def random_alert(i):
    timestamp = datetime.utcnow() - timedelta(minutes=random.randint(0, 100000))
    return {
        "alert_id": f"ALRT-{i:06d}",
        "timestamp": timestamp.isoformat() + "Z",
        "account_id": f"ACC-{random.randint(100000, 999999)}",
        "transaction_amount": round(random.uniform(10, 50000), 2),
        "transaction_type": random.choice(transaction_types),
        "location": random.choice(locations),
        "device_info": f"Device-{uuid.uuid4().hex[:8]}-{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
        "alert_type": random.choice(alert_types),
        "severity_score": random.randint(1, 100),
        "severity_label": random.choice(["Low", "Medium", "High", "Critical"]),
        "alert_description": random.choice(alert_descriptions),
        "risk_indicators": random.sample(risk_indicators_pool, random.randint(1, 3)),
        "investigation_outcome": random.choices(outcomes, weights=[0.15, 0.7, 0.15])[0]
    }

# Generate dataset
alerts = [random_alert(i) for i in range(1, NUM_RECORDS + 1)]

# Save to JSON file
with open(OUTPUT_FILE, "w") as f:
    json.dump(alerts, f, indent=2)

print(f"Generated {NUM_RECORDS} fraud alerts into {OUTPUT_FILE}")

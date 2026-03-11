import pandas as pd

# Load login data
data = pd.read_csv("data/sample_log.csv", parse_dates=["timestamp"])

# Count failed attempts per user
failed_attempts = data[data['status'] == 'failure'].groupby('username').size()

# Threshold for suspicious activity
THRESHOLD = 3

# Identify suspicious users
suspicious_users = failed_attempts[failed_attempts >= THRESHOLD]

print("Suspicious Users Detected:")
for user, attempts in suspicious_users.items():
    print(f"User: {user}, Failed Attempts: {attempts}")

# Optional: save results to CSV
suspicious_users.to_csv("data/suspicious_users.csv", header=True)
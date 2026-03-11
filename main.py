import pandas as pd
import argparse

# -----------------------------
# CLI Arguments
# -----------------------------
parser = argparse.ArgumentParser(description="Detect suspicious login activity")
parser.add_argument("--input", type=str, default="data/sample_log.csv", help="Input CSV file")
parser.add_argument("--threshold", type=int, default=3, help="Failed login threshold")
parser.add_argument("--output", type=str, default="data/suspicious_users.csv", help="Output CSV file")
parser.add_argument("--time_output", type=str, default="data/suspicious_users_time.csv", help="Output CSV for time-based detection")
args = parser.parse_args()

# -----------------------------
# Load Login Data
# -----------------------------
data = pd.read_csv(args.input, parse_dates=["timestamp"])

# -----------------------------
# Threshold-based Detection
# -----------------------------
failed_attempts = data[data['status'] == 'failure'].groupby('username').size()
suspicious_users = failed_attempts[failed_attempts >= args.threshold]

print("Suspicious Users Detected (Total Failures >= Threshold):")
for user, attempts in suspicious_users.items():
    print(f"User: {user}, Failed Attempts: {attempts}")

# Save threshold-based results
suspicious_users.to_csv(args.output, header=True)
print(f"\nThreshold-based suspicious users saved to {args.output}")

# -----------------------------
# Time-based Detection
# -----------------------------
data['timestamp'] = pd.to_datetime(data['timestamp'])
suspicious_users_time = []

for user, group in data[data['status'] == 'failure'].groupby('username'):
    group = group.sort_values('timestamp')
    times = group['timestamp'].tolist()
    for i in range(len(times) - args.threshold + 1):
        # Check if consecutive failures happen within 10 minutes
        if (times[i + args.threshold - 1] - times[i]).seconds <= 600:
            suspicious_users_time.append(user)
            break

print("\nSuspicious Users within 10 minutes:")
for user in suspicious_users_time:
    print(f"User: {user}")

# Save time-based results
pd.DataFrame(suspicious_users_time, columns=['username']).to_csv(args.time_output, index=False)
print(f"\nTime-based suspicious users saved to {args.time_output}")
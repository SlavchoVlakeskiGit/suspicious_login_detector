# Suspicious Login Detector

A small Python tool to detect suspicious login activity by counting failed login attempts per user.

## Features
- Counts failed logins per user
- Flags users exceeding threshold (default: 3)
- Exports flagged users to CSV

## Usage
1. Place your login CSV file in `data/`
2. Run the script:
   ```bash
   python main.py --threshold 5
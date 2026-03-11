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
   python main.py

Optionally, set a custom threshold:

python main.py --threshold 5

Check data/suspicious_users.csv for flagged users

Skills Demonstrated

Basic log analysis

Anomaly detection

Python scripting

Future Improvements

Detect logins from unexpected countries/IPs

Send email alerts for suspicious activity

Add GUI for easier visualization


---

### **Key fixes I made**

1. **Closed all code blocks** with triple backticks ```  
2. Removed text outside headings or code blocks that was breaking formatting  
3. All headings use `#` + space or `##` + space  
4. Everything is **clean and ready to render** on GitHub  

---

### **After copying**

1. Save the file as `README.md` in your project folder (`D:\suspicious_login_detector`)  
2. Stage and commit:

```cmd
git add README.md
git commit -m "fix README formatting for GitHub"
git push
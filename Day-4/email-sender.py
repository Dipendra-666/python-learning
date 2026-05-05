import re
import json
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from collections import defaultdict

# ===================== CONFIG =====================
LOG_FILE = 'app.log'
ERROR_THRESHOLD = 3
REPORT_FILE = f'error_report_{datetime.now().strftime("%Y%m%d_%H%M")}.json'

# Email Configuration (Gmail example)
EMAIL_CONFIG = {
    'sender': 'your.email@gmail.com',
    'password': 'your_app_password',   # Use App Password if using Gmail
    'receiver': 'alert@company.com',
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587
}
# ================================================

def parse_log_file():
    errors = []
    cutoff_time = datetime.now() - timedelta(hours=24)
    
    log_pattern = r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] (ERROR|CRITICAL) - (.+)'
    
    with open(LOG_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.match(log_pattern, line.strip())
            if match:
                log_time_str, level, message = match.groups()
                log_time = datetime.strptime(log_time_str, "%Y-%m-%d %H:%M:%S")
                
                if log_time >= cutoff_time:
                    errors.append({
                        'timestamp': log_time_str,
                        'level': level,
                        'message': message.strip()
                    })
    return errors


def analyze_errors(errors):
    summary = defaultdict(int)
    for error in errors:
        # Group similar errors
        key = error['message'][:100]  # First 100 chars to group similar ones
        summary[key] += 1
    
    return dict(summary)


def send_email(summary, total_errors):
    if total_errors < ERROR_THRESHOLD:
        print(f"✅ Only {total_errors} errors found. No alert sent.")
        return
    
    subject = f"🚨 ALERT: {total_errors} Errors in Last 24 Hours"
    
    body = f"Error Summary Report\n"
    body += f"Total Errors: {total_errors}\n"
    body += f"Time: {datetime.now()}\n\n"
    body += "Top Errors:\n"
    
    for msg, count in sorted(summary.items(), key=lambda x: x[1], reverse=True):
        body += f"• [{count}x] {msg}\n"
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_CONFIG['sender']
    msg['To'] = EMAIL_CONFIG['receiver']
    
    try:
        with smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port']) as server:
            server.starttls()
            server.login(EMAIL_CONFIG['sender'], EMAIL_CONFIG['password'])
            server.send_message(msg)
        print("📧 Alert email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")


# ===================== MAIN =====================
if __name__ == "__main__":
    print("🔍 Analyzing logs...")
    errors = parse_log_file()
    
    if not errors:
        print("✅ No errors found in last 24 hours.")
    else:
        summary = analyze_errors(errors)
        total_errors = len(errors)
        
        # Save report
        report = {
            'timestamp': datetime.now().isoformat(),
            'total_errors': total_errors,
            'summary': summary,
            'details': errors
        }
        
        with open(REPORT_FILE, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"📊 Found {total_errors} errors. Report saved to {REPORT_FILE}")
        
        # Send alert if needed
        send_email(summary, total_errors)
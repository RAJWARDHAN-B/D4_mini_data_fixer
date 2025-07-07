import pandas as pd
import re

def detect_issues(df):
    issues = {
        'missing_emails': df[df['email'].isnull()],
        'invalid_emails': df[~df['email'].astype(str).str.match(r"[^@]+@[^@]+\.[^@]+")],
        'duplicate_rows': df[df.duplicated()],
        'suspect_countries': df[~df['country'].str.lower().isin(load_valid_countries())]
    }

    log = []
    for key, value in issues.items():
        log.append(f"{key}: {len(value)} issues found")

    with open("logs/detection_log.txt", "w") as f:
        f.write("\n".join(log))

    return issues

def load_valid_countries():
    with open("countries.txt") as f:
        return [line.strip().lower() for line in f]

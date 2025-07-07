import pandas as pd
import re
from fuzzywuzzy import process

def correct_data(df):
    log = []

    # Normalize name and country casing
    df['name'] = df['name'].astype(str).str.strip().str.title()
    df['country'] = df['country'].astype(str).str.strip().str.title()

    # Remove duplicates by name
    before = len(df)
    df = df.drop_duplicates(subset=['name']).copy()
    after = len(df)
    log.append(f"Removed {before - after} duplicate rows based on name")

    # Fix email
    df['email'] = df['email'].fillna("").apply(fix_email)
    df.loc[df['email'] == "", 'email'] = "unknown@example.com"

    # Fix country names
    valid_countries = load_valid_countries()
    df['country'] = df['country'].apply(lambda c: fuzzy_correct(c, valid_countries, log))

    with open("logs/correction_log.txt", "w") as f:
        f.write("\n".join(log))

    return df

def fix_email(email):
    email = email.replace("[at]", "@").replace(" ", "").replace("..", ".")
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return ""
    return email

def load_valid_countries():
    with open("countries.txt") as f:
        return [line.strip().title() for line in f]

def fuzzy_correct(country, valid_list, log):
    country = str(country).strip().title()
    if country in valid_list:
        return country

    match, score = process.extractOne(country, valid_list)
    if score >= 60:  # Relaxed threshold
        log.append(f"Corrected '{country}' to '{match}' (score: {score})")
        return match
    else:
        log.append(f"Could not confidently correct '{country}' (best: {match}, score: {score})")
        return "Unknown"

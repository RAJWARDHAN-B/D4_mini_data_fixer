import pandas as pd
from agents.detection_agent import detect_issues
from agents.correction_agent import correct_data
from agents.enrichment_agent import enrich_data

def run_pipeline():
    df = pd.read_csv("data/raw_customers.csv")
    detect_issues(df)

    df = correct_data(df)
    df = enrich_data(df)

    df.to_csv("data/cleaned_customers.csv", index=False)
    print("Data cleaning completed. Output saved to 'data/cleaned_customers.csv'.")

if __name__ == "__main__":
    run_pipeline()

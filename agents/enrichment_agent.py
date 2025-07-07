def enrich_data(df):
    log = []
    df['is_email_missing'] = df['email'] == "unknown@example.com"
    df['name_length'] = df['name'].apply(lambda x: len(str(x)))

    log.append("Added 'is_email_missing' and 'name_length' columns.")

    with open("logs/enrichment_log.txt", "w") as f:
        f.write("\n".join(log))

    return df

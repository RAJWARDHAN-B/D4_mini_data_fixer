# D4 Customer Data Cleaning Pipeline

This project implements a modular data cleaning pipeline using Python. It reads raw customer data, detects and corrects common issues, enriches the dataset with additional features, and saves the cleaned data.

---

## 📂 Project Structure
├── main.py
├── agents/
│ ├── detection_agent.py
│ ├── correction_agent.py
│ └── enrichment_agent.py
├── data/
│ └── raw_customers.csv
├── logs/
│ ├── detection_log.txt
│ ├── correction_log.txt
│ └── enrichment_log.txt
└── countries.txt


---

## 🚀 How It Works

1. **Input**: Reads customer data from `data/raw_customers.csv`.
2. **Detection**: Identifies missing or invalid emails, duplicate records, and suspect country values.
3. **Correction**:
   - Fixes email formatting issues.
   - Normalizes name and country casing.
   - Removes duplicate customer entries.
   - Fuzzy matches incorrect country names with a valid list (`countries.txt`).
4. **Enrichment**: Adds:
   - `is_email_missing`: whether the email was missing and defaulted.
   - `name_length`: number of characters in the customer's name.
5. **Output**: Writes cleaned data to `data/cleaned_customers.csv`.

---

## 🛠️ Installation

Make sure you have Python 3.7+ installed. Then install dependencies:

```bash
pip install pandas fuzzywuzzy python-Levenshtein

---

## ▶️ Usage

Run the main pipeline:

```bash
python main.py




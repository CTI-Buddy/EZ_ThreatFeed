import requests
import json
import pandas as pd
from datetime import datetime
import time
import logging

# Set up logging for better error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to fetch data from C2IntelFeeds (GitHub)
def fetch_c2intelfeeds():
    try:
        c2intel_url = "https://raw.githubusercontent.com/drb-ra/C2IntelFeeds/master/feeds/c2-domains.csv"
        response = requests.get(c2intel_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.text.splitlines()
        iocs = [(line.strip(), 'C2IntelFeeds', 'C2 Domain') for line in data]  # Parse each domain
        logging.info(f"Fetched {len(iocs)} IOCs from C2IntelFeeds.")
        return iocs
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch data from C2IntelFeeds: {e}")
        return []

# Function to process and normalize data into a consistent structure
def process_iocs(iocs, source):
    processed = []
    for ioc in iocs:
        indicator, source, threat_type = ioc
        processed.append({
            "ioc": indicator,
            "source": source,
            "threat_type": threat_type,
            "actor": "Unknown",  # Placeholder for now
            "activity": "Unknown",  # Placeholder for now
            "severity": source,  # Severity based on the source
            "confidence_level": "High",  # Placeholder, add logic to determine confidence
            "tags": [],  # Placeholder for additional tags (e.g., "Phishing", "APT")
            "ref_link": f"https://github.com/drb-ra/C2IntelFeeds"  # Link to C2IntelFeeds repo
        })
    return processed

# Function to save data as JSON or CSV (appending new data)
def save_output(data, output_format="json"):
    try:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        if output_format == "json":
            with open(f"aggregated_iocs_{timestamp}.json", "w") as f:
                json.dump(data, f, indent=4)
            logging.info(f"Saved output as JSON: aggregated_iocs_{timestamp}.json")
        elif output_format == "csv":
            df = pd.DataFrame(data)
            df.to_csv(f"aggregated_iocs_{timestamp}.csv", index=False)
            logging.info(f"Saved output as CSV: aggregated_iocs_{timestamp}.csv")
    except Exception as e:
        logging.error(f"Failed to save output: {e}")

# Main function to aggregate and append new data
def aggregate_data(limit=100):
    # Fetch data from C2IntelFeeds
    c2intel_data = fetch_c2intelfeeds()
    
    if not c2intel_data:
        logging.warning("No data fetched from C2IntelFeeds. Exiting.")
        return

    # Process the data from C2IntelFeeds
    aggregated_data = []
    aggregated_data.extend(process_iocs(c2intel_data, 'C2IntelFeeds'))

    # Save the data as JSON or CSV (append to a new file with timestamp)
    save_output(aggregated_data, output_format="json")  # Change to "csv" if you prefer CSV

if __name__ == "__main__":
    aggregate_data()

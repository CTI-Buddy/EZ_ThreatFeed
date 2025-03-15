# EZ ThreatFeed

This Python-based script aggregates fresh indicators of compromise (IOCs) from multiple open-source threat intelligence feeds and outputs them in a standardized format (JSON or CSV). The purpose of this tool is to collect and process IOCs, including domains, URLs, and other threat-related data, into a centralized repository for further analysis.

## Features
- Aggregates IOCs from multiple sources:
  - **C2IntelFeeds** (GitHub)
  - **Abuse.ch URLhaus** (URL submissions)
  - **Abuse.ch ThreatFox** (Malicious IPs and URLs)
  - **Abuse.ch Payloads** (Malicious payloads)
- Outputs data in **JSON** or **CSV** formats.
- Data includes IOC, source, threat type, severity, and other relevant metadata.
- Simple, lightweight tool for continuous threat intelligence collection.

## Installation

### Requirements
- Python 3.x
- `requests` library
- `pandas` library

### Installing Dependencies

To install the required dependencies, use `pip`:

```bash
pip install requests pandas
```

## Usage

### Running the Script

To run the script, simply execute the following command:

```bash
python EZ_ThreatFeed.py
```

This will fetch the latest IOCs from the defined sources, process them, and save the results in either JSON or CSV format in the current working directory.

The output files will be named with a timestamp for easy tracking, e.g., `aggregated_iocs_20250313_154530.json`.

### Changing Output Format

The script currently supports two output formats:

- **JSON**: The default output format. To change it, you can modify the `save_output()` function in the script.
- **CSV**: The output format can also be changed by setting `output_format="csv"` in the `aggregate_data()` function.

### Customizing the Script

You can modify the script to include additional feeds or change the existing ones. To add a new feed:

1. **Fetch the feed data**: Add a new function to fetch the feed, similar to the `fetch_c2intelfeeds()` function.
2. **Process the data**: Write a function to process and format the IOCs in the same structure as the existing ones.
3. **Update the `aggregate_data()` function**: Add the new feed to the aggregation process.

## Example Output

The output will contain a list of IOCs with the following fields:

- **ioc**: The indicator of compromise (e.g., domain, IP, URL).
- **source**: The source of the IOC (e.g., `C2IntelFeeds`, `Abuse.ch`, etc.).
- **threat_type**: The type of threat (e.g., `C2 Domain`, `Malicious URL`).
- **actor**: The actor associated with the IOC (e.g., `Unknown`, `APT34`).
- **activity**: The activity associated with the IOC (e.g., `Phishing`, `Botnet`).
- **severity**: Derived from the source of the IOC (e.g., `C2IntelFeeds`, `Abuse.ch`).
- **confidence_level**: Placeholder for now (can be adjusted based on source reputation).
- **tags**: Optional tags for categorizing the IOC (e.g., `Phishing`, `Ransomware`).
- **ref_link**: A reference link to the source for more information (e.g., GitHub URL).

### Example JSON Output:
```json
[
  {
    "ioc": "example.com",
    "source": "C2IntelFeeds",
    "threat_type": "C2 Domain",
    "actor": "Unknown",
    "activity": "Unknown",
    "severity": "C2IntelFeeds",
    "confidence_level": "High",
    "tags": [],
    "ref_link": "https://github.com/drb-ra/C2IntelFeeds"
  },
  ...
]
```

## Contributing

Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request with new features or improvements.

To contribute:

1. Fork the repository.
2. Clone your fork:
    ```bash
    git clone https://github.com/CTI-Buddy/EZ_ThreatFeed.git
    ```
3. Create a new branch:
    ```bash
    git checkout -b new-feature
    ```
4. Make your changes, commit, and push.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


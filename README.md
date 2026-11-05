# Spam Email Detection and Port Scanner

This repository contains two small Python command-line projects:

- `spamEmaiditection.py` trains a TF-IDF and Random Forest classifier using `data.csv`, then predicts whether a sample message is spam.
- `portScanner.py` checks a range of TCP ports on an IP address or hostname you are authorized to scan.

## Setup

Install Python, then install the project dependencies from PowerShell:

```powershell
py -m pip install -r requirements.txt
```

## Spam email detection

Keep `data.csv` in the project folder. It must contain `input` and `output` columns. Run:

```powershell
py .\spamEmaiditection.py
```

The script trains a model from the CSV and prints the prediction for its sample message.

## TCP port scanner

Provide a target IP or hostname and an inclusive start and end port:

```powershell
py .\portScanner.py 192.168.1.10 1 100
```

Each port is reported as open, closed, or no response. A no-response result can mean that a firewall filtered the connection or that the host could not be reached. The scanner checks TCP only. Scan only systems you own or have permission to assess.

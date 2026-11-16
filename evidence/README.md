# Evidence and Diagnostics

This folder contains verified diagnostic outputs gathered during the missions on macOS Darwin arm64. All sensitive personal identifiers (usernames, serial numbers, local network SSIDs) have been redacted as required.

### 1. Python and Git Verifications
- Python Version: Python 3.9.6
- Git Version: git version 2.55.0

### 2. Network Diagnostics (Mission 7)
- `ping -c 3 example.com`: 0.0% packet loss, ~4.8ms average latency.
- `nslookup example.com`: Resolved to addresses 104.20.23.154 and 172.66.147.243.

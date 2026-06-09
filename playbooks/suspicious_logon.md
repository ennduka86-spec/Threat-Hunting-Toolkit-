# Suspicious Logon Hunt Playbook

## Objective
Identify and investigate suspicious logon activity that may indicate brute force attempts, credential misuse, or lateral movement.

## MITRE ATT&CK Mapping
- **T1110 – Brute Force**
- **T1078 – Valid Accounts**

## Data Sources
- Windows Security Event Logs (Event IDs: 4624, 4625, 4672)
- Authentication logs (SSH, RDP)
- SIEM platforms (Splunk, Elastic Security)

## Detection Queries
- **Splunk SPL**
  ```splunk
  index=wineventlog EventCode=4625
  | stats count by Account_Name, Source_Network_Address
  | where count > 5

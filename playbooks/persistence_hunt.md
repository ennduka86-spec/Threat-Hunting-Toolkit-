# Persistence Hunt Playbook

## Objective
Detect and investigate persistence mechanisms that adversaries use to maintain long‑term access to systems.

## MITRE ATT&CK Mapping
- **T1547 – Boot or Logon Autostart Execution**
- **T1053 – Scheduled Task/Job**
- **T1037 – Logon Scripts**

## Data Sources
- Windows Security Event Logs (Event IDs: 4697, 7045)
- Registry changes (Sysmon Event ID 13)
- Scheduled tasks (Event ID 106)
- Startup folder monitoring

## Detection Queries
- **Splunk SPL**
  ```splunk
  index=wineventlog EventCode=4697 OR EventCode=7045
  | stats count by Service_Name, Service_File_Name, Account_Name

# Phishing Hunt Playbook

## Objective
Detect and investigate phishing attempts delivered via email, focusing on suspicious headers, attachments, and domains.

## MITRE ATT&CK Mapping
- **T1566 – Phishing**
- **T1204 – User Execution**

## Data Sources
- Email gateway logs
- SIEM email ingestion (headers, attachments)
- Threat intelligence feeds

## Detection Queries
- **Splunk SPL**
  ```splunk
  index=email_logs
  | search subject="*" attachment_type="exe" OR attachment_type="js"
  | stats count by sender, subject, attachment_name

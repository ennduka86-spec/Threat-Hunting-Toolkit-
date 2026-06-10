# Threat-Hunting-Toolkit-
Scripts, queries, and playbooks for MITRE ATT&amp;CK‑aligned threat hunting across SIEM (Splunk, Sentinel), EDR (CrowdStrike), and cloud platforms (AWS, Azure). Includes automation workflows, detection rules, and documentation to support proactive SOC investigations.

![GitHub repo size](https://img.shields.io/github/repo-size/ennduka86-spec/Threat-Hunting-Toolkit-?color=blue)
![GitHub stars](https://img.shields.io/github/stars/ennduka86-spec/Threat-Hunting-Toolkit-?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/ennduka86-spec/Threat-Hunting-Toolkit-?color=green)
![Python version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/github/license/ennduka86-spec/Threat-Hunting-Toolkit-?color=yellow)

---

## Overview
Threat-Hunting-Toolkit is a MITRE ATT&CK‑aligned collection of scripts, detection queries, datasets, and playbooks designed for SOC analysts and cybersecurity professionals.  
It demonstrates practical threat hunting workflows across **Windows Event Logs, Linux SSH logs, Splunk SPL, and Elastic KQL**.

---

## 📂 Repository Structure
```text
Threat-Hunting-Toolkit/
├── scripts/              # Automation scripts
│   ├── hunt_parser.py
│   ├── win_event_hunt.ps1
│   └── ssh_hunt.sh
├── queries/              # Detection queries
│   ├── splunk_hunts.spl
│   └── elastic_hunts.kql
├── playbooks/            # Threat hunting playbooks
│   ├── suspicious_logon.md
│   ├── persistence_hunt.md
│   ├── phishing_hunt.md
│   └── cloud_iam_hunt.md
├── datasets/             # Sample datasets
│   ├── sample_events.json
│   └── sample_events_v2.json
├── tests/                # Unit tests
│   └── test_hunt_parser.py
├── README.md
└── LICENSE

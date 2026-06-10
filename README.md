# Threat-Hunting-Toolkit

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![PowerShell](https://img.shields.io/badge/PowerShell-5.1-lightblue?logo=powershell)
![Bash](https://img.shields.io/badge/Bash-4.4-green?logo=gnu-bash)
![Splunk](https://img.shields.io/badge/Splunk-SPL-orange?logo=splunk)
![Elastic](https://img.shields.io/badge/Elastic-KQL-yellow?logo=elastic)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK-red?logo=mitre)

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

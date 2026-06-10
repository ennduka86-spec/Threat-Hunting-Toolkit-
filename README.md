# Threat-Hunting-Toolkit

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![PowerShell](https://img.shields.io/badge/PowerShell-5.1-lightblue?logo=powershell)
![Bash](https://img.shields.io/badge/Bash-4.4-green?logo=gnu-bash)
![Splunk](https://img.shields.io/badge/Splunk-SPL-orange?logo=splunk)
![Elastic](https://img.shields.io/badge/Elastic-KQL-yellow?logo=elastic)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK-red?logo=mitre)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-blue?logo=githubactions)
![CI/CD](https://github.com/ennduka86-spec/Threat-Hunting-Toolkit-/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/github/license/ennduka86-spec/Threat-Hunting-Toolkit-)



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
```
## ⚙️ Installation
Clone the repository and set up dependencies:
```bash
git clone https://github.com/ennduka86-spec/Threat-Hunting-Toolkit-.git
cd Threat-Hunting-Toolkit-
pip install -r requirements.txt

```
## ✨ Features
- Cross-platform scripts
- Detection queries
- Playbooks
- Sample datasets
- Unit tests
## 🔄 Workflow
- Collect logs → Windows, SSH, Cloud, Email
- Parse events → Python, PowerShell, Bash scripts
- Map to MITRE ATT&CK techniques
- Run detection queries (Splunk SPL / Elastic KQL)
- Investigate with playbooks
- Respond & document
## 🔮 Future Work
- Add YARA rules for malware hunting
- Expand cloud playbooks (GCP, Kubernetes)
- Integrate CI/CD pipeline for automated hunts
- Add Splunk/Elastic dashboards
## 🛡️ MITRE ATT&CK Coverage
- T1110 – Brute Force
- T1078 – Valid Accounts
- T1059 – Command Execution
- T1547 – Persistence
- T1566 – Phishing
- T1098 – Account Manipulation
- T1087 – Account Discovery

## 🤝 Contributing
- Contributions are welcome!
- Fork the repository
- Create a feature branch (git checkout -b feature/new-playbook)
- Commit your changes (git commit -m "Add new playbook for persistence")
- Push to the branch (git push origin feature/new-playbook)
- Open a Pull Request
## 🙏 Acknowledgments
- MITRE ATT&CK for technique mapping
- Splunk and Elastic for query frameworks
- Sysmon and Windows Event Logs for telemetry sources
- Community SOC analysts for inspiration and best practices


```
## 📂 Textual Diagram (ASCII Box Style)
  +-------------------+        +-------------------+        +-------------------+
|   Log Sources     | -----> |   Hunt Scripts    | -----> | MITRE ATT&CK Map  |
| (Windows, SSH,    |        | (Python, PS, Bash)|        |   Techniques      |
|  Cloud, Email)    |        +-------------------+        +-------------------+
+-------------------+                 |                           |
                                      v                           v
                              +-------------------+        +-------------------+
                              | Detection Queries | -----> |   Playbooks       |
                              | (Splunk, Elastic) |        | Investigation     |
                              +-------------------+        +-------------------+
                                                                |
                                                                v
                                                        +-------------------+
                                                        | Response Actions  |
                                                        | (Quarantine, MFA, |
                                                        |  Reset, Revoke)   |
                                                        +-------------------+
```
## 📦 Architecture Diagram (Mermaid)
```mermaid
flowchart TD
    A[Logs: Windows, SSH, Cloud, Email] --> B[Scripts: Parser + Hunts]
    B --> C[MITRE ATT&CK Mapping]
    C --> D[Detection Queries: Splunk + Elastic]
    D --> E[Playbooks: Investigation Steps]
    E --> F[Response Actions: Quarantine, Reset, Revoke]
```
## 📌 License
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

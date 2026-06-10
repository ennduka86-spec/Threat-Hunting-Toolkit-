
---

## 📄 `cloud_iam_hunt.md`

```markdown
# Cloud IAM Hunt Playbook

## Objective
Detect and investigate misuse of cloud Identity and Access Management (IAM) roles, policies, and credentials.

## MITRE ATT&CK Mapping
- **T1078 – Valid Accounts**
- **T1098 – Account Manipulation**
- **T1087 – Account Discovery**

## Data Sources
- AWS CloudTrail logs
- Azure AD sign‑in logs
- IAM policy change events

## Detection Queries
- **Splunk SPL**
  ```splunk
  index=cloudtrail eventName=CreateUser OR eventName=AttachRolePolicy
  | stats count by userIdentity.userName, requestParameters.roleName

# hunt_parser.py
import json

MITRE_MAP = {
    "4625": "T1110 - Brute Force",
    "4688": "T1059 - Command Execution",
    "4672": "T1078 - Valid Accounts"
}

def parse_log(file):
    with open(file, "r") as f:
        for line in f:
            event = json.loads(line)
            technique = MITRE_MAP.get(str(event.get("event_id")), "Unknown")
            print(f"{event['timestamp']} | {event['user']} | {event['action']} | {technique}")

if __name__ == "__main__":
    parse_log("datasets/sample_events.json")

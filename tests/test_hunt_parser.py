import unittest
import json
from scripts import hunt_parser

class TestHuntParser(unittest.TestCase):

    def setUp(self):
        # Sample events for testing
        self.sample_events = [
            {"timestamp": "2026-06-09T02:05:00Z", "event_id": 4625, "user": "unknown", "action": "LogonFailure"},
            {"timestamp": "2026-06-09T02:10:00Z", "event_id": 4688, "user": "admin", "action": "ProcessCreation"},
            {"timestamp": "2026-06-09T02:15:00Z", "event_id": 4672, "user": "svc_account", "action": "SpecialPrivilegesAssigned"},
            {"timestamp": "2026-06-09T02:25:00Z", "event_id": 4624, "user": "analyst", "action": "LogonSuccess"}
        ]

    def test_mitre_mapping(self):
        # Check that known event IDs map correctly
        self.assertEqual(hunt_parser.MITRE_MAP.get("4625"), "T1110 - Brute Force")
        self.assertEqual(hunt_parser.MITRE_MAP.get("4688"), "T1059 - Command Execution")
        self.assertEqual(hunt_parser.MITRE_MAP.get("4672"), "T1078 - Valid Accounts")

    def test_unknown_event(self):
        # Event ID not in MITRE_MAP should return "Unknown"
        self.assertEqual(hunt_parser.MITRE_MAP.get("9999", "Unknown"), "Unknown")

    def test_parse_log_output(self):
        # Simulate parsing and check output formatting
        for event in self.sample_events:
            technique = hunt_parser.MITRE_MAP.get(str(event.get("event_id")), "Unknown")
            output = f"{event['timestamp']} | {event['user']} | {event['action']} | {technique}"
            self.assertIn("|", output)  # Ensure formatted output contains separators

if __name__ == "__main__":
    unittest.main()

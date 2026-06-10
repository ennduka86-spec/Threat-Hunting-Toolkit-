#!/bin/bash
# SSH Hunt Script
# Detect brute force attempts in auth.log

LOGFILE="/var/log/auth.log"

echo "=== Failed SSH Logins ==="
grep "Failed password" $LOGFILE | awk '{print $1,$2,$3,$9,$11}' | sort | uniq -c | sort -nr | head -20

echo "=== Successful SSH Logins ==="
grep "Accepted password" $LOGFILE | awk '{print $1,$2,$3,$9,$11}' | sort | uniq -c | sort -nr | head -20

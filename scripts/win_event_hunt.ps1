# Windows Event Hunt Script
# Detect suspicious logons and privilege escalation

# Failed logons (Event ID 4625)
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625} |
Select-Object TimeCreated, @{Name='User';Expression={$_.Properties[5].Value}}, @{Name='IP';Expression={$_.Properties[18].Value}} |
Group-Object User | Where-Object {$_.Count -gt 5}

# Privilege escalation (Event ID 4672)
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4672} |
Select-Object TimeCreated, @{Name='User';Expression={$_.Properties[1].Value}}, @{Name='Privileges';Expression={$_.Properties[2].Value}}

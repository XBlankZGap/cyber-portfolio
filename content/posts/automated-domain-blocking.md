+++
date = '2025-11-05T10:00:00+01:00'
draft = false
title = 'Automated Domain Blocking via Batch Scripting'
categories = ["Network Security & Infrastructure"]
case_id = "AUTOMATION-NET-2025"
vulnerability_class = "Manual Mitigation Inefficiency"
tools = ["Batch Scripting", "VS Code", "Windows Hosts File"]

[cover]
image = "images/feature-automated-domain-blocking.png"

tags = ["Automation", "Security Engineering", "C2 Mitigation", "Endpoint Security"]
+++

**Objective:** To develop a reusable and scalable automation tool for neutralizing network threats at the system level.

<!--more-->

## 1. The Vulnerability: Manual Mitigation Inefficiency

Relying on manual entries to the Windows hosts file for domain blocking is a slow and error-prone process. In an active threat scenario where multiple malicious domains (e.g., `trasre.com`, `shallspark.com`) are identified, the delay in manual configuration increases the window of opportunity for malware to establish a Command-and-Control (C2) connection or exfiltrate data.

## 2. Technical Execution: Scripted Host Redirection

I developed a batch script using the VS Code IDE to automate the redirection of suspicious traffic. The script programmatically appends the local loopback address (127.0.0.1) to the Windows hosts file for every identified malicious domain. This ensures that any application attempting to reach these external servers is immediately redirected back to the local machine, effectively "cutting off" the communication.

| Component | Value | Purpose |
| :--- | :--- | :--- |
| **Language** | Batch (.bat) | Native Windows execution for system-level changes. |
| **Target File** | %SystemRoot%\System32\drivers\etc\hosts | The system file that maps hostnames to IP addresses. |
| **Logic** | Append (>>) | Ensures existing host mappings are preserved while adding new blocks. |
| **Loopback IP** | 127.0.0.1 | The address used to nullify malicious outbound requests. |

## 3. Execution Workflow

1. **Requirement Analysis:** Identified the need for a scalable way to deploy domain blocks across multiple machines after discovering a cluster of suspicious domains in Wireshark.
2. **Script Development:** Authored the `@echo off` script to target the system’s drivers directory and map the identified domains to localhost.
3. **Redundancy Check:** Included both root domains and "www" subdomains in the script to ensure comprehensive coverage.
4. **Verification & Unblocking:** Developed a secondary "unblock" script to restore original host settings for testing and maintenance purposes.

## 4. Key Commands
```batch
:: Snippet of the block-suspicious-domains.bat script 
@echo off
set hostspath=%SystemRoot%\System32\drivers\etc\hosts
echo 127.0.0.1 sparkle0.com>> %hostspath%
echo 127.0.0.1 trasre.com>> %hostspath%
echo Done! The domains have been blocked.
pause
```

## 5. Evidence of Work

![Discovery](/images/project5_script_ide.png)
*Caption: Discovery phase showing the logic and domain list within the IDE before execution.*

![Results](/images/project5_hosts_verification.png)
*Caption: Results phase showing the successful system-level mapping of malicious domains to the loopback address after script execution.*

## 6. Professional Impact

This project significantly improves System Integrity by reducing the time-to-remediate for known network threats. By moving from manual entry to automation, I ensured consistent protection across the environment and reduced human error. This demonstrates an ability to translate threat intelligence into actionable, scalable security infrastructure.

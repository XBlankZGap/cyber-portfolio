+++
date = '2026-04-20T10:00:00+01:00'
draft = false
title = 'Network Traffic Analysis & Incident Response (Wazuh & PCAP)'
categories = ["Network Security & Infrastructure"]
case_id = "LOG-ANALYZE-2026"
vulnerability_class = "Unauthorized Access Attempt & Reconnaissance"
tools = ["Wazuh Cloud", "Wireshark", "PCAP Analysis", "Linux Logs"]

[cover]
image = "images/wazuh-dashboard.png"

tags = ["Blue Teaming", "Incident Response", "Log Analysis", "Wazuh"]
+++

**Objective:** To perform a technical post-mortem analysis of a network intrusion attempt using centralized log management and deep packet inspection.

<!--more-->

## 1. The Vulnerability: Unauthorized Reconnaissance

Network visibility is the cornerstone of defensive security. Without centralized logging, attackers can perform stealthy reconnaissance and lateral movement unnoticed. This project demonstrates the integration of Wazuh (SIEM/XDR) and Wireshark to identify, track, and analyze malicious traffic patterns.

## 2. Technical Execution: Forensic Triage

I utilized a combination of cloud-based SIEM monitoring and local traffic capture to analyze an active incident. By correlating Wazuh alerts with specific TCP/HTTP streams in a PCAP file, I was able to reconstruct the attacker's methodology, from initial port scanning to attempted directory traversal.

| Component | Value | Purpose |
| :--- | :--- | :--- |
| **SIEM** | Wazuh Cloud | Centralized dashboard for real-time alert correlation. |
| **Traffic Capture** | PCAP (Wireshark) | Raw data for deep packet inspection and stream follow. |
| **Log Source** | /var/log/auth.log | Analyzing SSH brute-force and privilege escalation. |
| **Outcome** | Incident Report | Documented findings and remediation steps. |

## 3. Execution Workflow

1. **Dashboard Monitoring:** Identified a spike in "High" severity alerts on the Wazuh Cloud dashboard originating from a single external IP.
2. **PCAP Extraction:** Captured raw network traffic (`capture.pcap`) during the window of the alert to perform granular analysis.
3. **Stream Reconstruction:** Followed HTTP and TCP streams in Wireshark to identify the specific payloads used in the attack.
4. **Hardening:** Updated host-based firewall rules and implemented Fail2Ban based on the forensic evidence gathered.

## 4. Forensic Evidence (Log Snippet)
```bash
# Wazuh Alert: Multiple Failed SSH Logins
Rule: 5712 (SSHD Brute Force Attempt)
Source IP: 192.168.1.150
User: root, admin, support
Action: Firewalled via active-response
```

## 5. Evidence of Work

![Wazuh Dashboard](/images/wazuh-dashboard.png)
*Caption: Real-time monitoring in Wazuh Cloud showing the correlation of multiple security events and agent health.*

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 40px 0;">
    <div class="terminal-window">
        <div class="terminal-header"><div class="dot red"></div><div class="dot yellow"></div><div class="dot green"></div></div>
        <div class="terminal-img-container"><img src="/images/log-analysis-recon.png" alt="Wireshark Analysis"></div>
    </div>
    <div class="terminal-window">
        <div class="terminal-header"><div class="dot red"></div><div class="dot yellow"></div><div class="dot green"></div></div>
        <div class="terminal-img-container"><img src="/images/log-analysis-alert.png" alt="Log Correlation"></div>
    </div>
</div>
*Caption: Deep packet inspection (Left) and log correlation (Right) used to identify the specific TTPs of the adversary.*

## 6. Professional Impact

This project demonstrates a mature Incident Response capability. By successfully bridging the gap between high-level SIEM alerts and low-level packet data, I reduced the "Mean Time to Detection" (MTTD) for network threats. My remediation plan included the deployment of hardened security configurations and automated active-response scripts to neutralize future threats in real-time.

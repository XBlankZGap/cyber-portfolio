+++
date = '2025-07-15T10:00:00+01:00'
draft = false
weight = 300
title = 'Network Traffic Analysis & Automated Threat Mitigation'
categories = ["Network & Infrastructure Security"]
case_id = "TRAFFIC-MITIGATION-2025"
vulnerability_class = "Malicious External Communication"
tools = ["Wireshark", "Windows Hosts File", "Batch Scripting", "Router Filtering"]

[cover]
image = "images/feature-network-traffic-analysis.jpg"

tags = ["Wireshark", "DNS", "C2", "Defense-in-Depth"]
+++

**Objective:** To identify suspicious network traffic using protocol analysis and implement multi-layered blocking mechanisms to secure a local environment.

<!--more-->

## 1. The Vulnerability: Malicious External Communication

During live monitoring of network traffic, I identified several suspicious domains, such as `googleagmanger.com` and `aoneroom.com`, which exhibited characteristics of Command-and-Control (C2) infrastructure. These domains utilized CDN IP rotation to evade traditional security controls and performed frequent DNS resolution attempts, suggesting the presence of adware, tracking scripts, or persistent backdoors.

## 2. Technical Execution: Protocol Interrogation

I utilized Wireshark to perform granular packet inspection, isolating abnormal DNS queries and tracking the CNAME chaining used by attackers to obscure their true server locations.

| Component | Value | Purpose |
| :--- | :--- | :--- |
| **Analysis Tool** | Wireshark | Real-time packet capture and DNS log inspection. |
| **Mitigation 1** | Windows Hosts File | System-level redirection of malicious domains to 127.0.0.1. |
| **Mitigation 2** | Batch Scripting | Automation of the blocking process for speed and scalability. |
| **Mitigation 3** | Router Filtering | Network-wide protection via URL keyword filtering. |

## 3. Execution Workflow

1. **Traffic Baselining:** Monitored legitimate traffic (e.g., Google, Firebase) to establish a behavioral baseline for routine, secure communications.
2. **Threat Identification:** Flagged domains mimicking legitimate services (typosquatting) and those showing repeated queries to unknown subdomains.
3. **Local Nullification:** Manually updated the Windows hosts file to redirect traffic from identified malicious domains to the local loopback address.
4. **Automation & Scalability:** Developed a reusable batch script to automate the host file updates, reducing manual error and deployment time.
5. **Network-Wide Enforcement:** Configured the MTN 4G Router firewall to block these keywords at the gateway, protecting non-Windows devices like mobile phones and IoT hardware.

## 4. Key Commands
```batch
:: Automated domain blocking script snippet
@echo off
set hostspath=%SystemRoot%\System32\drivers\etc\hosts
echo 127.0.0.1 googleagmanger.com>> %hostspath%
echo 127.0.0.1 aoneroom.com>> %hostspath%
```

## 5. Evidence of Work

![Discovery](/images/network-traffic-analysis-discovery.jpeg)
*Caption: Identification of suspicious DNS queries and rotating CDN IPs in Wireshark logs.*

![Discovery](/images/network-traffic-analysis-discovery.jpeg)
*Caption: Centralized network-wide blocking of malicious domains at the router boundary to secure all connected devices.*

## 6. Professional Impact

This project demonstrates a Defense-in-Depth mindset. By combining local system-level modifications with centralized network-wide filtering, I ensured that no single point of failure would compromise the environment. I successfully neutralized communication channels for potential data exfiltration and confirmed the effectiveness of the remediation through continuous monitoring.

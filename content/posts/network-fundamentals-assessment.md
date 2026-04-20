+++
date = '2025-07-01T10:00:00+01:00'
draft = false
weight = 300
title = 'Network Security Fundamentals and Threat Assessment'
categories = ["Network & Infrastructure Security"]
case_id = "THREAT-ASSESS-2025"
vulnerability_class = "Diverse Attack Surface"
tools = ["Firewalls", "VPNs", "Encryption", "SIEM"]

tags = ["Network Security", "Risk Management", "CIA Triad", "Defense-in-Depth"]
[cover]
image = "images/network-fundamentals-assessment-discovery.jpeg"

+++

**Objective:** To conduct a comprehensive study of network threat vectors and security controls to establish a foundational defense strategy for organizational environments.

<!--more-->

## 1. The Vulnerability: Diverse Attack Surface

Modern networks face a broad spectrum of vulnerabilities ranging from ARP Poisoning and Man-in-the-Middle (MITM) attacks to Social Engineering and Zero-Day exploits. Without a structured understanding of these threats, security measures often remain reactive rather than proactive, leaving critical assets exposed to reconnaissance and unauthorized access.

## 2. Technical Execution: Layered Security Framework

I performed a deep-dive analysis into network security measures, categorizing them into physical, technical, and administrative layers. This involved studying the specific functions of various security tools—such as Stateful Inspection Firewalls, VPNs, and Network Segmentation—to determine how they collectively defend against the identified threat landscape.

| Component | Value | Purpose |
| :--- | :--- | :--- |
| **Firewalls** | Packet Filtering & WAF | Monitors and controls traffic based on predefined security rules. |
| **Encryption** | AES / RSA / ECC | Secures data at rest and in transit via cryptographic protocols. |
| **Access Control** | NAC / Zero Trust | Validates users/devices and enforces the principle of least privilege. |
| **Monitoring** | SIEM / Behavioral Analytics | Aggregates logs and uses AI to detect anomalies indicating threats. |

## 3. Execution Workflow

1. **Threat Research:** Analyzed 15 distinct network threats, including Buffer Overflows, DDoS attacks, and Phishing, to understand their operational mechanics.
2. **Security Measure Mapping:** Evaluated 18 different security controls and tools, determining their specific roles in protecting system integrity and data.
3. **Environment Setup:** Applied these foundational concepts to a personal PC and home network setup to monitor traffic and implement local firewall rules.
4. **Outcome Evaluation:** Verified the effectiveness of these measures by differentiating between safe and suspicious traffic patterns using live capture tools.

## 4. Key Commands
```powershell
# Commands used to audit local firewall and network configuration
# Checking the status of Windows Defender Firewall
netsh advfirewall show allprofiles

# Listing active network connections and associated processes
netstat -ab
```

## 5. Evidence of Work

![Discovery](/images/network-fundamentals-assessment-discovery.jpeg)
*Caption: Discovery phase showing the comprehensive classification and description of modern network attack vectors.*

![Results](/images/network-fundamentals-assessment-results.jpeg)
*Caption: Results/Impact phase showing the structured framework of defensive tools and concepts required to secure a network.*

## 6. Professional Impact

This project demonstrates a rigorous academic and practical grasp of System Integrity and organizational defense. By successfully mapping threats to specific security controls, I have established a methodology for building a robust security posture that addresses the CIA Triad (Confidentiality, Integrity, and Availability). This structured approach is vital for remediation planning, as it allows for the deployment of targeted defenses like Segmentation and Encryption to mitigate high-risk vulnerabilities.

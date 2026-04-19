+++
date = '2025-11-15T10:00:00+01:00'
draft = false
title = 'Network Traffic Baselining and Anomaly Detection'
categories = ["Network Security & Infrastructure"]
case_id = "ANOMALY-DETECT-2025"
vulnerability_class = "Obfuscated Network Activity (CWE-1021)"
tools = ["Wireshark", "DNS", "TLS", "Anomaly Detection"]

[cover]
image = "images/network-baselining-anomaly-discovery.jpeg"

tags = ["Wireshark", "Network Monitoring", "Indicators of Compromise", "Traffic Analysis"]
+++

**Objective:** To establish a behavioral baseline for legitimate network traffic and use protocol analysis to isolate potential security threats.

<!--more-->

## 1. The Vulnerability: Obfuscated Network Activity (CWE-1021)

A significant vulnerability in modern networks is the inability to distinguish between legitimate background services and malicious traffic. Attackers often use Domain Spoofing and typosquatting (e.g., `googleagmanger.com` instead of `googlemanager.com`) to hide their presence. Without a documented baseline of normal traffic, these subtle anomalies often go unnoticed, allowing malware to maintain persistence and communicate with external servers.

## 2. Technical Execution: Protocol Interrogation

I conducted a deep-packet analysis using Wireshark to categorize traffic by protocol and destination. By filtering for DNS and HTTPS traffic, I was able to verify the legitimacy of routine queries to known services like Google and Firebase while flagging high-frequency queries to unfamiliar domains.

| Component | Value | Purpose |
| :--- | :--- | :--- |
| **Analysis Tool** | Wireshark | Real-time packet capture and deep-packet inspection. |
| **Baseline Protocol** | TLSv1.2 / QUIC | Verified encrypted web communication for trusted services. |
| **Anomaly Vector** | DNS CNAME Chaining | Identified rotating IP patterns used to evade detection. |
| **Environment** | Personal/Home Network | Testing site for live monitoring and traffic differentiation. |

## 3. Execution Workflow

1. **Traffic Capture:** Initiated a live capture session in Wireshark to monitor all inbound and outbound system traffic.
2. **Behavioral Baselining:** Identified and documented safe traffic patterns from reputable services like Grammarly and Google.
3. **Anomaly Identification:** Filtered for DNS queries and identified a cluster of domains (e.g., `trasre.com`) that exhibited suspicious behavior, such as resolving through multiple IP addresses via Cloudfront and Aliyun CDNs.
4. **Impact Verification:** Determined that the identified domains were typical of rotating Command-and-Control (C2) infrastructure used for malware distribution.

## 4. Key Commands
```bash
# Filter Wireshark traffic to show only DNS queries
dns

# Filter to identify specific suspicious domain resolutions
dns.qry.name contains "aoneroom"

# Analyze TLS handshakes for version verification
tls.handshake.version == 0x0303
```

## 5. Evidence of Work

![Discovery](/images/network-baselining-anomaly-discovery.jpeg)
*Caption: Discovery phase showing the identification of suspicious DNS queries for domains like h5-static.aoneroom.com.*

![Results](/images/network-baselining-anomaly-results.jpeg)
*Caption: Results/Impact phase showing the verification of legitimate encrypted traffic (TLS/QUIC) as part of the baselining process.*

## 6. Professional Impact

This project directly addresses System Integrity by establishing the "Known Good" state of a network. By developing the ability to recognize abnormal DNS patterns and C2 communication, I provided a proactive defense that identifies compromises before data exfiltration occurs. This work demonstrates the practical value of traffic monitoring in detecting early indicators of compromise and informing a multi-layered remediation strategy.

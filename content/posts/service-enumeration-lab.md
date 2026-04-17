+++
date = '2025-08-05T10:00:00+01:00'
draft = false
title = 'Service Enumeration & Vulnerability Research'
categories = ["Binary & System Exploitation"]

[cover]
image = "images/feature-3-shell-privilege-escalation.png"

tags = ["Nmap", "Reconnaissance", "Enumeration", "Services"]
+++

**Objective:** To perform deep-packet inspection and service fingerprinting on a target host to identify exploitable entry points within the infrastructure.

<!--more-->

## 1. Execution Methodology: The "3-Phase Scan"

A professional scan isn't just one command; it’s a tiered approach to avoid missing hidden services or misidentifying versions.

- **Phase 1: Discovery (Ping Sweep)** – Confirming the host is alive.
- **Phase 2: Port Scanning (SYN Scan)** – Identifying all 65,535 possible TCP "doors."
- **Phase 3: Service Fingerprinting (-sV)** – Forcing the target to reveal exactly what software and version is running on the open ports.

## 2. Technical Findings (Port 21 Analysis)

During the enumeration of `192.168.56.101`, I identified a critical exposure on the File Transfer Protocol (FTP) service.

| Attribute | Value |
| :--- | :--- |
| **Port / Protocol** | 21 / TCP |
| **State** | Open |
| **Service Name** | ftp |
| **Version Identified** | vsftpd 2.3.4 |
| **Risk Level** | Critical (Backdoor Vulnerability) |

## 3. Vulnerability Research

Upon identifying vsftpd 2.3.4, I performed an offline vulnerability search using the Exploit Database (Exploit-DB) via the `searchsploit` utility on Kali Linux.

- **Finding:** The specific version of vsftpd (2.3.4) is documented as containing a malicious backdoor added to the source code by an unauthorized party.
- **Trigger:** Sending a `:)` smiley face in the username triggers the opening of a shell on Port 6200.

## 4. Key Commands & Tools

- `nmap -T4 -A -v 192.168.56.101`: An aggressive scan to pull OS details, service versions, and run default scripts.
- `nmap -p 21 --script ftp-vsftpd-backdoor 192.168.56.101`: A targeted script scan to confirm the existence of the specific backdoor before launching an exploit.
- `searchsploit vsftpd 2.3.4`: Querying the local Exploit-DB for known vulnerabilities.

![Screenshot](/images/project2_nmap_scan.png)
*Caption: Service version detection confirming the presence of the backdoored vsftpd 2.3.4 service.*


![Screenshot](/images/project2_searchsploit.png)
*Caption: Utilizing SearchSploit to map the identified service version to a known critical vulnerability (CVE-2011-2523).*


## 5. Professional Impact

By utilizing Service Fingerprinting, I successfully narrowed down the attack surface from dozens of open ports to a single, high-probability exploit. This phase demonstrates a logical transition from "Information Gathering" to "Vulnerability Assessment," ensuring that the subsequent exploitation phase is precise and effective.

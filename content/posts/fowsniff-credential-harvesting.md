+++
date = '2026-04-17T10:00:00+01:00'
draft = false
weight = 200
title = 'Fowsniff — Credential Harvesting & Password Cracking'
categories = ["Penetration Testing & Vulnerability Assessment"]
case_id = "FOWSNIFF-PASS-2026"
vulnerability_class = "Information Disclosure (Credential Leak)"
tools = ["Nmap", "Metasploit", "John the Ripper", "Hydra"]

[cover]
image = "images/feature-fowsniff.png"

tags = ["Password Cracking", "Credential Harvesting", "Information Disclosure", "John the Ripper"]
+++

**Objective:** To exfiltrate and crack leaked credentials from unencrypted data sources to perform authenticated service attacks.

<!--more-->

## 1. The Vulnerability: Information Disclosure (Credential Leak)

The target was found to have a critical information disclosure vulnerability where internal communication logs (emails) were accessible via unauthenticated network shares. These logs contained a dump of MD5-hashed credentials. This represents a fatal breakdown of Confidentiality, as any network participant could harvest the identity store without direct exploitation of a service flaw.

## 2. Technical Execution: Brute Force & Cryptanalysis

I utilized John the Ripper (JtR) to perform an offline dictionary attack against the exfiltrated MD5 hashes. Once recovered, these plaintext credentials were used as the primary authentication vector for secondary services (POP3/IMAP), demonstrating the cascading impact of a single data leak on organizational security.

| Component | Value | Purpose |
| :--- | :--- | :--- |
| **Data Source** | SMB Share (Unauthenticated) | The source of the leaked credential dump. |
| **Hash Type** | MD5 | The insecure algorithm used for initial password storage. |
| **Cracking Tool** | John the Ripper | Used for offline password recovery. |
| **Attack Pivot** | Hydra (POP3 Brute Force) | Utilizing recovered passwords for service access. |

## 3. Execution Workflow

1. **Information Gathering:** Scanned for Samba shares using Nmap and exfiltrated email logs from the `public` directory.
2. **Credential Extraction:** Cleaned the exfiltrated data to isolate user-hash pairs for systematic cracking.
3. **Cryptanalysis:** Used John the Ripper to successfully recover plaintext passwords from the MD5 hashes.
4. **Service Hijacking:** Utilized the recovered credentials in conjunction with Hydra to gain administrative access to the target’s email infrastructure (POP3).

## 4. Key Commands
```bash
# Using John the Ripper to crack the exfiltrated MD5 hashes
john --format=Raw-MD5 --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt

# Using Hydra to verify recovered credentials against the POP3 service
hydra -L users.txt -P cracked_passes.txt 10.10.x.x pop3
```

## 5. Evidence of Work

![Discovery](/images/fowsniff-pop3.png)
*Caption: Discovery phase showing the unauthenticated access to sensitive internal email logs.*

![Results](/images/fowsniff-cracking.png)
*Caption: Results/Impact phase showing the successful recovery of multiple plaintext passwords via John the Ripper.*

## 6. Professional Impact

This project demonstrates the "Identity Lifecycle" of an attack. I proved that a simple configuration error (open SMB share) leads directly to a total account takeover across separate services (email). To remediate this, I recommended that the organization decommission unencrypted shares and transition to bcrypt or Argon2 for password hashing, ensuring that even if data is leaked, it cannot be readily decrypted by an adversary.

+++
date = '2026-03-26T10:00:00+01:00'
draft = false
weight = 200
title = 'Mr. Robot — Web Exploitation & System Compromise'
categories = ["Penetration Testing & Vulnerability Assessment"]
case_id = "MRROBOT-WEB-2026"
vulnerability_class = "Improper Input Validation & Privilege Escalation"
tools = ["WPScan", "Nmap", "John the Ripper", "Nmap Privilege Escalation"]

tags = ["WordPress Security", "CTF", "Privilege Escalation", "Reconnaissance"]
[cover]
image = "images/feature-mrrobot.png"

+++

**Objective:** To demonstrate a full-stack compromise, from website reconnaissance and credential harvesting to gaining root-level access on a Linux server.

<!--more-->

## 1. The Vulnerability: Web-to-System Access Chain

The target platform was found to be running a vulnerable WordPress instance with an improperly configured administrative login. By exploiting a combination of Information Disclosure (exposed `robots.txt` and dictionary files) and brute force, I gained initial access to the web backend, providing a gateway for further system-level pivoting.

## 2. Technical Execution: Multi-Layered Exploitation

I conducted a tiered attack, beginning with aggressive web reconnaissance using `gobuster` and `wpscan`. After gaining a web shell, I exfiltrated password hashes for local users and utilized an insecure SUID bit on the `nmap` binary to escalate privileges to root.

| Component | Value | Purpose |
| :--- | :--- | :--- |
| **Reconnaissance** | Gobuster / WPScan | Identifying hidden directories and CMS vulnerabilities. |
| **Exploit Vector** | WordPress Brute Force | Gaining initial administrative access to the web interface. |
| **Credential Theft** | MD5 Hash Cracking | Recovering local user passwords from the system files. |
| **Privilege Esc** | Nmap SUID (Interactive) | Bypassing local security to gain a root shell. |

## 3. Execution Workflow

1. **Information Gathering:** Identified critical system information and hideouts in the `robots.txt` file, including a hidden wordlist and a cryptographic key.
2. **Web Hijacking:** Performed an automated brute force attack against the WordPress login using the exfiltrated wordlist to gain a web shell.
3. **Lateral Movement:** Located an encrypted MD5 hash for the user `robot` and recovered the plaintext password via John the Ripper.
4. **Root Escalation:** Identified that `nmap` was configured with the SUID bit, allowing for the execution of an interactive nmap session to spawn a root shell.

## 4. Key Commands
```bash
# Brute forcing WordPress login with a customized wordlist
wpscan --url http://10.10.x.x --passwords wordlist.txt --usernames Elliot

# Escalating privileges via Nmap SUID bit
nmap --interactive
!sh
```

## 5. Evidence of Work

![Discovery](/images/mrrobot-wpscan.png)
*Caption: Discovery phase identifying the WordPress administrative login and user enumeration.*

![Results](/images/feature-mrrobot.png)
*Caption: Results/Impact phase showing the successful use of Nmap's interactive mode to gain a root shell.*

## 6. Professional Impact

This project highlights the "Compromise Chain" where a single web-level failure (weak password) leads to total system takeover. By achieving root access via an insecure SUID binary, I proved that local configuration errors are as dangerous as external vulnerabilities. I recommended that the organization enforce strong password policies for CMS platforms and strictly adhere to the Principle of Least Privilege by removing unnecessary SUID bits from system binaries.

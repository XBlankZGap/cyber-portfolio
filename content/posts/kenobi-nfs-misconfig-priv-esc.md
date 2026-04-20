+++
date = '2026-03-25T10:00:00+01:00'
draft = false
weight = 200
title = 'Kenobi — Exploiting NFS Misconfigurations & Privilege Escalation'
categories = ["Penetration Testing & Vulnerability Assessment"]
case_id = "KENOBI-LINUX-2026"
vulnerability_class = "Insecure Service Configuration (NFS/ProFTPd)"
tools = ["Nmap", "Netcat", "Samba", "SUID"]

tags = ["Linux Security", "Privilege Escalation", "NFS", "ProFTPd"]
[cover]
image = "images/feature-kenobi.png"

+++

**Objective:** To demonstrate the use of insecure service configurations and SUID binaries to perform cross-protocol exploitation and gain root access.

<!--more-->

## 1. The Vulnerability: Insecure Service Configuration

This target exhibited multiple critical misconfigurations, including an insecure Network File System (NFS) share and a vulnerable ProFTPd service (v1.3.5) susceptible to arbitrary file copy vulnerabilities. This allows an attacker to manipulate server-side files via unauthenticated protocol requests, bypassing standard Access Control mechanisms.

## 2. Technical Execution: Service Chaining

I executed a multi-step attack chain, leveraging Samba for initial information gathering, ProFTPd to exfiltrate private SSH keys to an accessible NFS share, and finally identifying a misconfigured SUID bit on the `/usr/bin/menu` binary to escalate privileges to root.

| Component | Value | Purpose |
| :--- | :--- | :--- |
| **Initial Recon** | Nmap --script nfs-showmount | Identifying accessible network file shares. |
| **Exploit Vector** | ProFTPd SITE CPFR/CPTO | Copying sensitive files (id_rsa) to the NFS share. |
| **Auth Vector** | SSH (Private Key) | Gaining initial shell access as a regular user. |
| **Privilege Esc** | SUID (Path Hijacking) | Exploiting misconfigured binaries to gain root. |

## 3. Execution Workflow

1. **Enumeration:** Scanned for Samba shares using Nmap and listed NFS mount points to identify the exploitable infrastructure.
2. **File Manipulation:** Exploited the ProFTPd `SITE CPFR` and `SITE CPTO` commands to copy the user’s private SSH key to the mounted NFS directory.
3. **Initial Access:** Mounted the NFS share locally, retrieved the SSH key, and established a shell session via SSH.
4. **Root Escalation:** Identified an SUID binary that executed a system command (curl) without a full path, allowing for Path Hijacking to spawn a root shell.

## 4. Key Commands
```bash
# Mounting the insecure NFS share locally
mount 10.10.x.x:/var/tmp /mnt/kenobi_nfs

# Exploiting the ProFTPd file copy vulnerability
SITE CPFR /home/kenobi/.ssh/id_rsa
SITE CPTO /var/tmp/id_rsa
```

## 5. Evidence of Work

![Discovery](/images/kenobi-nfs.png)
*Caption: Identification of unauthenticated NFS shares and vulnerable Samba services.*

![Results](/images/kenobi-root.png)
*Caption: Successful privilege escalation showing root access gained through SUID binary exploitation.*

## 6. Professional Impact

This project highlights the risk of "Service Chaining," where multiple minor misconfigurations lead to a total system compromise. By successfully escalating to root, I proved that System Integrity is only as strong as its weakest service. I recommended that the organization enforce strict protocol-specific access controls and regularly audit system binaries for insecure SUID bit configurations.

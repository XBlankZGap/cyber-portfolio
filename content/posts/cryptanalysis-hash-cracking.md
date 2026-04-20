+++
date = '2025-09-25T10:00:00+01:00'
draft = false
weight = 500
title = 'Offline Cryptanalysis & Password Recovery'
categories = ["DevSecOps & Cryptography"]

tags = ["Cryptography", "Password Cracking", "John the Ripper", "Hashes"]
[cover]
image = "images/project5_jtr_cracking.png"

+++

**Objective:** To utilize high-performance cracking tools to perform a dictionary attack against stolen MD5 hashes, successfully recovering plaintext credentials.

<!--more-->

## 1. The Science of Hashing

Modern security relies on "one-way" cryptographic hashes. However, when a password is weak (like `msfadmin`), an attacker can use Brute Force or Dictionary Attacks to pre-calculate hashes and find a match. For this project, I targeted the `msfadmin` user, whose hash was exfiltrated during the previous post-exploitation phase.

## 2. Tool Selection: John the Ripper

I utilized John the Ripper (JtR), an industry-standard password security auditing tool. JtR was selected for its ability to automatically detect the hashing algorithm (MD5crypt) and its efficiency in multi-threaded processing.

| Component | Value |
| :--- | :--- |
| **Target User** | `msfadmin` |
| **Hash Type** | md5crypt (Identified by `$1$` prefix) |
| **Attack Method** | Single Crack & Wordlist Masking |
| **Cracking Speed** | < 1 Second (Immediate Recovery) |

## 3. Execution Workflow

1. **Loot Preparation:** Created a localized text file (`hash_to_crack.txt`) containing the raw exfiltrated hash string from the `/etc/shadow` file.
2. **Algorithm Detection:** Ran John the Ripper, which successfully identified the `$1$` signature as an MD5-based Linux crypt hash.
3. **The Attack:** Initiated the cracking process. Due to the weak nature of the password, the tool achieved a "collision" (a match) almost instantly.
4. **Credential Verification:** Used the `--show` flag to display the recovered plaintext password.

## 4. Key Commands Used

- `nano hash_to_crack.txt`: To manually stage the stolen hash for the cracking tool.
- `john hash_to_crack.txt`: To launch the automated cracking engine.
- `john --show hash_to_crack.txt`: To reveal the decrypted results in the terminal.

![Screenshot](/images/project5_jtr_cracking.png)
*Caption: Utilizing John the Ripper to perform an automated dictionary attack against the MD5crypt hash.*


![Screenshot](/images/project5_jtr_plaintext.png)
*Caption: Successful recovery of the administrative plaintext password, proving a critical failure in the target's credential policy.*


## 5. Professional Impact

This activity highlights the "human element" of cybersecurity. By cracking the password in less than a second, I demonstrated that Infrastructure Security is irrelevant if Identity Security is weak. This project proves my proficiency in handling "Loot" and converting raw data into actionable intelligence that could be used for further lateral movement or authenticated access.

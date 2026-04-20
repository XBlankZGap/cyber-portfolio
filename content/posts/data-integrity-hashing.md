+++
date = '2026-01-10T10:00:00+01:00'
draft = false
weight = 500
title = 'Data Integrity Verification via Cryptographic Hashing'
categories = ["DevSecOps & Cryptography"]
case_id = "HASHING-INTEGRITY-2026"
vulnerability_class = "Data Tampering & Plaintext Credentials"
tools = ["SHA-256", "MD5", "sha256sum", "Integrity Check"]

[cover]
image = "images/data-integrity-hashing-discovery.png"

tags = ["Hashing", "Data Integrity", "SHA-256", "Password Security"]
+++

**Objective:** To utilize one-way hashing algorithms to verify data authenticity and secure credential storage.

<!--more-->

## 1. The Vulnerability: Data Tampering & Plaintext Credentials

If data is stored or transmitted without integrity checks, it can be altered undetected, leading to a loss of Authenticity. Additionally, storing user passwords in plaintext exposes the organization to catastrophic identity theft in the event of a database breach.

## 2. Technical Execution: Hash Function Deployment

I implemented cryptographic hashing to convert variable-length data into fixed-length "fingerprints." Unlike encryption, these functions are one-way, making them ideal for verifying that files have not been modified and for securely storing password hashes rather than original values.

| Component | Value | Purpose |
| :--- | :--- | :--- |
| **Hash Function** | SHA-256 / MD5 | Generates a unique, fixed-length string from data. |
| **Integrity Check** | Checksum Verification | Detects if data was altered during storage or transit. |
| **Auth Security** | Password Hashing | Prevents original passwords from being recovered from a DB. |

## 3. Execution Workflow

1. **Integrity Baselining:** Generated initial hashes for critical system configuration files to serve as an "unaltered" reference. 
2. **Detection Logic:** Automated a periodic comparison of current file hashes against the baseline to detect unauthorized changes. 
3. **Secure Storage:** Configured the application backend to hash user passwords immediately upon registration. 
4. **Verification:** Implemented login logic that hashes the user's attempt and compares it to the stored hash, ensuring Authentication without exposing the secret. 

## 4. Key Commands
```bash
# Example: Generating a SHA-256 hash to verify a file's integrity
sha256sum sensitive_data.zip

# Example: Verifying hashes against a recorded list
sha256sum -c integrity_manifest.txt
```

## 5. Evidence of Work

![Discovery](/images/data-integrity-hashing-discovery.png)
*Caption: Discovery phase showing the functional difference between reversible encryption and one-way hashing.*

![Discovery](/images/data-integrity-hashing-discovery.png)
*Caption: Results/Impact phase showing the verification process where altered data is detected through hash mismatches.*

## 6. Professional Impact

This project ensures Data Integrity, confirming that information remains unaltered without detection. By implementing hashing for password storage, I significantly mitigated the risk of a secondary credential breach, preserving Authentication protocols even if the underlying data store is compromised.

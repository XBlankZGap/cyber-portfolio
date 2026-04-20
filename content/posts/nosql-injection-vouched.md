+++
date = '2026-04-18T10:00:00+01:00'
draft = false
title = 'NoSQL Injection & Database Poisoning (Vouched Application)'
categories = ["Web Application Pentesting"]
case_id = "NOSQL-INJECT-2026"
vulnerability_class = "Improper Neutralization of NoSQL Commands (CWE-943)"
tools = ["Postman", "MongoDB", "Express.js", "Bcrypt"]

[cover]
image = "images/nosql-vulnerability.png"

tags = ["NoSQL Injection", "MongoDB", "API Security", "Vouched"]
+++

**Objective:** To identify and exploit NoSQL injection vulnerabilities within the "Vouched" application to bypass authentication and extract sensitive user data.

<!--more-->

## 1. The Vulnerability: NoSQL Command Neutralization (CWE-943)

NoSQL injection occurs when an application fails to properly sanitize user input before using it in a database query. In document-oriented databases like MongoDB, this allows an attacker to inject logical operators (e.g., `$gt`, `$ne`) to manipulate the query logic, leading to unauthorized data access or authentication bypass.

## 2. Technical Execution: Logic Manipulation

Using Postman, I crafted malicious JSON payloads targeting the authentication and search endpoints of the Vouched application. By replacing standard string inputs with MongoDB operator objects, I successfully manipulated the database logic to return records that should have been restricted, effectively bypassing Bcrypt-hashed password checks.

| Component | Value | Purpose |
| :--- | :--- | :--- |
| **Attack Vector** | JSON Payload Injection | Injecting MongoDB operators into API requests. |
| **Target Endpoint** | `/api/v1/login` | Attempting to bypass password verification. |
| **Impact** | Authentication Bypass | Gaining access to any user account without a password. |
| **Remediation** | Schema Validation | Implementing strict typing for all incoming data. |

## 3. Execution Workflow

1. **Endpoint Enumeration:** Used Postman to identify API endpoints that accept JSON input for database queries.
2. **Operator Testing:** Injected basic logical operators (e.g., `{"$ne": null}`) to test if the database would return unintended results.
3. **Authentication Bypass:** Crafted a login request where the password field was replaced with a "not equal" operator, allowing login as any user whose username was known.
4. **Data Exfiltration:** Leveraged the injection vulnerability on search endpoints to dump the entire user collection.

## 4. Exploit Payload (JSON)
```json
// Malicious Login Payload
{
  "username": "admin",
  "password": { "$ne": "wrong_password" }
}
// This bypasses the Bcrypt check because the query returns the first user 
// where the password is NOT "wrong_password".
```

## 5. Evidence of Work

![NoSQL Vulnerability](/images/nosql-vulnerability.png)
*Caption: Initial discovery phase showing the identification of NoSQL-vulnerable endpoints in the Vouched application.*

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 40px 0;">
    <div class="terminal-window">
        <div class="terminal-header"><div class="dot red"></div><div class="dot yellow"></div><div class="dot green"></div></div>
        <div class="terminal-img-container"><img src="/images/nosql-postman-exploit.png" alt="Postman Exploit"></div>
    </div>
    <div class="terminal-window">
        <div class="terminal-header"><div class="dot red"></div><div class="dot yellow"></div><div class="dot green"></div></div>
        <div class="terminal-img-container"><img src="/images/nosql-audit-config.png" alt="Audit Config"></div>
    </div>
</div>
*Caption: Successful authentication bypass via Postman (Left) and the subsequent database audit configuration analysis (Right).*

## 6. Professional Impact

This project highlights a critical oversight in modern web development. While Bcrypt provides strong hashing, it cannot protect against logic-level vulnerabilities if the query itself is compromised. To remediate this, I recommended the implementation of strict Mongoose schemas and the use of query sanitizers to ensure that user input is never interpreted as a database operator.

+++
date = '2025-12-15T10:00:00+01:00'
draft = false
title = 'Insecure Direct Object Reference (IDOR) & Path Traversal Discovery'
categories = ["Web Application Pentesting"]
case_id = "PATH-TRAVERSAL-2025"
vulnerability_class = "Path Traversal (CWE-22)"
tools = ["OWASP ZAP", "WebGoat", "Active Scanning"]

[cover]
image = "images/idor-path-traversal-discovery-discovery.jpeg"

tags = ["IDOR", "Path Traversal", "Vulnerability Discovery", "Web Security"]
+++

**Objective:** To identify and verify directory traversal vulnerabilities that allow unauthorized access to sensitive system files.

<!--more-->

## 1. The Vulnerability: Path Traversal (CWE-22)

The web application was found to be vulnerable to Path Traversal (also known as Directory Traversal) because it failed to properly sanitize user-supplied input used to reference files on the server. This flaw allows an attacker to use special characters, such as `../`, to break out of the intended web root directory and access restricted files or directories elsewhere on the file system.

## 2. Technical Execution: Resource Interrogation

I utilized OWASP ZAP to identify parameters susceptible to path manipulation. By injecting traversal sequences into the `column` parameter of the target URL, I observed the application's response to determine if it would disclose file paths or system-level error messages.

| Component | Value | Purpose |
| :--- | :--- | :--- |
| **Vulnerable Parameter** | column | The input vector used for path manipulation. |
| **Risk Level** | High | Potential for full system file disclosure. |
| **Detection Method** | Active Scanning | Automated probing of parameters for traversal flaws. |
| **Tool** | OWASP ZAP | Facilitates the identification of insecure file referencing. |

## 3. Execution Workflow

1. **Automated Reconnaissance:** Initiated an Active Scan within OWASP ZAP to systematically test the application's URL parameters for traversal vulnerabilities.
2. **Alert Analysis:** Flagged a "Path Traversal" alert which indicated that the application was improperly handling input in the `column` parameter.
3. **Payload Verification:** Analyzed the attack vector to confirm that the technique could potentially reach directories residing outside the web primary folder.
4. **Context Evaluation:** Noted the request URLs and parameters where the vulnerabilities were flagged to determine the scope of the exposure.

## 4. Key Commands
```bash
# Example of a traversal payload identified during the scan
# This attempts to move up the directory tree to reach system files
../../../../etc/passwd

# The targeted URL identified by ZAP
http://localhost:8080/WebGoat/SqlInjectionMitigations/servers?column=..%2F..%2F
```

## 5. Evidence of Work

![Discovery](/images/idor-path-traversal-discovery-discovery.jpeg)
*Caption: Identification of the Path Traversal alert and the vulnerable parameter in OWASP ZAP.*

![Results](/images/idor-path-traversal-discovery-results.jpeg)
*Caption: Results/Impact phase showing the technical description of the attack and the input vector (URL Query String) identified by the tool.*

## 6. Professional Impact

This project highlights a critical risk to Data Confidentiality and System Integrity, as an attacker could potentially read sensitive configuration files or credentials stored on the server. To remediate this, I recommended that the application validate user input against a known "allow-list" of expected values rather than relying on sanitizing malicious sequences. Furthermore, I advised ensuring that the application process runs with the least privilege necessary to prevent access to sensitive operating system files.

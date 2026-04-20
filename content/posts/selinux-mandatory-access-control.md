+++
date = '2026-01-15T10:00:00+01:00'
draft = false
weight = 500
title = 'Mandatory Access Control (MAC) using SELinux'
categories = ["DevSecOps & Cryptography"]
case_id = "MAC-SELINUX-2026"
vulnerability_class = "Excessive Privilege & Service Exploitation"
tools = ["SELinux", "audit2allow", "getenforce", "audit log"]

tags = ["SELinux", "MAC", "Kernel Security", "Least Privilege"]
[cover]
image = "images/selinux-mandatory-access-control-discovery.jpeg"

+++

**Objective:** To enforce strict security policies at the kernel level, preventing unauthorized resource access by compromised services.

<!--more-->

## 1. The Vulnerability: Excessive Privilege & Service Exploitation

Traditional Linux permissions (Discretionary Access Control) are often insufficient if a root-level service is compromised. Without Mandatory Access Control, a compromised web server could potentially access sensitive user home directories or system configuration files.

## 2. Technical Execution: SELinux Policy Enforcement

I deployed Security-Enhanced Linux (SELinux) to enforce granular security policies on the host system. By managing SELinux modes and rules, I ensured that even "root" users or services were restricted to the minimum resources required for their specific function.

| Component | Value | Purpose |
| :--- | :--- | :--- |
| **SELinux Mode** | Enforcing | Actively blocks and logs all policy violations. |
| **Policy Type** | Targeted | Restricts specific network services while allowing normal user activity. |
| **Diagnostic Tool** | audit2allow | Analyzes logs to resolve policy-based service issues. |

## 3. Execution Workflow

1. **Mode Verification:** Evaluated current system posture using `getenforce` and transitioned the system to Enforcing mode. 
2. **Policy Configuration:** Applied specific rules to allow web services (e.g., Apache/Nginx) to access only designated web root folders. 
3. **Violation Analysis:** Monitored system logs to identify blocked actions that indicated either an attack or a misconfigured policy. 
4. **Remediation:** Utilized diagnostic tools to generate and apply custom policy modules to allow legitimate service operations. 

## 4. Key Commands
```bash
# Example: Checking the current SELinux enforcement status
sestatus

# Example: Troubleshooting a blocked service by searching the audit log
grep "denied" /var/log/audit/audit.log | audit2allow -M my_service_fix
```

## 5. Evidence of Work

![Discovery](/images/selinux-mandatory-access-control-discovery.jpeg)
*Caption: Discovery phase showing the mandatory access control architecture and mode descriptions.*

![Results](/images/selinux-mandatory-access-control-results.jpeg)
*Caption: Results/Impact phase demonstrating the analysis of logs and the resolution of policy violations for critical services.*

## 6. Professional Impact

Implementing SELinux provides a vital layer of defense for System Integrity. By enforcing a "Least Privilege" model at the kernel level, I ensured that even if a service is exploited, the damage is contained within its predefined policy. This significantly reduces the organization's attack surface and protects sensitive OS resources from unauthorized access.

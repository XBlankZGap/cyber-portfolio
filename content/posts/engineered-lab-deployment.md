+++
date = '2025-07-02T10:00:00+01:00'
draft = true
title = 'Engineered Security Lab Deployment & Troubleshooting'
categories = ["Security Operations & Engineering"]
case_id = "LAB-DEPLOY-2025"
vulnerability_class = "Environment Misconfiguration"
tools = ["Docker", "Java Runtime", "OWASP ZAP", "Windows 11"]

[cover]
image = "images/feature-engineered-lab-deployment.png"

tags = ["Lab Setup", "Troubleshooting", "Docker", "Security Engineering"]
+++

**Objective:** To design, configure, and maintain a virtualized security testing environment for controlled vulnerability assessment.

<!--more-->

## 1. The Vulnerability: Environment Misconfiguration

An insecure or improperly configured testing environment can lead to "false negatives" during scans or unintended exposure of the host system. During the deployment of the WebGoat and OWASP ZAP lab, I encountered several configuration flaws—including Proxy Interception Failures and Container Port Conflicts—that mirrored the real-world challenges a security professional faces when setting up enterprise monitoring tools.

## 2. Technical Execution: Lab Orchestration

I engineered a local security lab using a Windows 11 host, deploying the WebGoat microservices-based application and the OWASP ZAP proxy. I implemented a manual proxy configuration to ensure all browser-based traffic was successfully intercepted for deep-packet analysis.

| Component | Value | Purpose |
| :--- | :--- | :--- |
| **Virtualization** | Docker / Java Runtime | Used to containerize the vulnerable application. |
| **Proxy Gateway** | OWASP ZAP (8080) | Man-in-the-middle node for traffic inspection. |
| **Host System** | Windows 11 | The primary OS for security testing and documentation. |
| **Certificate Mgmt** | ZAP CA Certificate | Installed to facilitate HTTPS traffic interception. |

## 3. Execution Workflow

1. **System Initialization:** Verified Java and Docker prerequisites and launched the WebGoat server via the Command Line Interface (CLI).
2. **Network Bridge Configuration:** Manually routed browser traffic through localhost:8080 to bridge the gap between the application and the security analyzer.
3. **Advanced Troubleshooting:** Resolved port 8080 conflicts by reviewing Docker logs and ensuring no other services were competing for the gateway.
4. **Certificate Trust Establishment:** Imported the ZAP Root CA certificate into the browser's trusted store to bypass SSL/TLS certificate warnings.

## 4. Key Commands
```powershell
# Launching the secure lab environment
java -jar webgoat-2025.3.jar

# Troubleshooting port conflicts and inspecting container status
docker logs [container_id]
netstat -ano | findstr :8080
```

## 5. Evidence of Work

![Discovery](/images/project13_cli_init.png)
*Caption: Discovery phase showing the successful initialization of the lab environment and identification of port mapping.*

![Results](/images/project13_browser_interception.png)
*Caption: Results/Impact phase showing the successful interception of traffic, with the browser confirming it is being controlled by automated software.*

## 6. Professional Impact

This project demonstrates Operational Excellence and the ability to build a secure testing infrastructure from the ground up. By resolving complex browser-proxy interception issues and port conflicts, I proved my technical competency in the "Post-Mortem" phase of lab setup. These skills are essential for maintaining System Integrity within a Security Operations Center (SOC) or a Red Team environment, where the reliability of tools is as critical as the analysis they provide.

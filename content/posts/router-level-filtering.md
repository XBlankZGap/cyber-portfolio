+++
date = '2025-11-10T10:00:00+01:00'
draft = false
title = 'Centralized Network Security via Router-Level Filtering'
categories = ["Network Security & Infrastructure"]
case_id = "GATEWAY-NET-2025"
vulnerability_class = "Device-Level Mitigation Gaps"
tools = ["MTN 4G Router", "URL Filtering", "IPv4", "Firewall"]

[cover]
image = "images/feature-router-level-filtering.png"

tags = ["Network Security", "Firewall", "Gateway", "IoT Security"]
+++

**Objective:** To implement non-device-specific security controls by enforcing domain blocking at the network gateway.

<!--more-->

## 1. The Vulnerability: Device-Level Mitigation Gaps

Relying solely on host-based security measures (like the Windows hosts file) creates significant coverage gaps for non-configurable devices. Mobile phones, tablets, and IoT hardware often lack accessible system files for manual domain blocking. This leaves a portion of the network exposed to Command-and-Control (C2) communications and phishing traffic if a threat originates from or targets these "unmanaged" devices.

## 2. Technical Execution: Gateway URL Filtering

I utilized the MTN 4G Router Admin Panel to establish a centralized defense layer. By configuring IPv4 URL Keyword Filtering, I instructed the router to intercept and drop traffic destined for the suspicious domains identified during the Wireshark analysis phase. This method ensures that the security policy is enforced at the network boundary, regardless of the operating system or configuration of the connected endpoint.

| Component | Value | Purpose |
| :--- | :--- | :--- |
| **Hardware** | MTN 4G Router | The central gateway for all local network traffic. |
| **Control Logic** | URL Keyword Filtering | Blocks traffic based on domain strings. |
| **Protocol** | IPv4 | The addressing scheme used for the filtering rules. |
| **Coverage** | Network-Wide | Protects all connected Windows, Mobile, and IoT devices. |

## 3. Execution Workflow

1. **Perimeter Analysis:** Identified that blocking domains on a single PC did not prevent the same malicious domains from being accessed by mobile devices on the same Wi-Fi.
2. **Gateway Access:** Authenticated into the home router's administrative interface to access the firewall and security settings.
3. **Rule Configuration:** Added identified malicious strings (e.g., `aoneroom.com`, `givefreely.com`, `trasre.com`) to the URL Filtering List.
4. **Validation:** Verified that the router successfully blocked requests to these domains from multiple device types, confirming a robust, centralized defense.

## 4. Key Logic
```bash
# Logical Rule applied via GUI:
IF (HTTP_REQUEST_URL CONTAINS "malicious_domain.com") THEN (ACTION = BLOCK/DROP)
```

## 5. Evidence of Work

![Discovery](/images/project6_router_interface.png)
*Caption: Discovery phase showing the MTN router firewall interface and the initial empty filtering rules before configuration.*

![Results](/images/project6_filtering_active.png)
*Caption: Results phase showing the active URL Filtering List with ten suspicious domains successfully blocked at the network level.*

## 6. Professional Impact

This project demonstrates an understanding of Defense-in-Depth and the importance of securing the network perimeter. By moving the control point to the router, I protected the System Integrity of the entire local environment, significantly reducing the attack surface. This proactive approach mitigates the risk of lateral movement and ensures a consistent security posture across a diverse range of hardware.

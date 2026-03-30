+++
date = '2026-03-20T10:00:00+01:00'
draft = false
title = 'Project 1: Defensive Lab Environment & Network Configuration'

[cover]
image = "images/feature-1-vbox-machine.png"
+++

**Objective:** To design and deploy a secure, isolated virtualization environment for controlled penetration testing and vulnerability analysis.

<!--more-->

## 1. Technical Overview

Before any testing occurs, a "sandbox" must be established. This ensures that exploits do not "leak" onto the public internet or the local home network. For this project, I utilized Oracle VirtualBox to create a private Host-Only Network.

## 2. Architecture Components

- **Attacker Machine:** Kali Linux (Rolling Edition)
- **Target Machine:** Metasploitable 2 (Linux-based vulnerable sinkhole)
- **Network Type:** Host-Only (`vboxnet0`)
- **Network Range:** `192.168.56.0/24`

## 3. Implementation Steps

1. **Interface Initialization:** I identified and activated the virtual network adapter on the Kali host to ensure a communication path to the target.
2. **Kernel Module Troubleshooting:** I resolved issues with the VirtualBox Guest Additions and networking modules using `modprobe` to ensure the virtual bridge was stable.
3. **Connectivity Verification:** Performed a bilateral ping test to confirm that the machines could "see" each other without external interference.

## 4. Key Commands Used

- `ip addr show vboxnet0`: To verify the Attacker IP (`192.168.56.1`).
- `sudo modprobe vboxnetflt`: To manually load the VirtualBox net-filter driver during a service failure.
- `ping -c 4 192.168.56.101`: To confirm the route to the target.

![Screenshot](/images/project1_network.png)
*Caption: Verification of the isolated Host-Only network interface and successful connectivity to the target environment.*


## 5. Security Reflection

Setting up a Host-Only network is a core requirement for Ethical Hacking. It demonstrates a commitment to "Safety First"—ensuring that vulnerable services (like the ones on Metasploitable) are never exposed to the actual internet where they could be hijacked by real malicious actors.

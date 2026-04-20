+++
date = '2025-08-20T10:00:00+01:00'
draft = false
weight = 400
title = 'Cross-Site Request Forgery (CSRF) via Forged Reviews'
categories = ["Application Security (AppSec)"]
case_id = "CSRF-WEB-2025"
vulnerability_class = "Missing Anti-Forgery Tokens (CWE-352)"
tools = ["OWASP ZAP", "Python", "HTML/JS", "WebGoat"]

[cover]
image = "images/csrf-forged-reviews-discovery.jpg"

tags = ["CSRF", "Session Management", "OWASP", "Auth Bypass"]
+++

**Objective:** To exploit missing request verification to perform unauthorized actions on behalf of a logged-in user.

<!--more-->

## 1. The Vulnerability: Missing Anti-Forgery Tokens (CWE-352)

A Cross-Site Request Forgery (CSRF) vulnerability was discovered on the review submission endpoint of the WebGoat application. This flaw exists because the application fails to properly validate the origin of incoming requests, allowing an attacker to trick a victim's browser into submitting a state-changing request (such as posting a review) without the user's knowledge or consent. Although a `validateReq` token was present, it did not expire quickly enough to prevent reuse in a cross-site context.

## 2. Technical Execution: Request Forgery

I used OWASP ZAP to intercept a legitimate POST request to identify the required parameters and target endpoint. I then developed a malicious HTML landing page containing a hidden form designed to auto-submit the captured parameters. By hosting this page on a local Python server, I successfully simulated an external attack where the forged request was executed as soon as the authenticated victim visited the malicious URL.

| Component | Value | Purpose |
| :--- | :--- | :--- |
| **Endpoint** | /WebGoat/csrf/review | The vulnerable review submission target. |
| **Analysis Tool** | OWASP ZAP | Used for traffic interception and parameter analysis. |
| **Exploit Tool** | VS Code / Python | Used to craft the HTML payload and host the attack. |
| **Auth Bypass** | validateReq token | Reused the captured token to validate the forged request. |

## 3. Execution Workflow

1. **Discovery:** Logged into the application and intercepted a legitimate form submission using OWASP ZAP to analyze the HTTP POST request structure.
2. **Vulnerability Analysis:** Examined the `validateReq` token and determined it was susceptible to reuse since it remained valid across the short session.
3. **Exploit Logic:** Crafted an external HTML page with a hidden form and a JavaScript `submit()` function to trigger the attack automatically.
4. **Post-Exploitation:** Hosted the malicious file using `python -m http.server` and confirmed that visiting the page successfully posted a "Hacked by CSRF!" review in the application on behalf of the user.

## 4. Key Commands
```html
<!-- Malicious CSRF Payload -->
<form id="csrfForm" action="http://localhost:8080/WebGoat/csrf/review" method="POST">
  <input type="hidden" name="reviewText" value="Hacked by CSRF!" />
  <input type="hidden" name="stars" value="1" />
  <input type="hidden" name="validateReq" value="(captured_token_here)" />
</form>
<script>document.getElementById('csrfForm').submit();</script>
```
```bash
# Hosting the exploit locally
python -m http.server 9000
```

## 5. Evidence of Work

![Discovery](/images/csrf-forged-reviews-discovery.jpg)
*Caption: OWASP ZAP flagging the absence of robust anti-CSRF tokens for the application session.*

![Results](/images/csrf-forged-reviews-results.jpeg)
*Caption: Successful submission of the forged review ("Hacked by CSRF!") without any manual user interaction.*

## 6. Professional Impact

This project demonstrates a significant risk to System Integrity and user trust, as attackers can perform unintended actions like deleting data or posting unauthorized content. To remediate this, I recommended implementing unique, per-session CSRF tokens for all state-changing operations and enforcing the SameSite cookie attribute to ensure requests only originate from the legitimate domain.

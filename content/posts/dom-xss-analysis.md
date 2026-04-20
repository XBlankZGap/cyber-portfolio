+++
date = '2025-08-15T10:00:00+01:00'
draft = false
weight = 400
title = 'DOM-Based Cross-Site Scripting (XSS) Analysis'
categories = ["Application Security (AppSec)"]
case_id = "XSS-DOM-2025"
vulnerability_class = "Unsafe DOM Manipulation (CWE-79)"
tools = ["JavaScript", "jQuery", "OWASP ZAP", "WebGoat"]

tags = ["XSS", "JavaScript", "Security Engineering", "Remediation"]
[cover]
image = "images/feature-dom-xss-analysis.jpg"

+++

**Objective:** To identify and exploit an unsafe JavaScript "sink" to execute arbitrary code in the victim's browser context.

<!--more-->

## 1. The Vulnerability: Unsafe DOM Manipulation (CWE-79)

The application is vulnerable to DOM-based Cross-Site Scripting (XSS) because it renders user-controlled input directly into the Document Object Model (DOM) without prior sanitization. Specifically, the application uses an unsafe "sink" (the `.html()` method), which allows a browser to interpret and execute any script tags or malicious event handlers passed through the URL.

## 2. Technical Execution: Client-Side Scripting

By performing a manual code review of the frontend JavaScript files, I identified a function that directly handles URL parameters for rendering page content. By crafting a URL with a malicious image-based payload, I triggered an execution event entirely within the client's browser, bypassing the need for server-side interaction.

| Component | Value | Purpose |
| :--- | :--- | :--- |
| **Vulnerable Script** | LessonContentView.js | Responsible for rendering lesson parameters. |
| **Unsafe Method** | .html(param) | The JQuery "sink" that executes HTML/JS. |
| **Attack Vector** | Fragment Identifier (#) | Used to pass the payload without a server request. |
| **Payload** | `<img src=x onerror=alert(1)>` | Triggers a script when the image fails to load. |

## 3. Execution Workflow

1. **Source Code Discovery:** Audited the `LessonContentView.js` file and located the `showTestParam` function.
2. **Sink Identification:** Confirmed that `this.$el.find('.lesson-content').html('test:' + param);` was being used to render input.
3. **Exploit Logic:** Hypothesized that replacing the `param` with a script-bearing HTML tag would force the browser to execute it.
4. **Verification:** Navigated to the crafted URL to confirm the successful execution of an alert box.

## 4. Key Commands
```javascript
// The identified vulnerable code snippet:
this.$el.find('.lesson-content').html('test:' + param);

// The payload used in the URL:
http://localhost:8080/WebGoat/start.mvc#test/<img src=x onerror=alert(1)>
```

## 5. Evidence of Work

![Discovery](/images/dom-xss-analysis-discovery.jpeg)
*Caption: Discovery phase identifying the existence of Cross-Site Scripting weaknesses within the application.*

![Results](/images/dom-xss-analysis-results.jpeg)
*Caption: Results phase confirming the execution of arbitrary JavaScript via the DOM-based XSS vulnerability.*

## 6. Professional Impact

This vulnerability poses a significant risk to Data Confidentiality and User Session Integrity, as an attacker could use this flaw to steal session cookies, hijack accounts, or redirect users to phishing sites. To remediate this, I recommended replacing the unsafe `.html()` method with `.text()`, which ensures all user input is treated as plain text rather than executable code. Additionally, implementing a robust Content Security Policy (CSP) would provide a secondary layer of defense to block unauthorized script execution.

import os
import glob
import re

category_map = {
    "Network Security & Infrastructure": "Network & Infrastructure Security",
    "Web Application Pentesting": "Application Security (AppSec)",
    "Binary & System Exploitation": "Penetration Testing & Vulnerability Assessment",
    "Cryptography & Data Integrity": "DevSecOps & Strategy",
    "Security Operations & Engineering": "Security Operations (SOC) & Incident Response"
}

files = glob.glob("content/posts/*.md")
for file in files:
    with open(file, 'r') as f:
        content = f.read()
    
    for old, new in category_map.items():
        # Update the frontmatter categories array
        content = content.replace(f'categories = ["{old}"]', f'categories = ["{new}"]')
        
    with open(file, 'w') as f:
        f.write(content)

print(f"Updated {len(files)} files.")

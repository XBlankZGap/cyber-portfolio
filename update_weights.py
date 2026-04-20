import os
import glob

category_weights = {
    "Security Operations (SOC) & Incident Response": 100,
    "Penetration Testing & Vulnerability Assessment": 200,
    "Network & Infrastructure Security": 300,
    "Application Security (AppSec)": 400,
    "DevSecOps & Strategy": 500
}

files = glob.glob("content/posts/*.md")
for file in files:
    with open(file, 'r') as f:
        content = f.read()
    
    # Find category
    weight = 999
    for cat, base_weight in category_weights.items():
        if f'"{cat}"' in content:
            weight = base_weight
            break
            
    # Add weight to frontmatter if not exists, or replace it
    if "weight =" in content:
        import re
        content = re.sub(r'weight\s*=\s*\d+', f'weight = {weight}', content)
    else:
        # insert after draft = false
        content = content.replace('draft = false\n', f'draft = false\nweight = {weight}\n')
        
    with open(file, 'w') as f:
        f.write(content)

print(f"Updated weights in {len(files)} files.")

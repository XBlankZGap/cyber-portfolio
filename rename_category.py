import glob

files = glob.glob("content/posts/*.md")
files.append("layouts/_default/list.html")

for file in files:
    with open(file, 'r') as f:
        content = f.read()
    
    if "DevSecOps & Strategy" in content:
        content = content.replace("DevSecOps & Strategy", "DevSecOps & Cryptography")
        with open(file, 'w') as f:
            f.write(content)
        print(f"Updated {file}")

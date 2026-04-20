import os
import re

content_dir = '/home/sophy/cyber-site/content/posts'
output_file = '/home/sophy/cyber-site/project_summaries.txt'
base_url = 'https://XBlankZGap.github.io/cyber-portfolio/posts/'

projects = []

def clean_list(text):
    return text.replace('[', '').replace(']', '').replace('"', '').replace("'", "").strip()

for filename in sorted(os.listdir(content_dir)):
    if filename.endswith('.md'):
        with open(os.path.join(content_dir, filename), 'r') as f:
            content = f.read()
            
            # Split front matter and body
            parts = content.split('+++')
            if len(parts) < 3:
                parts = content.split('---')
            
            front_matter = parts[1] if len(parts) > 1 else ""
            body = parts[2] if len(parts) > 2 else content
            
            # Extract title
            title_match = re.search(r'title = "(.*?)"', front_matter) or re.search(r"title = '(.*?)'", front_matter)
            title = title_match.group(1) if title_match else filename
            
            # Extract tools from front matter
            tools_match = re.search(r'tools = \[(.*?)\]', front_matter)
            tools = clean_list(tools_match.group(1)) if tools_match else ""
            
            # If tools missing, look in body
            if not tools:
                tools_section = re.search(r'## \d\. (Tool Selection|Key Commands).*?\n(.*?)\n', body, re.IGNORECASE)
                if tools_section:
                    tools = tools_section.group(2).strip()
                else:
                    # Look for table with tools
                    table_tools = re.findall(r'\|\s*\*\*?(?:Tools?|Language|Scanning Engine)\*\*?\s*\|\s*(.*?)\s*\|', body, re.IGNORECASE)
                    if table_tools:
                        tools = ", ".join(table_tools)

            # Extract tags (Skills)
            tags_match = re.search(r'tags = \[(.*?)\]', front_matter)
            skills = clean_list(tags_match.group(1)) if tags_match else "Cybersecurity, Technical Analysis"
            
            # Extract Objective
            obj_match = re.search(r'\*\*Objective:\*\* (.*?)\n', body)
            objective = obj_match.group(1).strip() if obj_match else "Analyze and secure system infrastructure."
            
            # Extract Findings
            # Strategy: Get text under Section 1 and Section 5/6 (Impact/Results)
            findings_parts = []
            
            section_1 = re.search(r'## 1\..*?\n(.*?)(?=\n##|\n!\[)', body, re.DOTALL)
            if section_1:
                findings_parts.append(section_1.group(1).strip())
            
            impact_section = re.search(r'## [56]\..*?(Impact|Results).*?\n(.*?)(?=\n##|$)', body, re.DOTALL | re.IGNORECASE)
            if impact_section:
                findings_parts.append(impact_section.group(2).strip())
            
            findings = " ".join(findings_parts).replace('\n', ' ').strip()
            # Truncate findings if too long
            if len(findings) > 500:
                findings = findings[:497] + "..."
                
            if not findings:
                findings = "Refer to project link for detailed findings and vulnerability analysis."
            
            link = base_url + filename.replace('.md', '/')
            
            projects.append({
                'title': title,
                'objective': objective,
                'findings': findings,
                'tools': tools if tools else "See project description",
                'skills': skills,
                'link': link
            })

with open(output_file, 'w') as f:
    f.write(f"CYBERSECURITY PORTFOLIO PROJECT SUMMARIES\n")
    f.write(f"Total Projects: {len(projects)}\n")
    f.write("="*50 + "\n\n")
    
    for i, p in enumerate(projects, 1):
        f.write(f"{i}. {p['title']}\n")
        f.write(f"   Link: {p['link']}\n")
        f.write(f"   Objective: {p['objective']}\n")
        f.write(f"   Findings: {p['findings']}\n")
        f.write(f"   Tools Used: {p['tools']}\n")
        f.write(f"   Skills Gained: {p['skills']}\n")
        f.write("-" * 50 + "\n\n")

print(f"Successfully generated {output_file}")

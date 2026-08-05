from pathlib import Path
import json

score = 0
total = 0
report = []

def check(desc, ok):
    global score, total
    total += 1
    if ok:
        score += 1
        report.append(f"✅ {desc}")
    else:
        report.append(f"❌ {desc}")

root = Path(".")

check("collection.json", (root/"collection.json").exists())
check("README.md", (root/"README.md").exists())
check("CATALOG.md", (root/"CATALOG.md").exists())
check("CONTRIBUTING.md", (root/"CONTRIBUTING.md").exists())
check("ROADMAP.md", (root/"ROADMAP.md").exists())
check("Template", (root/"templates/SKILL_TEMPLATE.md").exists())
check("GitHub Action", (root/".github/workflows/validate-skills.yml").exists())

collection = json.loads((root/"collection.json").read_text(encoding="utf-8"))
index = json.loads((root/"skills/index.json").read_text(encoding="utf-8"))

check("Mesmo número de skills", len(collection["skills"]) == len(index))

for skill in index:
    p = root / skill["path"]
    check(f"{skill['id']}/SKILL.md", p.exists())

percent = round(score/total*100)

report.append("")
report.append(f"Score: {score}/{total}")
report.append(f"Saúde da coleção: {percent}%")

if percent == 100:
    report.append("Status: PRONTA PARA BETA")
elif percent >= 90:
    report.append("Status: QUASE PRONTA")
else:
    report.append("Status: NECESSITA AJUSTES")

Path("REPORT.md").write_text("\n".join(report), encoding="utf-8")

print("\n".join(report))

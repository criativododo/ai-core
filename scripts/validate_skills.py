from pathlib import Path
import sys

ROOT = Path("skills")
required = ["name:", "description:", "version:", "author:"]

errors = []

for skill_dir in sorted(ROOT.iterdir()):
    if not skill_dir.is_dir():
        continue

    skill_file = skill_dir / "SKILL.md"

    if not skill_file.exists():
        errors.append(f"[ERRO] {skill_dir.name}: SKILL.md não encontrado")
        continue

    text = skill_file.read_text(encoding="utf-8")

    for field in required:
        if field not in text:
            errors.append(f"[ERRO] {skill_dir.name}: campo obrigatório ausente -> {field}")

if errors:
    print("\n".join(errors))
    sys.exit(1)

print(f"✅ {len([d for d in ROOT.iterdir() if d.is_dir()])} skills validadas com sucesso.")

#!/usr/bin/env python3

import json
import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

COLLECTION = ROOT / "collection.json"
INDEX = ROOT / "skills" / "index.json"

collection = json.loads(COLLECTION.read_text(encoding="utf-8"))
skills = json.loads(INDEX.read_text(encoding="utf-8"))

cmd = sys.argv[1] if len(sys.argv) > 1 else "help"

if cmd == "list":
    print(f"\n{collection['name']}\n")
    for s in skills:
        print(f"- {s['id']}")
    sys.exit(0)

elif cmd == "manifest":
    print(json.dumps(collection, indent=2, ensure_ascii=False))
    sys.exit(0)

elif cmd == "info":
    if len(sys.argv) < 3:
        print("Uso: python scripts/ai_core.py info <skill>")
        sys.exit(1)

    skill = sys.argv[2]

    for s in skills:
        if s["id"] == skill:
            print(json.dumps(s, indent=2, ensure_ascii=False))
            sys.exit(0)

    print("Skill não encontrada.")
    sys.exit(1)

elif cmd == "doctor":
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "doctor.py")],
        check=True
    )
    sys.exit(0)

print("""
AI Core CLI

Comandos:

list
info <skill>
manifest
doctor
""")

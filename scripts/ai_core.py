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




elif cmd == "release":
    import shutil
    import subprocess

    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "doctor.py")],
        check=True
    )

    build = ROOT / "build-release"
    dist = ROOT / "dist"

    shutil.rmtree(build, ignore_errors=True)
    shutil.rmtree(dist, ignore_errors=True)

    build.mkdir()
    dist.mkdir()

    arquivos = [
        "collection.json",
        "README.md",
        "CATALOG.md",
        "CONTRIBUTING.md",
        "ROADMAP.md"
    ]

    pastas = [
        "skills",
        "templates",
        ".github"
    ]

    for arq in arquivos:
        shutil.copy2(ROOT / arq, build / arq)

    for pasta in pastas:
        shutil.copytree(ROOT / pasta, build / pasta)

    destino = dist / "ai-core"

    shutil.make_archive(
        str(destino),
        "zip",
        build
    )

    shutil.rmtree(build)

    print("\\n✅ Release criada:")
    print(destino.with_suffix(".zip"))
    sys.exit(0)

print("""
AI Core CLI

Comandos:

list
info <skill>
manifest
doctor
release
""")

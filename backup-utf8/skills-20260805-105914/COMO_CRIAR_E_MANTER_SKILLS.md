Eu faria um documento que ensina **como manter o AI Core**, não apenas como criar Skills. Assim, qualquer IA (ou você daqui a um ano) entende o processo.

Salve como:

**`skills/COMO_CRIAR_E_MANTER_SKILLS.md`**

```md
# Manual de Criação e Manutenção de Skills

Este repositório é a fonte oficial ("Source of Truth") das Skills utilizadas pelos agentes de IA do Criativo Dodô.

## Objetivo

Toda Skill deve existir neste repositório antes de ser utilizada em qualquer plataforma (Claude, GPT, Manus, Gemini etc.).

O GitHub é a fonte oficial de versionamento.

---

# Estrutura

Cada Skill é um arquivo:

skills/

branding.skill
consultoria.skill
humanizar.skill
...

Nunca mantenha versões duplicadas da mesma Skill.

---

# Criando uma Skill

1. Criar um novo arquivo:

```bash
touch skills/minha-skill.skill
```

2. Editar o arquivo.

3. Testar a Skill no Claude.

4. Caso aprovada, salvar.

---

# Alterando uma Skill

Após qualquer alteração:

```bash
git add .

git commit -m "feat(skill): melhora minha-skill"

git push
```

Nunca altere uma Skill sem criar um commit.

---

# Convenção de Commits

Nova Skill

```text
feat(skill): adiciona branding
```

Melhoria

```text
feat(skill): melhora branding
```

Correção

```text
fix(skill): corrige branding
```

Reorganização

```text
refactor(skill): reorganiza branding
```

Documentação

```text
docs: atualiza manual
```

---

# Fluxo Oficial

Ideia

↓

Criar Skill

↓

Testar

↓

Commit

↓

Push

↓

GitHub

↓

Uso pelos agentes

---

# Versionamento

Cada commit representa uma evolução da Skill.

Nunca sobrescreva histórico.

Caso uma alteração seja ruim, utilize o Git para recuperar versões anteriores.

---

# Agentes Consumidores

As Skills deste repositório podem ser utilizadas por:

- Claude
- ChatGPT
- Manus
- Gemini
- Cursor
- Codex
- Outros agentes

---

# Fonte da Verdade

Este repositório é a única fonte oficial das Skills.

Nenhuma Skill deve existir apenas dentro do Claude.

Toda Skill deve estar versionada neste repositório.

---

# Boas práticas

- Um arquivo por Skill.
- Nome curto e descritivo.
- Atualizar apenas quando necessário.
- Fazer commits pequenos.
- Escrever mensagens de commit claras.
- Nunca excluir histórico.
- Sempre realizar `git push` após um commit.

---

# Fluxo Diário

```bash
cd ~/Desktop/ai-core

# editar uma Skill

git add .

git commit -m "feat(skill): descrição da alteração"

git push
```

Este é o fluxo padrão para manutenção das Skills.
```

Esse documento vira o "manual operacional" do seu AI Core e padroniza como qualquer pessoa (ou agente de IA) deve criar, alterar e versionar Skills.
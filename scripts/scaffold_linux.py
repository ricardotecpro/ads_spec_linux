import os
from pathlib import Path

# --- Configuration ---
SYLLABUS = [
    {"id": 1, "module": "Módulo 1 – Fundamentos", "title": "Introdução ao Linux e Software Livre"},
    {"id": 2, "module": "Módulo 1 – Fundamentos", "title": "Instalação e Ambiente"},
    {"id": 3, "module": "Módulo 1 – Fundamentos", "title": "Estrutura do Sistema de Arquivos"},
    {"id": 4, "module": "Módulo 1 – Fundamentos", "title": "Terminal e Primeiros Comandos"},
    {"id": 5, "module": "Módulo 2 – Administração", "title": "Manipulação de Arquivos"},
    {"id": 6, "module": "Módulo 2 – Administração", "title": "Permissões e Segurança"},
    {"id": 7, "module": "Módulo 2 – Administração", "title": "Gerenciamento de Pacotes"},
    {"id": 8, "module": "Módulo 2 – Administração", "title": "Processos e Monitoramento"},
    {"id": 9, "module": "Módulo 3 – Ferramentas", "title": "Compactação e Backup"},
    {"id": 10, "module": "Módulo 3 – Ferramentas", "title": "Redes no Linux"},
    {"id": 11, "module": "Módulo 3 – Ferramentas", "title": "Variáveis de Ambiente e Bash"},
    {"id": 12, "module": "Módulo 3 – Ferramentas", "title": "Redirecionamento e Pipes"},
    {"id": 13, "module": "Módulo 4 – Especialização", "title": "Introdução a Shell Script"},
    {"id": 14, "module": "Módulo 4 – Especialização", "title": "Linux para Programadores"},
    {"id": 15, "module": "Módulo 4 – Especialização", "title": "Serviços e Inicialização"},
    {"id": 16, "module": "Módulo 4 – Especialização", "title": "Projeto Final"},
]

DIRS = [
    "docs/aulas",
    "docs/slides/.src",
    "docs/quizzes/.src",
    "docs/exercicios",
    "docs/projetos",
    "docs/assets/images"
]

# --- Templates ---

TEMPLATE_AULA = """# {title}

## 🎯 Objetivos da Aula
- [ ] Compreender os conceitos de {title}
- [ ] Praticar comandos no terminal
- [ ] Resolver desafios propostos

## 📊 Visão Geral
```mermaid
graph TD
    A[Início] --> B[Conceito]
    B --> C[Prática]
    C --> D[Projeto]
```

## 🧠 Conceito
O Linux é um sistema...

!!! info "Conceito"
    Linux é o núcleo (kernel) de um sistema operacional livre.

## 💻 Prática Terminal
```termynal-exec
ls -la
pwd
```

!!! tip "Dica"
    Use sempre a tecla `Tab` para completar comandos.

## 🚀 Mini-Projeto
Desenvolva um pequeno tutorial sobre...

---
## 🎯 Próximos Passos

<div class="grid cards" markdown>

-   :material-presentation: **Acessar Slides**
    -   [Ver Slides da Aula](../slides/slide-{id:02d}.html)

-   :material-school: **Quiz**
    -   [Responder Quiz](../quizzes/quiz-{id:02d}.md)

-   :material-dumbbell: **Exercícios**
    -   [Lista de Exercícios](../exercicios/exercicio-{id:02d}.md)

-   :material-rocket: **Projeto**
    -   [Mini Projeto](../projetos/projeto-{id:02d}.md)

</div>
"""

TEMPLATE_SLIDE = """---
theme: material
---

# {title}
## Aula {id:02d} 🐧

---

## Objetivos
- Entender {title} {{ .fragment }}
- Aplicar na prática {{ .fragment }}

---

## O que é {title}?
Explicação detalhada aqui.

```bash
# Exemplo de comando
ls /etc
```

---

## Diagrama da Aula
```mermaid
graph LR
    User -->|Comando| Terminal
    Terminal -->|Kernel| Hardware
```

---

## Resumo
- Ponto 1 {{ .fragment }}
- Ponto 2 {{ .fragment }}

---

<!-- _class: lead -->
# Próxima Aula: ...
"""

TEMPLATE_QUIZ = """# Quiz {id:02d}: {title}

**Teste seus conhecimentos.**

1. Qual o comando para listar arquivos?
    - ( ) cd
    - (x) ls
    - ( ) pwd
    *Explicação: O comando `ls` (list) é usado para listar conteúdos de diretórios.*

2. Linux é software livre?
    - (x) Sim
    - ( ) Não
    *Explicação: O Linux é distribuído sob a licença GPL.*

3. [Pergunta 3...]
    - ( ) Opção A
    - (x) Opção B
    *Explicação: ...*

4. [Pergunta 4...]
    - ( ) Opção A
    - (x) Opção B
    *Explicação: ...*

5. [Pergunta 5...]
    - ( ) Opção A
    - (x) Opção B
    *Explicação: ...*

6. [Pergunta 6...]
    - ( ) Opção A
    - (x) Opção B
    *Explicação: ...*

7. [Pergunta 7...]
    - ( ) Opção A
    - (x) Opção B
    *Explicação: ...*

8. [Pergunta 8...]
    - ( ) Opção A
    - (x) Opção B
    *Explicação: ...*

9. [Pergunta 9...]
    - ( ) Opção A
    - (x) Opção B
    *Explicação: ...*

10. [Pergunta 10...]
    - ( ) Opção A
    - (x) Opção B
    *Explicação: ...*
"""

TEMPLATE_EXERCICIO = """# Exercícios Aula {id:02d}: {title}

## 🟢 Básico
1. Execute o comando `...` e descreva a saída.
2. Crie uma pasta chamada `aula-{id:02d}`.

## 🟡 Intermediário
3. Mova o arquivo `X` para a pasta `Y`.
4. Mude a permissão do arquivo para `755`.

## 🔴 Desafio
5. Crie um script que automatize a criação de 10 pastas e um arquivo dentro de cada uma.
"""

TEMPLATE_PROJETO = """# Projeto Aula {id:02d}: {title}

## 🚀 Descrição
Implemente um sistema de organização de arquivos que...

## 📋 Requisitos
- [ ] Criar estrutura de pastas
- [ ] Aplicar permissões corretas
- [ ] Usar pipes e redirecionamento

## 💡 Dica
Explore o comando `find` e `xargs`.
"""

def create_files():
    for d in DIRS:
        Path(d).mkdir(parents=True, exist_ok=True)
    
    for lesson in SYLLABUS:
        lid = lesson["id"]
        title = lesson["title"]
        
        # Paths
        p_aula = Path(f"docs/aulas/aula-{lid:02d}.md")
        p_slide_src = Path(f"docs/slides/.src/slide-{lid:02d}.md")
        p_quiz_src = Path(f"docs/quizzes/.src/quiz-{lid:02d}.md")
        p_exerc = Path(f"docs/exercicios/exercicio-{lid:02d}.md")
        p_proj = Path(f"docs/projetos/projeto-{lid:02d}.md")
        
        # Write Files (Overwrite based on request to "atualizar")
        p_aula.write_text(TEMPLATE_AULA.format(id=lid, title=title), encoding="utf-8")
        p_slide_src.write_text(TEMPLATE_SLIDE.format(id=lid, title=title), encoding="utf-8")
        p_quiz_src.write_text(TEMPLATE_QUIZ.format(id=lid, title=title), encoding="utf-8")
        p_exerc.write_text(TEMPLATE_EXERCICIO.format(id=lid, title=title), encoding="utf-8")
        p_proj.write_text(TEMPLATE_PROJETO.format(id=lid, title=title), encoding="utf-8")
            
        print(f"Generated Lesson {lid:02d}: {title}")

def update_mkdocs():
    mkdocs_path = Path("mkdocs.yml")
    content = mkdocs_path.read_text(encoding="utf-8")
    
    # Simple nav generation
    nav = ["nav:", "  - Início: index.md", "  - Plano de Ensino: plano-ensino.md", "  - Aulas:"]
    current_module = None
    for lesson in SYLLABUS:
        module = lesson["module"]
        title = lesson["title"]
        lid = lesson["id"]
        if module != current_module:
            nav.append(f"      - {module}:")
            current_module = module
        nav.append(f"        - 'Aula {lid:02d} - {title}': aulas/aula-{lid:02d}.md")
    
    nav.extend([
        "  - Exercícios:",
        "      - 'Índice': exercicios/index.md",
    ])
    for i in range(1, 17):
        nav.append(f"      - 'Ex {i:02d}': exercicios/exercicio-{i:02d}.md")
        
    nav.extend([
        "  - Projetos:",
        "      - 'Índice': projetos/index.md",
    ])
    for i in range(1, 17):
        nav.append(f"      - 'Proj {i:02d}': projetos/projeto-{i:02d}.md")

    nav.extend([
        "  - Quizzes:",
        "      - 'Índice': quizzes/index.md",
    ])
    for i in range(1, 17):
        nav.append(f"      - 'Quiz {i:02d}': quizzes/quiz-{i:02d}.md")

    nav.extend([
        "  - Slides:",
        "      - 'Índice': slides/index.md",
    ])
    for i in range(1, 17):
        nav.append(f"      - 'Slide {i:02d}': slides/slide-{i:02d}.md")

    nav.extend([
        "  - Configuração:",
        "      - 'Índice': setups/index.md",
        "      - 'Setup Android': setups/setup-01.md",
        "      - 'Setup iOS': setups/setup-02.md",
        "  - Sobre:",
        "      - 'O Curso': sobre.md",
        "      - 'Roadmap': project_roadmap.md",
        "      - 'Materiais Extras': materiais.md",
        "  - Impressão: print_page.md"
    ])
    
    if "nav:" in content:
        content = content.split("nav:")[0]
    
    final_content = content.strip() + "\n\n" + "\n".join(nav) + "\n"
    mkdocs_path.write_text(final_content, encoding="utf-8")
    print("Updated mkdocs.yml")

if __name__ == "__main__":
    create_files()
    update_mkdocs()

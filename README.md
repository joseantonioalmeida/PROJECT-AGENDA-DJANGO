#  Agenda Django — Projeto de Agenda de Contatos

Este é um projeto de Agenda de Contatos desenvolvido com o framework web Django (Python).  
Ele permite cadastrar, listar, atualizar e excluir contatos de forma organizada, com autenticação de usuários e filtros de pesquisa.

---

##  Funcionalidades

✔ Cadastro de usuários  
✔ Login e logout  
✔ CRUD completo de contatos  
✔ Associação de contatos por usuário  
✔ Pesquisa por nome, e-mail ou telefone  
✔ Exclusão com confirmação  
✔ Ordenação por data e ID  
✔ Estilização responsiva com CSS personalizado

---

##  Tecnologias Utilizadas

- 🐍 Python  
- (MVC/MVT)  
- 🗃 SQLite (banco de dados local)  
- 🐚 HTML / CSS  
- ⚙️ Git / GitHub

---

## 💡 Estrutura do Projeto

📦PROJECT-AGENDA-DJANGO
┣ 📂contact
┣ 📂project
┣ 📂utils
┣ 📜manage.py
┣ 📜requirements.txt

- **contact** – App responsável por contatos e lógica da agenda  
- **project** – Arquivo de configuração principal do Django  
- **utils** – Scripts utilitários (Gera contatos fake para popular o banco (editar para usar campos corretos) )

---
📌 Uso Básico

✔ Registrar novo usuário
✔ Login
✔ Adicionar contato
✔ Editar contato
✔ Excluir contato com confirmação

---

💬 O que eu Aprendi com esse Projeto

Criação de rotas, views e templates no Django;
Organização do Django MVT;
Modelos, formulários, validações;
Pesquisa com filtros avançados (Q);
Autenticação de usuários;
UX de confirmação de exclusão;
Git & GitHub;
CSS personalizado.

---

##  Como Rodar o Projeto Localmente

1. Clone o repositório:
git clone https://github.com/joseantonioalmeida/PROJECT-AGENDA-DJANGO.git

2. Acesse a pasta:
cd PROJECT-AGENDA-DJANGO

3. Crie um ambiente virtual:
python -m venv venv

4. Ative o ambiente:
Windows:
  venv\Scripts\activate

macOS / Linux:
  source venv/bin/activate

5. Instale as dependências:

pip install -r requirements.txt

6. Crie as migrações e aplique-as:
python manage.py makemigrations
python manage.py migrate

7. Crie um super usuário (opcional):
python manage.py createsuperuser

8. Rode o servidor:
python manage.py runserver

Agora acesse:
👉 http://127.0.0.1:8000


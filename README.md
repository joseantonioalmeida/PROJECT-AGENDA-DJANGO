#  Agenda Django — Projeto de Agenda de Contatos

Este é um projeto de Agenda de Contatos desenvolvido com o framework Django (Python). Ele permite a gestão completa de contatos com autenticação de usuários, filtros de pesquisa e uma interface responsiva.

Além da aplicação, este repositório documenta um Deploy Real em ambiente Linux (WSL2) utilizando a stack de produção Nginx + Gunicorn + PostgreSQL.

---

##  Funcionalidades

✔ Cadastro de usuários  
✔ Login e logout  
✔ CRUD completo de contatos (Criar, Ler, Atualizar e Excluir) 
✔ Associação de contatos por usuário (privacidade)  
✔ Pesquisa avançada por nome, e-mail ou telefone 
✔ UX de confirmação para exclusão   
✔ Estilização responsiva com CSS personalizado
✔ Cadastro de usuários, Login e Logout

---

# 🛠 Tecnologias e Infraestrutura

## Desenvolvimento & Produção:
  *Python 3.10+ & Django 5.x.
  
  *PostgreSQL (Banco de dados de produção).
  
  *HTML5 / CSS3.
## Deploy & DevOps:
  *SO: Windows 11 com WSL2 (Ubuntu 22.04).
  *Porta de Saída: 80 (HTTP Padrão).
  *Web Server: Nginx (Proxy Reverso e entrega de arquivos estáticos).
  *App Server: Gunicorn (WSGI HTTP Server).
  *Controle de Versão: Git (Fluxo de deploy via Git Push para o servidor).

---

## 🏗 Arquitetura do Deploy (WSL2)
O servidor foi estruturado para ser acessível diretamente pela rede:
1. Ponte de Rede: O Windows redireciona o tráfego da porta 80 (ou porta personalizada via netsh) para o IP interno do WSL2.
2. Nginx: Escuta na Porta 80, servindo arquivos CSS/JS da pasta staticfiles e repassando requisições para o Gunicorn.
3. Gunicorn: Gerencia os processos do Django através de um Unix Socket (/run/agenda.sock), conectando-se ao PostgreSQL para persistência de dados.

---

## 💡 Estrutura do Projeto

📦 PROJECT-AGENDA-DJANGO
┣ 📂 contact (App principal e lógica da agenda).
┣ 📂 project (Configurações globais e conexão com DB).
┣ 📂 utils (Scripts para geração de dados fake).
┣ 📜 manage.py.
┣ 📜 requirements.txt.
┗ 📂 docs (Contém guias de configuração: gunicorn.txt, nginx-http.txt, server.md.txt).

---
📌 Uso Básico

✔ Registrar novo usuário.
✔ Login.
✔ Adicionar contato.
✔ Editar contato.
✔ Excluir contato com confirmação.

---

💬 O que eu Aprendi com esse Projeto

  *Django MVT: Organização de rotas, models, formulários e views.
  *Banco de Dados Relacional: Migração de SQLite para PostgreSQL e gestão de roles/privilégios.
  *Segurança: Autenticação de usuários e proteção de rotas.
  *DevOps: Configuração de servidores Linux, escrita de arquivos de serviço no systemd, gerenciamento de permissões de
            pastas (chmod/chown) e configuração de proxy reverso no Nginx na Porta 80.
  *Git & GitHub.

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

---
## 🌍 Detalhes do Deploy (Modo Produção)
Para entender como este projeto foi colocado no ar, consulte os arquivos explicativos na raiz ou pasta de documentos:
  *gunicorn.txt: Configuração do Daemon do Gunicorn.
  *nginx-http.txt: Configuração do servidor Nginx na Porta 80.
  *server.md.txt: Guia detalhado de comandos Linux e Portproxy do Windows.

---

## 🏗 Arquitetura do Deploy
O fluxo de funcionamento do servidor foi configurado da seguinte forma:
1. Usuário acessa o IP do Windows na porta 3390.
2. O Portproxy do Windows redireciona o tráfego para o IP interno do WSL2.
3. O Nginx recebe a requisição:
    3.1 Se for /static/, ele entrega o CSS/JS diretamente da pasta staticfiles.
    3.2 Se for dinâmico, ele repassa para o Gunicorn.
4. O Gunicorn processa a lógica do Django através de um Unix Socket (mais rápido que portas TCP).
---

## 📖 Passo a Passo do Deploy (O que foi feito)
1. Preparação do Servidor (Ubuntu/WSL2)
Criamos um repositório bare no Linux para receber o código via Git direto do Windows:
  mkdir -p ~/agendarepo
  cd ~/agendarepo
  git init --bare

No Windows, adicionamos o servidor como um remoto:
  git remote add agendarepo jose@172.26.126.18:/home/jose/agendarepo
  git push agendarepo main
  
2. Configuração do Gunicorn (Application Server)
Para garantir que o Django rode como um serviço do sistema, configuramos o gunicorn.service e o gunicorn.socket no /etc/systemd/system/.
Comando de execução:
  gunicorn --workers 3 --bind unix:/run/agenda.sock agenda.wsgi:application

3. Configuração do Nginx (Web Server)
Configuramos o Nginx para servir os arquivos estáticos (CSS) que o Django não serve em produção e para agir como proxy reverso:
server {
    listen 80; # Porta interna do Linux
    location /static/ {
        alias /home/jose/agendaapp/static/;
    }
    location / {
        include proxy_params;
        proxy_pass http://unix:/run/agenda.sock;
    }
}

4. Permissões e Coleta de Estáticos
Um dos maiores desafios foi garantir que o usuário do Nginx (www-data) tivesse acesso aos arquivos do usuário jose. Resolvemos com:
  sudo chmod -R 755 /home/jose/agendaapp/static
  python manage.py collectstatic

5. Ponte de Rede (Windows ↔ WSL2)
Como o WSL2 fica em uma rede interna, usamos o PowerShell (Admin) para abrir a porta para o mundo:
  netsh interface portproxy add v4tov4 listenport=3390 listenaddress=0.0.0.0 connectport=80 connectaddress=172.26.126.18

---
## 🛑 Como Encerrar o Servidor (Decommissioning)
Se precisar desligar o projeto e limpar os recursos:

1. Parar Serviços: sudo systemctl stop agenda.socket nginx
2. Remover Redirecionamento: netsh interface portproxy reset (No Windows Admin).
3. Limpar Arquivos: rm -rf ~/agendaapp ~/agendarepo.

---

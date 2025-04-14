# Twitter Clone - Projeto Final

Este é um projeto final desenvolvido com Django como parte do meu curso. A aplicação é uma versão simplificada do Twitter, com funcionalidades básicas de rede social.

## Funcionalidades

- Cadastro, login e logout de usuários
- Criação automática de perfis
- Postagem de mensagens (texto)
- Feed com os posts do próprio usuário e de quem ele segue
- Seguir e deixar de seguir usuários
- Visualização de perfil e posts de outros usuários
- Interface simples e responsiva

## Tecnologias

- Python 3
- Django 5
- SQLite (banco de dados local)
- HTML, CSS (inline, sem frameworks externos)

## Como rodar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/twitter-clone.git
   cd twitter-clone
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install django
   ```

4. Rode as migrações e o servidor:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. Acesse em:
   ```
   http://127.0.0.1:8000/
   ```

## Autor

Gabriel Soares da Silva  
[LinkedIn](https://www.linkedin.com/in/gabrielssilva-dev/) | [Portfólio](https://github.com/gabrielsilva3107)
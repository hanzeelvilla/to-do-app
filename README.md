# Welcome to my to do App

As a way to practice my django skills I created with django a to do App, where you can
sign up and login in to create, update and delete your to dos. You just need a title
and optionally a body for more content and a deadline. Also, I'm planning to add roles
so you can mark a to do as a routine, hobby, important and more, a search bar where you
can search by date, title, body, role etc.

## Set up

Clone the repository

```bash
git clone "https://github.com/hanzeelvilla/to-do-app.git"
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

```bash
.\.venv\Scripts\Activate.ps1
```

Install the requirements

```bash
pip install -r requirements.txt
```

Create the database

```python
python manage.py migrate
```

Create a .env file and a SECRET_KEY

You can run this comand that generates a a functional SECRET_KEY

```python
python -c "import secrets; print(secrets.token_urlsafe())"
```

Then you just copy and paste the output **without quotation marks** inside your .env file

For example

```bash
SECRET_KEY=OY1c4f2I0ZF0XGhySXhOxOgW_1ny-0k1a2Il0qOUhA
```


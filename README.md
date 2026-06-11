# 📰 News Hub Django Project

## 📌 Overview

News Hub is a Django-based web application that allows users to register, create, approve, and manage news articles using role-based access control.

The project also includes a REST API built with Django REST Framework.

---

# 🚀 Features

## User Roles

* Reader
* Journalist
* Editor

## Authentication

* User Registration
* Login / Logout
* Role-based permissions

## Article System

* Journalists can create articles
* Journalists can edit and delete their own articles before approval
* Editors can approve articles
* Readers can view approved articles

## REST API

* Retrieve approved articles
* View subscribed articles
* Create, update, and delete articles via API

## Email Notifications

* Console-based email notifications when articles are approved

---

# 🛠 Tech Stack

* Python
* Django
* Django REST Framework
* MariaDB / MySQL
* HTML / CSS

---

# ⚙️ Project Setup Instructions

## 1. Clone the repository

```bash
git clone https://github.com/JanieGrove28/news-hub.git
```

---

## 2. Enter the project folder

```bash
cd news-hub
```

---

## 3. Create a virtual environment

### Windows

```bash
python -m venv venv
```

---

## 4. Activate the virtual environment

### Windows

```bash
venv\Scripts\activate
```

---

## 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄 Database Setup (MariaDB)

This project uses MariaDB/MySQL instead of SQLite.

## Create the database

Open MariaDB/MySQL and run:

```sql
CREATE DATABASE news_db;
```

---

## Database Configuration

Update the `DATABASES` section in `settings.py` if needed:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'news_db',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

## 6. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 7. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

---

## 8. Run the development server

```bash
python manage.py runserver
```

---

## 9. Open the application

Open your browser and go to:

```text
http://127.0.0.1:8000/
```

---

# 🔑 Test User Roles

## Journalist

* Can create articles
* Can edit and delete their own articles

## Editor

* Can approve articles
* Can manage publishers

## Reader

* Can read approved articles

---

# 👨‍💻 Admin Access

Publishers can be created through the Django admin panel.

Admin URL:

```text
http://127.0.0.1:8000/admin/
```

---

# 📡 API Endpoints

## Approved Articles

```text
/api/articles/
```

## Subscribed Articles

```text
/api/subscriptions/
```

---

# ✅ Notes

* Editors are responsible for approving articles before they become visible to readers.
* Duplicate email registration is prevented.
* Role-based access control is implemented throughout the project.
* Publishers can be created through the Django admin panel.
* The project uses MariaDB/MySQL as the database backend.

---

# 🐳 Docker Setup

This project includes a Dockerfile for containerised deployment.

## Build Docker Image

```bash
docker build -t news-hub .
```

## Run Docker Container

```bash
docker run -p 8000:8000 news-hub
```

## Access Application

Open in your browser:

```text
http://127.0.0.1:8000
```

## Requirements

* Docker Desktop must be installed and running.
* Ensure port 8000 is free before running the container.

## Notes

If Docker is not installed, the project can still be run locally using the virtual environment setup above.

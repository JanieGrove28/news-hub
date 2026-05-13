# 📰 News Hub Django Project

## 📌 Overview
<<<<<<< HEAD

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
* SQLite
* HTML / CSS

---

# ⚙️ Project Setup Instructions

## 1. Clone the repository

```bash
git clone <your-github-repository-link>
```

---

## 2. Enter the project folder

```bash
cd news_capstone
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
=======
News Hub is a Django-based web application that allows users to register, create, approve, and manage news articles using role-based access control.

It also includes a REST API built with Django REST Framework.

---

## 🚀 Features

- Custom User Model with roles:
  - Reader
  - Journalist
  - Editor

- Authentication system:
  - Login / Logout
  - Role-based permissions

- Article system:
  - Create articles (Journalist only)
  - Approve articles (Editor only)
  - View published articles

- REST API:
  - Get approved articles
  - View subscribed articles
  - Create/update/delete articles via API

- Email simulation:
  - Console-based email notifications when articles are approved

---

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework
- SQLite
- HTML / CSS

---

## ⚙️ Setup Instructions

1. Install dependencies:
```bash
pip install -r requirements.txt
>>>>>>> bf8953c5044d80824794e9511acb31e28f75b7b6

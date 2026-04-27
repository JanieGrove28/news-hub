# 📰 News Hub Django Project

## 📌 Overview
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

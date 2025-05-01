# 🏋️ User Membership Management API

A Django REST Framework-based API to manage users and their memberships.
Suitable for use cases like gyms, clubs, or other subscription-based services.

---

## 📂 Project Structure
```
.
├── app/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
├── database/
│   ├── db.cnf
│   └── docker-compose.yaml
├── usermanagement/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── requirements.txt
├── manage.py
└── .gitignore
```

## 🚀 Features

- Manage different types of memberships (name, price, duration).
- Register and list members.
- Track and update membership status for each member.
- Validate active membership via an entry code.
- RESTful endpoints with automatic expiration logic.
- MySQL support via Docker for quick setup.

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/WendersonBarros/gym-management-django.git
cd gym-management-django
```

### 2. Set up MySQL using Docker

```bash
cd database
cp db.cnf.example db.cnf
docker-compose up -d
```

### 3. Install dependencies

It's recommended to use a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Run migrations and start the server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## 📡 API Endpoints

All endpoints are prefixed with `/app/`.

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/membership/` | GET, POST | List or create memberships |
| `/membership/<id>` | GET, PUT, DELETE | Retrieve, update, or delete a membership |
| `/member/` | GET, POST | List or register members |
| `/member/<id>` | GET, PUT, DELETE | Retrieve, update, or delete a member |
| `/status/` | GET, POST | List or create membership statuses |
| `/status/<id>` | GET, PUT | Retrieve or update membership status |
| `/entry/<entry_code>` | GET | Validate if a member has an active membership |

---

## 🧠 Models Overview

- `Membership`: Defines membership plans (name, price, duration, active status).
- `Member`: Basic user info, including a unique `entry_code`.
- `Membership_status`: Connects a member with a membership, tracks expiration and renewal.

Expiration dates are calculated based on the membership duration and auto-updated when memberships are renewed.

---

## ⚙️ Configuration

The database is configured in `database/db.cnf` and referenced in `settings.py`. Ensure the `.cnf` file is properly filled and named (no `.example` extension).

---

## ✅ Example Request: Validate Entry Code

```http
GET /app/entry/12345
```

**Response:**

```json
{
  "detail": "Membership is active"
}
```

If expired:

```json
{
  "detail": "Membership expired"
}
```

---

## 📦 Dependencies

- Django 5.2
- Django REST Framework
- MySQL client (`mysqlclient`)
- Docker (for MySQL)

---

## 🛡️ Security & Deployment Notes

- Change the default `SECRET_KEY` in production.
- Set `DEBUG = False` before deploying.
- Add your domain to `ALLOWED_HOSTS`.

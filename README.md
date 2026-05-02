# 🏆 Team Task Flow - Full Stack Management App

This is a personal project built to demonstrate a full-stack Django implementation with role-based access control and RESTful APIs. It's designed for small teams to track their project progress efficiently.


## ✨ Key Features

- **🔐 Secure Authentication**: Signup/Login system with role-based access (Admin/Member).
- **📂 Project Management**: Create and manage multiple projects.
- **✅ Task Tracking**: Create, assign, and monitor tasks with status and priority indicators.
- **📊 Premium Dashboard**: A stunning, glassmorphism-inspired dashboard for a quick overview of team productivity.
- **⚡ REST APIs**: Fully documented RESTful endpoints built with Django REST Framework.
- **📱 Responsive Design**: Seamless experience across desktop and mobile.

## 🛠️ Tech Stack

- **Backend**: Django 4.2+
- **API**: Django REST Framework
- **Frontend**: Django Templates + Vanilla CSS + JS
- **Database**: PostgreSQL (Production) / SQLite (Local)
- **Deployment**: Railway
- **Security**: WhiteNoise (Static files), CORS-headers, Role-based permissions

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd team-task-management
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Migrations
```bash
python manage.py migrate
```

### 4. Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 5. Start the Server
```bash
python manage.py runserver
```

## 🔑 Demo Accounts

- **Admin**: `admin` / `admin123`
- **Member**: `member1` / `member123`

## 📡 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/projects/` | GET | List all projects (filtered by role) |
| `/api/tasks/` | GET | List all tasks |
| `/api/tasks/` | POST | Create a new task (Admin only) |

## 🌐 Deployment

This app is optimized for **Railway**. To deploy:
1. Connect your GitHub repository to Railway.
2. Set the `SECRET_KEY` and `DEBUG=False` in environment variables.
3. Railway will automatically detect the `Procfile` and deploy.

---
Built with ❤️ for the Candidate Nomination Assignment.

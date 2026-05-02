# 🚀 Team Task Manager

A professional, feature-rich Django application for managing projects, tasks, and teams with ease. This project is optimized for high-performance production environments and is fully deployable to **Railway**.

## ✨ Features

- **Dashboard**: A clean overview of your ongoing projects and tasks.
- **Project Management**: Create, update, and track progress of multiple projects.
- **Task Management**: Assign tasks to team members, set priorities, and track status.
- **Role-based Access**: Custom user model with 'Admin' and 'Member' roles.
- **Team Collaboration**: Manage team members and their assignments.
- **Production Ready**: Configured with PostgreSQL, Gunicorn, WhiteNoise, and automated migrations.

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Database**: PostgreSQL (Production) / SQLite (Development)
- **Styling**: Vanilla CSS (Custom Design)
- **Deployment**: Railway / GitHub Actions
- **Server**: Gunicorn with WhiteNoise for static files

## 🚀 Quick Start (Local Development)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ABIRAM323/TEAM_TASK_MANAGER.git
   cd TEAM_TASK_MANAGER
   ```

2. **Set up virtual environment**:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start development server**:
   ```bash
   python manage.py runserver
   ```

## 🌍 Production Deployment (Railway)

This project is pre-configured for Railway. Simply connect your GitHub repository and ensure you have a **PostgreSQL** service linked to your web service.

### Key Deployment Files:
- `railway.json`: Deployment orchestration.
- `Procfile`: Gunicorn server configuration.
- `start.sh`: Automated startup script for migrations and static files.
- `fix_admin.py`: Guaranteed admin account creation.

## 🔒 License

Distributed under the MIT License. See `LICENSE` for more information.

---
Created with ❤️ by ABIRAM323

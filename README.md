# Nairobi 5G Home Internet Installation Leads

A Django web application for collecting 5G internet installation leads in Nairobi.

## Features

- Multi-step form for checking 5G availability
- Lead collection with contact information
- Email notifications for new leads
- Responsive design

## Local Development

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install requirements: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Start server: `python manage.py runserver`

## Requirements Management

⚠️ **CRITICAL WARNING:** Never use `pip freeze > requirements.txt` as it captures all installed packages including system packages that will cause deployment failures on platforms like PythonAnywhere, Heroku, etc.

### How to properly manage requirements:
1. **Only add packages you explicitly install** for your project
2. **Django automatically handles its own dependencies** (asgiref, sqlparse, etc.)
3. **For production deployment**, keep requirements.txt minimal
4. **If you need to add a package**, manually edit requirements.txt

### Example of correct requirements.txt:
```
Django==4.2.11
django-crispy-forms==2.1
```

### Wrong way (causes deployment failures):
```bash
pip freeze > requirements.txt  # ❌ NEVER DO THIS
```

## PythonAnywhere Deployment

### Step 1: Upload Code
1. Go to PythonAnywhere dashboard
2. Open a Bash console
3. Clone your repository:
   ```bash
   git clone https://github.com/leonadotienootieno-rgb/5G-internet.git
   cd 5G-internet
   ```

### Step 2: Set up Virtual Environment
```bash
mkvirtualenv --python=python3.10 myenv
pip install -r requirements.txt
```

### Step 3: Database Setup
```bash
python manage.py migrate
```

### Step 4: Static Files
```bash
python manage.py collectstatic
```

### Step 5: Create WSGI File
Create `internet_leads/wsgi.py` (if not exists) or update it:
```python
import os
import sys

path = '/home/yourusername/5G-internet'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'internet_leads.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### Step 6: Configure Web App
1. Go to Web tab in PythonAnywhere
2. Add a new web app
3. Choose **Manual configuration** and **Python 3.10**
4. Set the source code path to: `/home/yourusername/5G-internet`
5. Set the WSGI file path to: `/home/yourusername/5G-internet/internet_leads/wsgi.py`
6. Set virtualenv path to: `/home/yourusername/.virtualenvs/myenv`
7. Set static files:
   - URL: `/static/`
   - Path: `/home/yourusername/5G-internet/staticfiles`

### Step 7: Environment Variables
Set these in Web > Environment variables:
- `DJANGO_SETTINGS_MODULE=internet_leads.settings`
- `SECRET_KEY=your-secret-key-here`
- `DEBUG=False`
- `ALLOWED_HOSTS=your-domain.pythonanywhere.com`

### Step 8: Reload Web App
Click the green reload button to deploy.

## Email Configuration

For production, update `internet_leads/settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

## License

MIT License
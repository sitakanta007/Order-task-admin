# Django Admin Panel (Products + Coupons + Orders + Customers)

This Django project acts as the single source of truth for the entire ecommerce system.
It owns the MySQL schema that your Node.js API uses through Prisma.

The Django admin panel allows you to manage:

- Customers
- Products
- Orders
- Coupons
- UserCoupon (coupon usage tracking)

## Tech Stack

- Python 3.10+
- Django
- MySQL (hosted on Railway)
- Gunicorn (for running in EC2)
- EC2 (Ubuntu 22.04)
- Static files served from EC2 filesystem

## Requirements

- Python 3
- Virtual environment
- MySQL database URL
- EC2 instance with inbound ports open (if deployed)

## Project Structure
```
django-app/
 ├─ adminpanel/           # Main Django project
 │   ├─ settings.py
 │   ├─ urls.py
 │   ├─ wsgi.py
 │   └─ ...
 ├─ coupons/
 ├─ products/
 ├─ orders/
 ├─ customers/
 ├─ manage.py
 ├─ venv/
 └─ static/               # Collected static files
```
## Environment Variables
```
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=3306
```

## Static Files Setup

In settings.py:
```
STATIC_URL = '/static/'
STATIC_ROOT = '/home/ubuntu/django-app/static/'
```

Collect them:
```
python manage.py collectstatic
```

## Local Development

Activate virtual environment:
```source venv/bin/activate```

Install dependencies:

```pip install -r requirements.txt```

Run dev server:

```python manage.py runserver 0.0.0.0:8000```

Deployment on EC2 (Gunicorn Only, No Nginx)
1. SSH into EC2
```ssh -i key.pem ubuntu@your-ec2-ip```

2. Start venv
```
cd django-app
source venv/bin/activate
```

3. Run with Gunicorn
```gunicorn --bind 0.0.0.0:8000 adminpanel.wsgi:application --reload```


Runs Django admin live on:
```
http://<ec2-ip>:8000/
```
4. Run with Gunicorn + Systemd (optional)

Create ```/etc/systemd/system/gunicorn.service:```
```
[Unit]
Description=Gunicorn service for Django app
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/django-app
Environment="PATH=/home/ubuntu/django-app/venv/bin"
ExecStart=/home/ubuntu/django-app/venv/bin/gunicorn \
  --workers 3 \
  --bind 0.0.0.0:8000 \
  adminpanel.wsgi:application

[Install]
WantedBy=multi-user.target
```

Reload & start:
```
sudo systemctl daemon-reload
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
```

Check status:
```
sudo systemctl status gunicorn
```

## Admin Panel Features
- Manage Products - Name, Price, Description, Image URL, Quantity, Created timestamp
- Manage Coupons - Code, Type (percentage / hybrid / flat), nth_value (nth order number for any user), Max discount, Status active/inactive, Track Coupon Usage
- Every coupon usage is visible in UserCoupon entries.
- Orders Management - All orders placed by the Node frontend appear in: orders → order_items

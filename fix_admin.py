import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

username = 'admin'
email = 'admin@example.com'
password = 'admin12345'

user, created = User.objects.get_or_create(username=username)
user.email = email
user.set_password(password)
user.is_superuser = True
user.is_staff = True
user.role = 'admin'  # Ensure the role is set to admin
user.save()

if created:
    print(f"Superuser {username} created successfully.")
else:
    print(f"Superuser {username} updated successfully.")

# backend_3350

# Backend API for the simple forum android application 
# Deployed via pythonanywhere

# Migrate before running 
python manage.py makemigrations
python manage.py migrate

# To run on all interfaces on port 8000
python manage.py runserver 0:8000

# To run local on port 8000
python manage.py runserver localhost:8000 

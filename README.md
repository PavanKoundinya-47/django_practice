
# 🖼️ Django Project

This is a sample Django project developed as part of an interview task. It includes basic blog functionality using PostgreSQL as the backend.

---

## 🔧 Setup Instructions

Follow the steps below to get the project up and running:

1. **Clone the repository and navigate into the project directory:**

   ```bash
   git clone https://github.com/your-username/django_practice-master.git
   cd django_practice-master/test_mod
   ```

2. **Set up the PostgreSQL database:**

   Make sure PostgreSQL is installed and running. Then run the following SQL commands:

   ```sql
   CREATE DATABASE test_imgdb;
   ALTER ROLE postgres WITH PASSWORD 'u&e!!!s4g3es28iTv3oqvkBod';
   ```

   💡 *If `test_imgdb` already exists, you can skip the `CREATE DATABASE` command.*

3. **Ensure the following database configuration is present in `settings.py`:**

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'test_imgdb',
           'USER': 'postgres',
           'PASSWORD': 'u&e!!!s4g3es28iTv3oqvkBod',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

4. **Create and activate a Python virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

5. **Install required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

6. **Run the database migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Start the Django development server:**

   ```bash
   python manage.py runserver
   ```

8. **Open your browser and go to:**

   [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
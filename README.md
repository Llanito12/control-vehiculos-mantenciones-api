Evaluacion N. 2 - Programacion Backend

Asignatura: Programacion Backend
Docente: Erick Bailey Rebolledo
Modalidad: Individual
Proyecto: API REST con Django REST Framework

---

Descripcion del Proyecto

Este proyecto consiste en el desarrollo e implementacion de una API REST funcional construida con Django y Django REST Framework (DRF). Permite realizar operaciones CRUD completas (GET, POST, PUT, PATCH, DELETE) sobre el modelo de datos configurado.

---

Tecnologias Utilizadas

- Python 3.x
- Django 6.x
- Django REST Framework
- python-dotenv
- SQLite / PostgreSQL

---

Estructura del Proyecto

evaluacion_backend/
.env.example
.gitignore
manage.py
README.md
requirements.txt
scripts/
    setup_db.sql
mi_proyecto/
    settings.py
    urls.py
api/
    models.py
    serializers.py
    views.py
    urls.py

---

Instrucciones de Instalacion y Ejecucion

1. Clonar el repositorio
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_CARPETA>

2. Crear y activar el entorno virtual

python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\activate



3. Instalar dependencias
pip install -r requirements.txt


5. Ejecutar migraciones
python manage.py makemigrations
python manage.py migrate

6. Iniciar el servidor
python manage.py runserver

Acceso local: http://127.0.0.1:8000/api/

---

Endpoints

Categorias:
GET / POST -> /api/categorias/
GET / PUT / PATCH / DELETE -> /api/categorias/{id}/

Productos:
GET / POST -> /api/productos/
GET / PUT / PATCH / DELETE -> /api/productos/{id}/
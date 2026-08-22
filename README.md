# PTC Maket API

A Django REST API for the PTC project. The API is organized into portfolio, blog, CRM, and company-information applications, with English, Persian, and Arabic URL prefixes.

## Features

- Django 5.1+ and Django REST Framework
- OpenAPI schema and Swagger UI via drf-spectacular
- Multilingual API routes: English (`en`), Persian (`fa`), and Arabic (`ar`)
- Portfolio categories and projects
- Blog articles and comments
- CRM order requests and contact messages
- Company history and team members
- PostgreSQL support
- Uploaded media and CKEditor integration

## Requirements

- Python 3.12 or newer
- PostgreSQL 15+ for local development, or Docker and Docker Compose

## Quick Start With Docker

1. Build and start the services:

   ```bash
   docker compose up --build
   ```

2. In another terminal, apply migrations:

   ```bash
   docker compose exec web python manage.py migrate
   ```

3. Create an admin user when needed:

   ```bash
   docker compose exec web python manage.py createsuperuser
   ```

The API is available at `http://127.0.0.1:8000`.

To stop the services:

```bash
docker compose down
```

The PostgreSQL data is stored in the `postgres_data` Docker volume.

## Local Development

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Make sure PostgreSQL is running and configure the development database connection in `config/settings/development.py`.

4. Apply migrations and create an administrator:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

## API Documentation

- Swagger UI: `http://127.0.0.1:8000/api/docs/`
- OpenAPI schema: `http://127.0.0.1:8000/api/schema/`
- Generated schema file: [`schema.yml`](schema.yml)
- Django admin: `http://127.0.0.1:8000/en/admin/`

The API routes are locale-prefixed. Replace `en` with `fa` or `ar` as needed.

## API Endpoints

All endpoints below are available under `/en/api/` and the other supported locale prefixes.

| Application | Resources |
| --- | --- |
| About | `/about/history/`, `/about/team-members/` |
| Blog | `/blog/articles/`, `/blog/comments/` |
| CRM | `/crm/order-request/`, `/crm/contact-us/` |
| Portfolio | `/portfolio/categories/`, `/portfolio/projects/` |

Most resources use Django REST Framework viewsets, so collection and detail routes are available. Check Swagger UI or `schema.yml` for supported methods, request bodies, and response schemas.

## Media and Static Files

Uploaded files are stored in `media/`. During development, Django serves media and static files directly when `DEBUG=True`.

## Useful Commands

```bash
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py test
python manage.py collectstatic
```

## Project Structure

```text
about/      Company history and team members
blog/       Articles and comments
config/     Django project configuration and URL routing
core/       Shared project functionality
crm/        Contact and order-request APIs
portfolio/  Users, categories, and projects
media/      Uploaded media files
postman/    Postman collections
```

## License

No license has been specified for this project.

# Docker setup

- `cp ./backend/.env.sample .backend.env`
- Configure backend environment variables by editing `.backend.env`
- `cp ./frontend/.env.sample .frontend.env`
- Create images with `docker compose build`
- Create containers without starting using `docker compose up --no-start`
- Run backend setup and note OAuth ID:
```
docker compose run backend python manage.py migrate
docker compose run backend python manage.py createsuperuser
docker compose run backend python manage.py setup	
```
- Edit `.frontent.env` and add the OAuth ID
- Launch services with `docker compose up`

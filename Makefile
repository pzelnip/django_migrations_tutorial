build:
	docker build -t django_migrations_tutorial:latest .

shell:
	docker run --rm -v $(PWD):/app -e DJANGO_SETTINGS_MODULE=django_migrations_tutorial.settings.local -w /app -it django_migrations_tutorial:latest /bin/bash

server:
	docker run --rm -v $(PWD):/app -p 6100:6100 -e DJANGO_SETTINGS_MODULE=django_migrations_tutorial.settings.local -w /app django_migrations_tutorial:latest python manage.py runserver 0.0.0.0:6100

clean:
	docker rmi django_migrations_tutorial:latest

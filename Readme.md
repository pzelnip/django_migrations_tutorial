# Django Migrations Sample Project

Sample project for illustrating Django migrations.

## Setup

1. Clone the repository
2. Create a virtual environment
3. Install the requirements
4. `export DJANGO_SETTINGS_MODULE=django_migrations_tutorial.settings.local`

Alternatively, a Dockerfile is supplied to run the project in a container.  To use this:

1. Clone the repository
2. `make build`
3. `make server` & leave that running
4. go to <http://localhost:6100>

Then to do interactive shell stuff (like the management commands), do a `make shell`

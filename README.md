# flask-workshop-espe

This is the code explained in the **Workshop** for the **"Universidad de las Fuerzas Armadas ESPE"**.

**Workshop Name:** Entornos Virtuales en Python orientado a DevOps | Taller de Flask

I started explaining Virtual Envs in Python and how to isolate dependencies in Python projects.

How to handle multiple versions of Python with [pyenv](https://github.com/pyenv/pyenv) and its commands to list and install available versions of Python.

I exposed about [python-poetry](https://python-poetry.org/), some commands to create a Python project, create the virtual env, add and remove dependencies; and what are the `pyproject.toml` file used together with `poetry.lock`. **See more about pyproject.toml file:** [PEP 517](https://www.python.org/dev/peps/pep-0517/) and [PEP 518](https://www.python.org/dev/peps/pep-0518/).

Why create the virtual env inside the project and name it: `.venv`.

Importance of locking dependency versions ([poetry.lock](https://github.com/hugofer93/taller-flask/blob/main/poetry.lock)) in Development, Staging, and Production Environments, also about **semantic versioning**.

I explained why use environment variables to separate settings, credentials or secrets from source code, using [python-decouple](https://github.com/henriquebastos/python-decouple/).

To finish, I made an **Introduction to Flask** applying what was described above, I also explained each line of the application's source code and its configuration, database and templates.
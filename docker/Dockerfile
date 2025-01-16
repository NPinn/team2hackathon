FROM python:3-slim

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install git -y -q --no-install-recommends && \
	apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false

ENV \
	PIP_NO_CACHE_DIR=off \
	PIP_DISABLE_PIP_VERSION_CHECK=on \
	PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1 \
	VIRTUAL_ENV=/venv 
ENV \
	POETRY_VIRTUALENVS_CREATE=false \
	POETRY_VIRTUALENVS_IN_PROJECT=false \
	POETRY_NO_INTERACTION=1 \
	POETRY_VERSION=1.8.3

# install poetry 
RUN pip install "poetry==$POETRY_VERSION"

# add venv to path 
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN mkdir /venv
RUN mkdir /app
RUN mkdir /app/.ruff_cache/
RUN touch /app/.coverage
RUN adduser -u 1000 --disabled-password --gecos "" appuser && chown appuser:appuser -R \
	/app \
	/app/.coverage \
	/app/.ruff_cache \
	/venv
WORKDIR /app

COPY --chown=appuser:appuser ./pyproject.toml ./poetry.lock ./

USER appuser

# # Install python packages
RUN python -m venv $VIRTUAL_ENV
RUN . $VIRTUAL_ENV/bin/activate
RUN poetry config virtualenvs.create false
RUN poetry install --no-root -n 

# # During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "futurecare.wsgi"]

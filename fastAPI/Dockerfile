FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

WORKDIR /code/app
RUN alembic init migrations

COPY ./preset_alembic/preset.ini /code/app/alembic.ini
COPY ./preset_alembic/env.py /code/app/migrations/env.py

# WORKDIR /code
#RUN alembic revision --autogenerate -m "Created"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

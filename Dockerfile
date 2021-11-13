FROM python:3.9
ENV PYTHONBUFFERED=1
ENV MYSQL_HOST=host.docker.internal
WORKDIR /code
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

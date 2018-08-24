FROM python:3.6-alpine
EXPOSE 8000

COPY Pipfile* /app/
WORKDIR /app
RUN pip3 install pipenv flake8 && \
    pipenv install --system --dev

COPY . /app
CMD ["gunicorn", "-w 4", "-b 0.0.0.0", "main:app"]

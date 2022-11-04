FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt


COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()"]
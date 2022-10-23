FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt


COPY . .

CMD [ "python", "-m", "flask", "--app", "./app/app.py", "run", "--host","0.0.0.0"]
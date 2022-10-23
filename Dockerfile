FROM python:3

WORKDIR /usr/src/app

# TODO: intall dependencies when we use them.
# Currently there is not requirements.txt file so this will cause the build to break.
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app/app.py" ]
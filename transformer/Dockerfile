FROM python:3 as build

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]

FROM build as test

RUN pytest --cov=. --cov-fail-under=75

FROM build as production

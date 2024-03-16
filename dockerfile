FROM python:3.12.1-alpine3.18

WORKDIR /src/weatherapp/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .

RUN rm -f logs/mylogs.log && touch logs/mylogs.log

RUN cd /src/weatherapp/app

CMD [ "python", "main.py" ]

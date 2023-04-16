FROM python:3.9

WORKDIR /biz

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "-m", "biz"]

FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install pandas requests --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./get_sw.py" ]
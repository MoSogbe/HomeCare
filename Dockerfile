FROM python:3.11
#EXPOSE 5000
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir  --upgrade -r requirements.txt
RUN pip install flask
COPY . .
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--reload"]
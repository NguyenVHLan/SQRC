FROM python:3.11
RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6
EXPOSE 5000
WORKDIR /app
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
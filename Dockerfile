FROM selenium/standalone-chrome:latest

USER root
#USER seluser

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*


WORKDIR /app


COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt


COPY URL_Validation.py .


CMD ["python3", "URL_Validation.py"]
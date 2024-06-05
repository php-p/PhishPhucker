# Stage 1: Build dependencies
FROM python:3.11 AS build
WORKDIR /app
COPY phishphucker.py /app/phishphucker.py
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Install additional dependencies and download Chrome and ChromeDriver
FROM build AS dependencies
RUN apt-get update && \
    apt-get install -y wget unzip curl fonts-liberation libasound2 libatk-bridge2.0-0 libatk1.0-0 libatspi2.0-0 libcups2 libdbus-1-3 libdrm2 libgbm1 libgtk-3-0 libnspr4 libnss3 libxcomposite1 libxdamage1 libxfixes3 libxkbcommon0 libxrandr2 xdg-utils libu2f-udev && \
    curl -Lo "/tmp/chromedriver-linux64.zip" "https://storage.googleapis.com/chrome-for-testing-public/123.0.6312.86/linux64/chromedriver-linux64.zip" && \
    curl -Lo "/tmp/chrome-linux64.zip" "https://storage.googleapis.com/chrome-for-testing-public/123.0.6312.86/linux64/chrome-linux64.zip" && \
    unzip /tmp/chromedriver-linux64.zip -d /opt && \
    unzip /tmp/chrome-linux64.zip -d /opt && \
    rm /tmp/chromedriver-linux64.zip /tmp/chrome-linux64.zip

# Stage 3: Final image
FROM python:3.11
WORKDIR /app
COPY --from=dependencies /app /app
COPY --from=dependencies /opt/chrome-linux64 /app/chrome
COPY --from=dependencies /opt/chromedriver-linux64 /app/
COPY phuckers /app/phuckers
CMD ["python", "phishphucker.py", ">", "/dev/stdout"]

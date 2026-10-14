FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY service/ ./service/

# OpenShift runs containers as an arbitrary non-root user
RUN chgrp -R 0 /app && chmod -R g=u /app
EXPOSE 8000
CMD ["gunicorn", "--bind=0.0.0.0:8000", "--log-level=info", "service:app"]

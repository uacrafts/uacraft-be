FROM python:3.12-slim AS builder
 
WORKDIR /code

RUN apt-get update && \
    python3 -m venv venv

ENV VIRTUAL_ENV=/code/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
 
COPY requirements requirements
RUN pip install --upgrade pip && \
    pip install -r requirements/development.txt --no-cache-dir
 
# Stage 2
FROM python:3.12-slim AS runner
 
WORKDIR /code
 
COPY --from=builder /code/venv venv
COPY . .

ENV VIRTUAL_ENV=/code/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PORT=8000
 
EXPOSE ${PORT}

CMD gunicorn --bind :${PORT} --workers 2 apps.wsgi
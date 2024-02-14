FROM python:3.10 AS builder

WORKDIR /app

RUN python3 -m venv venv
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY requirements.txt .
RUN pip install -r requirements.txt


FROM python:3.10 AS runner

ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PORT=8000

WORKDIR /app

COPY --from=builder /app/venv venv
COPY backend backend

EXPOSE ${PORT}
CMD gunicorn --bind :${PORT} --workers 2 backend.wsgi
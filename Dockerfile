ARG IMAGEBASE=app-base:latest

FROM ${IMAGEBASE}

COPY models/ /models
COPY app.py /

CMD python /app.py
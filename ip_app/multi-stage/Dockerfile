FROM python AS  builder

WORKDIR /app

ADD https://github.com/Deepak128404/flask_ip.git .

RUN pip install -r ip_app/requirements.txt

FROM python:3.9.19-slim-bookworm
WORKDIR /app

COPY --from=builder /app /app
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /usr/local/lib /usr/local/lib

EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["ip_app/get_container_ip.py"]

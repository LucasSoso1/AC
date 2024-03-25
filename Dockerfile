
FROM python:3.7-slim
RUN pip install Flask mysql-connector-python
RUN mkdir /templates
RUN mkdir /static
COPY AC2.py /app.py
COPY templates/* /templates/
COPY static/* /static/
RUN chmod -R a+rwx /static
RUN chmod -R a+rwx /templates
CMD ["python", "app.py"]

FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /opt/services/pyapp/src
#VOLUME ["/opt/services/pyapp/src"]
# We copy the requirements.txt file first to avoid cache invalidations
COPY requirements.txt /opt/services/pyapp/src/
WORKDIR /opt/services/pyapp/src
RUN pip install -r requirements.txt
COPY . /opt/services/pyapp/src
EXPOSE 5090
CMD ["python", "run.py"]
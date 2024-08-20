FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /ecom
COPY requirements.txt /ecom/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /ecom/
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


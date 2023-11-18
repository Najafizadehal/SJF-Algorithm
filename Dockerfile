FROM python:3.10

ADD OSproject/main.py .

CMD ["python","./main.py"]
FROM python:3

RUN git clone git@gitlab.com:jwlatech/mili-test.git

RUN pip3 install parameterized

WORKDIR /mili-test

CMD ["python3", "-m", "unittest"] && ["python3", "main.py"]
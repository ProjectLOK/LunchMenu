From python

RUN apt-get update
WORKDIR /usr/src/app
COPY . .
COPY ./requirements.txt ./
RUN pip install -r ./requirements.txt
CMD ["main.py"]
ENTRYPOINT ["python3"]
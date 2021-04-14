FROM python

COPY ETL.py ETL.py
COPY vaccineburden.csv vaccineburden.csv 
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "./ETL.py" ]

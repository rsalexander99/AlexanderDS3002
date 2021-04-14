#!/usr/bin/env python3

import pandas as pd
import MySQLdb

# Read data
df = pd.read_csv('vaccineburden.csv')

# Drop covid_burden column
df.drop(columns=["covid_burden"])

# Transform Possible Vaccine Coverage column into percent values
df["possible_vaccine_coverage"] *= 100

# Initialize connection to AWS-RDS instance
DB_NAME = input("Enter database name: ")
HOST = input("Enter host URL: ")
USER = input("Enter username: ")
PASS = input("Enter password: ")

try:
    # Establish connection
    db = MySQLdb.connect(host=HOST, user=USER, passwd=PASS, db=DB_NAME)
    c = db.cursor()
    # Ensure table does not exist
    c.execute(f"DROP TABLE IF EXISTS vaccinecoverage")
    # Create empty table
    c.execute(f"CREATE TABLE vaccinecoverage (country VARCHAR(40), country_economic_status VARCHAR(40), possible_vaccine_coverage DECIMAL(4,2))")
    # Insert dataframe into SQL Server
    for i, row in df.iterrows():
        c.execute(f"INSERT INTO vaccinecoverage (country, country_economic_status, possible_vaccine_coverage) VALUES (%s, %s, %s)", (row.country, row.country_economic_status, row.possible_vaccine_coverage))
    db.commit()
    # Print completion statement
    print("Dataset on global COVID vaccine coverage has been successfully written to your SQL server")
    c.close()
except (MySQLdb.Error) as e:
    error_data = str(e)
    print("ERROR: Incorrect database credentials. Re-run file and be sure to input correct credentials")
    c.close()
# AlexanderDS3002
This repository contains project files for DS 3002 Data Science Systems

These files are components of Data Project 1. See dataproject1 in "Packages" section to access container image. NOTE: Run container in interactive mode

Data Project 1: Option 2, ETL Data Processor

This ETL processor ingests a locally-mounted csv file on global COVID vaccination data, transforms it, converts transformed file into SQL database table, and writes it to a MySQL database system.

MySQL database credentials are required to use this tool. These credentials are personal to you, the user, and are typically used to login to your MySQL database via a user interface, like phpMyAdmin or MySQLWorkbench. When running this processor locally (in docker -it mode!), you will be prompted to input your credentials, including, your database name, host name, username, and password. The processor will throw an error if you input incorrect credentials. 

After transforming the vaccineburden.csv into a pandas dataframe and conducting cleaning operations, this tool will use your credentials to connect to a MySQL server, leveraging the mysqlclient library to push the data out to your MySQL database in the form of an SQL table.

The final table, which you can examine on your MySQL user interface, features country-level data on the amount of COVID vaccines each country has purchased and/or agreed to purchase within the last year. The column "possible_vaccination_coverage" indicates what percentage of the country's population will be covered by the vaccines the country has purchased and/or will purchase in the near future. Information on each country's economic status is also included, and the trend illustrated by this table is evidence that wealthier countries control a greater proportion of the global vaccine supply. (I used this data in a project for a different class, in which I presented on the consequences of vaccine nationalism.)

Data Source: Duke Global Health Innovation Center, Updated Weekly, Accessed Mar. 16

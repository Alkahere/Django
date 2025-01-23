# Django Distributed System

This project simulates a distributed system with multiple databases using Django. The system has three databases (`users`, `products`, and `orders`) and performs concurrent data insertions and checks.

## Requirements

- Python 3.10+ (or compatible version)
- Django 4.x+
- SQLite3 (for the databases)

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Alkahere/Django.git
   cd Django_project

## Running the Custom Commands
1. Insert Data into Databases (insert_data)
The insert_data command is used to insert pre-defined data into the users, products, and orders databases concurrently.

## Install Dependencies
= pip install -r requirements.txt

## Make Migrations : 
- python manage.py makemigrations
- python manage.py migrate



To insert the data, run the following command:
## python manage.py insert_data

This command will:
Insert user data into users
Insert product data into products
Insert order data into orders

## Check Data in Databases (check_data)
After inserting the data, you can check the records in the respective databases using the check_data command.

To check the data, run the following command:
## python manage.py check_data
This command will:
Fetch and print all records from the users , products , orders



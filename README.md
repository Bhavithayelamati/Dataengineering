# Multinational Retail Data Centralization

## Table of Contents
- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [How to Use](#how-to-use)
- [Database Credentials](#database-credentials)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project, part of the Data Science Career Accelerator at Ai Core, tackles centralizing sales data for a multinational retail company. The goal is to enhance accessibility and analytical capabilities by consolidating sales data into a PostgreSQL database. The project follows a star schema design, and data-driven insights are derived through PostgreSQL queries.

## Project Structure

### Milestone 1 - Set up the environment

### Milestone 2 - Data Extraction and Cleaning
- `data_cleaning.py`: Contains the `DataCleaning` class for data cleaning.
- `data_extraction.py`: Includes the `DataExtractor` class for data extraction.
- `database_utils.py`: Defines the `DatabaseConnector` class for database interaction.
- `main.py`: Main script to execute the data handling process.
- `db_creds.yaml`: Database credentials file (Add this to `.gitignore`).

### Milestone 3 - Create the Database Schema
This milestone is dedicated to creating the database schema, defining the structure of our database, including entities, relationships, and constraints necessary for the project's functionality.
- Task 1: Cast the columns of the orders_table to the correct data types.
- Task 2: Cast the columns of the dim_users_table to the correct data types.
- Task 3: Update the dim_store_details table.
- Task 4: Make changes to the dim_products table for the delivery team.
- Task 5: Update the dim_products table with the required data types.
- Task 6: Update the dim_date_times table.
- Task 7: Updating the dim_card_details table.
- Task 8: Create the primary keys in the dimension tables.
- Task 9: Finalizing the star-based schema & adding the foreign keys to the orders table.
- Task 10: Update the latest code changes to GitHub.

### Milestone 4: Querying the Data
In Milestone 4, query the available data to extract meaningful insights for the business. The queries are designed to answer specific questions and provide valuable metrics that can aid in decision-making.

## Installation
- Technologies Used:
  - Python (Pandas, NumPy)
  - PostgreSQL
  - AWS (boto3)
  - SQLalchemy
  - psycopg2
  - tabula-py
  - YAML (library)

## License
MIT License

Copyright (c) 2024 by Bhavitha Yelamati

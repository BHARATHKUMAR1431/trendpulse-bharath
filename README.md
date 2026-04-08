# TrendPulse

TrendPulse is a Python project that collects live trending stories from the HackerNews API and organises them into useful categories such as technology, world news, sports, science, and entertainment.

The project demonstrates how real-time data can be fetched from an API and stored in structured format for further analysis and visualization.

## Features

* Fetches trending stories from HackerNews
* Categorises stories based on keywords
* Stores structured data in JSON format
* Forms the first step of a data pipeline workflow

## Technologies

Python
Requests library

## How to Run

Install dependency:

pip install requests

Run the script:

python task1_data_collection.py

## Output

The script generates a JSON file inside the data folder:

data/trends_YYYYMMDD.json

Each record contains:

post_id
title
category
score
num_comments
author
collected_at

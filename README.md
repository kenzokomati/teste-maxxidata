# Data Ingestion and Cleaning Script

## Introduction
This project is a Python script that fetches data from the Star Wars API (SWAPI), processes it, cleans it, and saves it into CSV files. It demonstrates basic techniques for handling API requests, transforming data with pandas, and saving processed data to CSV files.


---
## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Explanation](#explanation)


---
## Requirements
This script requires the following Python libraries:

- pandas==2.2.3
- requests==2.32.3

These dependencies can be installed using pip from the requirements.txt file.



---
## Installation
To install the required dependencies, follow these steps:

Clone the repository or download the files.

Create and activate a virtual environment (optional but recommended).
``` bash
python -m venv venv
source venv/bin/activate    # For Linux/Mac
venv\Scripts\activate       # For Windows
```
Install the dependencies:
```bash
pip install -r requirements.txt
```



---
## Usage
Run the script: After installing the necessary dependencies, you can execute the script by running:

```bash
python script.py
```



---
## Output Files: The script will create two folders: raw and work.

- raw/ will contain the original data fetched from the API (people.csv, planets.csv, films.csv).
- work/ will contain the cleaned data (people_cleaned.csv, planets_cleaned.csv, films_cleaned.csv).



---
## Explanation


- ### Fetching Data
The function fetch_data(api_url) sends a GET request to the given API URL. It processes the response and extracts the data in JSON format. If an error occurs during the request (e.g., network error or non-200 status code), it catches and prints the error.


- ### Cleaning Data
The clean_data(df) function applies a transformation to every element in the DataFrame:


- ### Converts string values to lowercase.
Removes any characters that are not alphanumeric or whitespace (such as special characters like @, #, etc.).


- ### Saving Data
The save_csv(data, folder, filename) function saves the processed DataFrame to a CSV file in the specified folder. It creates the folder if it doesn’t exist.

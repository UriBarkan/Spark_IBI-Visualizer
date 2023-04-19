# IBI Investment Visualizer

## Overview

The IBI Investment Visualizer is a Python script that allows you to analyze your investments according to predefined rules. It is designed to work with an Excel file downloaded from IBI's trading platform, a.k.a Spark-IBI.

## Prerequisites

Before using the script, you must have the following:

- An account with IBI
- Login credentials for IBI's trading platform: https://sparkibi.ordernet.co.il/#/auth
- An Excel file of your investments downloaded from the platform

## Usage

To use the script, follow these steps:

1. Clone or download the repository to your local machine.
2. Install the required Python packages using pip: `pip install -r requirements.txt`.
3. Log in to IBI's trading platform and download an Excel file of your investments.
4. Create an Excel `classifications.xlsx` file in the same folder and modify it to fit your needs.
5. Run the script freom the path to your Python file with the command `streamlit run Dashboard.py`. 

## Classification File Format

The `Security Classes.xlsx` file must be formatted as follows:

- The first row should contain the column names: `Stock Number`, `Security Type`, and `Market`.
- Each subsequent row should contain a rule for classifying investments.
- The `Stock Number` column should contain the nserial umber of the security as it appears in IBI Excel file.
- The `Security Type` shoukd contain the type of the security, i.e. either `Stock` or `Bond`.
- The `Market` column should contain geographical market of the security, i.e. `IL` (for Israel) or `Global` (for US securities).

### Structure

Here is the structure of the `Security Classes.xlsx` file:

| Stock Numbe | Security Type | Market |
| ----------- | ------------- | ------ |
| XXX         | Stock         | IL     |
| YYY         | Bond          | Global |

## Example files
Exmaple files with dummy data can be found in the "Example files" folder.

## Contributing

If you find a bug or have a suggestion for improvement, please submit an issue or a pull request.

## License

This project is licensed under the MIT License. See the `License.txt` file for details.

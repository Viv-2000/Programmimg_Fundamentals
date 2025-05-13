# Grid Visualization from Google Docs Table

## Overview

This Python project retrieves a publicly available Google Document, extracts a table, and visualizes its contents on a 2D grid using ASCII characters. The characters `█` and `░` are mapped to numerical values and plotted on a grid to represent the data from the table in a visual format.

The project utilizes the following libraries:
- `requests`: To fetch the HTML content of the Google Doc.
- `BeautifulSoup`: For parsing and extracting table data from the HTML.
- `numpy`: For handling the grid and ensuring efficient data manipulation.
- `matplotlib`: (Although not directly used in this version, it can be applied for better visual representations).

## Features
- Fetches a Google Doc and parses its table data.
- Converts data into a 2D grid format, using `█` for solid blocks and `░` for light blocks.
- Prints the grid visually in the console for easy analysis.

## Requirements
To run this project, you need to install the following Python packages:
```bash
pip install requests beautifulsoup4 matplotlib numpy

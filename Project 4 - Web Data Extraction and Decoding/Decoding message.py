#########################################################################################################################################
#########################################################################################################################################

'''
Project Code Explanation: Grid Visualization from Google Docs Table
Project Overview: This project retrieves a table from a publicly available Google Document, extracts the data, and then visualizes it on a grid-based format using Python libraries such as requests, BeautifulSoup, and matplotlib. The table is represented using two distinct characters: █ (solid block) and ░ (light block). The extracted data is mapped to these characters, then organized into a 2D grid and printed out.

Code Breakdown:

Imports:
-- requests: Used to send HTTP requests to the URL of the Google Doc and retrieve the document's HTML content.
-- BeautifulSoup: Parses the HTML content to extract the table and its data.
-- matplotlib.pyplot: Provides a plotting interface for potential future visualizations (though this is not utilized directly in this code).
-- numpy: Useful for handling multi-dimensional arrays, which represent the grid in this case.

Fetching the Document:
-- The script starts by specifying the URL of the public Google Doc that contains a table.
-- A GET request is sent to fetch the content of the document using the requests.get(url) function.
-- If the request is successful (HTTP status code 200), the document's HTML content is parsed using BeautifulSoup to extract the relevant table(s).

Extracting Data:
-- The script then finds all the <table> elements in the HTML using soup.find_all('table'). It assumes that the first table (index 0) contains the data of interest.
-- The rows (<tr>) of the table are processed, and the content of each cell (<td>) is extracted and stripped of any unwanted whitespace or HTML tags.
-- The data is structured in a list of rows, with each row being a list of cells.

Data Transformation:
-- The data extracted from the table is filtered to remove the header or unnecessary rows, and the remaining rows are parsed.
-- Characters in the table are mapped to numeric values (█ to 1 and ░ to 0), making it easier to represent them visually on a grid.
-- Each row of data is then transformed into (x, numeric_value, y) where:
-- x is the horizontal coordinate (column index),
-- numeric_value corresponds to the block type (1 for solid, 0 for light),
-- y is the vertical coordinate (row index).

Grid Creation:
-- The maximum x and y values are determined to define the grid's size.
-- A 2D NumPy array (grid) is created and initialized with spaces, representing an empty grid.
-- The script then fills the grid with █ (solid) or ░ (light) based on the extracted data and their respective coordinates.

Grid Visualization:
-- The final grid is printed row by row, with characters joined by spaces for better readability.

Future Improvements & Potential Use Cases:
-- Visualization: While this project simply prints the grid, matplotlib could be used to create a more graphical representation, showing the grid as a plot where █ and ░ blocks are rendered as colored squares.
-- Interactivity: This script could be extended to make the grid interactive, where a user could click on a grid cell and see its corresponding data.
-- Enhanced Data Processing: The code could be expanded to handle multiple tables or other types of document content, such as images or text.
'''

#########################################################################################################################################
#########################################################################################################################################


import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np

#########################################################################################################################################
#########################################################################################################################################


# URL for the Google Doc
url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"

# Making the GET request
response = requests.get(url)

# Check if the response is successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all tables in the document
    tables = soup.find_all('table')

    # Assuming the first table is the one we are interested in (based on your description)
    table = tables[0]

    # Extract rows from the table
    rows = table.find_all('tr')

    # Loop through each row and extract the data from each cell (td)
    grid_data = []
    for row in rows:
        cells = row.find_all('td')
        # Extract the content from each cell and strip any extra spaces or HTML tags
        row_data = [cell.get_text(strip=True) for cell in cells]
        grid_data.append(row_data)


 # Print the extracted data
    for row in grid_data:
        print(row)

else:
    print(f"Failed to retrieve the document. Status code: {response.status_code}")

#########################################################################################################################################
#########################################################################################################################################


data = grid_data[1:]

char_to_num = {'█': 1, '░': 0}  # Mapping two characters to numeric values
# Convert x and y coordinates to integers, and map characters to numeric values
data = [(int(x), char_to_num.get(char, 0), int(y)) for x, char, y in data]

# Determine the grid's size
max_x = max([x for x, _, _ in data])
max_y = max([y for _, _, y in data])

# Create an empty grid with spaces (representing empty cells)
grid = np.full((max_y + 1, max_x + 1), ' ')  # Initialize grid with spaces

# Populate the grid with characters
for x, num, y in data:
    grid[y][x] = {1: '█', 0: '░'}[num]  # Place the character (█ or ░) at the correct position

# Print the grid of characters
for row in grid:
    print(' '.join(row))  # Join characters with space for better readability

#########################################################################################################################################
#########################################################################################################################################

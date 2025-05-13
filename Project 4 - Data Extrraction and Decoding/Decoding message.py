import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np


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


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"

# Get the webpage content
page = requests.get(url).text

# Parse the HTML page
soup = BeautifulSoup(page, "html.parser")

# Empty lists to store the data
quotes = [] # will store all the quotes
authors = [] # will store the names of the authors

# Loop through each quote block
for block in soup.find_all("div", class_="quote"):
    quotes.append(block.find("span", class_="text").get_text())
    authors.append(block.find("small", class_="author").get_text())

# Save data into Excel file
pd.DataFrame({"Quote": quotes, "Author": authors}).to_excel("quotes.xlsx", index=False)

print(" Done! Quotes saved in quotes.xlsx")

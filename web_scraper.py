# Task 13: Web Scraping Using BeautifulSoup

import requests
from bs4 import BeautifulSoup
import csv

URL = "https://quotes.toscrape.com/"

try:
    # 1. Fetch HTML content
    response = requests.get(URL)
    response.raise_for_status()

    # 2. Parse HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # 3. Find all quote blocks
    quotes = soup.find_all("div", class_="quote")

    # 4. Open CSV file to store extracted data
    with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author", "Author Link"])

        # 5. Extract text, links safely
        for quote in quotes:
            text = quote.find("span", class_="text")
            author = quote.find("small", class_="author")
            link = quote.find("a")

            quote_text = text.text if text else "N/A"
            author_name = author.text if author else "N/A"
            author_link = link["href"] if link else "N/A"

            writer.writerow([quote_text, author_name, author_link])

    print("Scraping completed. Data saved to quotes.csv")

except requests.exceptions.RequestException as e:
    print("Error fetching the webpage:", e)

# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# -------------------
# Configuration Section
# -------------------
# Define the URL of the page you want to scrape
TARGET_URL = "https://www.oneusefulthing.org/p/strategies-for-an-accelerating-future"

# -------------------
# Web Scraping Section
# -------------------
def fetch_page(url):
    """Fetch the HTML content of the specified URL"""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the response status code is 4XX/5XX
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

# -------------------
# Parsing Section
# -------------------
def parse_content(html_content):
    """Parse the fetched HTML content and extract relevant information"""
    # Example: extracting all paragraph texts
    soup = BeautifulSoup(html_content, 'html.parser')
    paragraphs = [p.text for p in soup.find_all('p')]
    return paragraphs

# -------------------
# Main Execution Section
# -------------------
if __name__ == "__main__":
    # Step 1: Fetch the page
    html_content = fetch_page(TARGET_URL)

    if html_content:
        # Step 2: Parse the page
        extracted_data = parse_content(html_content)

        # Step 3: Process the extracted data (TODO)
        # This is where you might save data to a file, analyze it, or perform other processing.
        # For demonstration, we'll just print the extracted paragraph texts.
        for paragraph in extracted_data:
            print(paragraph)

        # TODO: Add any additional data processing or handling here


import requests
from bs4 import BeautifulSoup

url = "https://hyperdrive.solana.com/projects/explore"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all anchor tags (<a>) with 'href' containing 'github.com'
    github_links = soup.find_all("a", href=lambda href: href and "github.com" in href)

    # Extract and print the GitHub links
    for link in github_links:
        print(link["href"])
else:
    print("Failed to fetch the page.")

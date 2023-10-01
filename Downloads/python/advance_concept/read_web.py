from bs4 import BeautifulSoup
import requests

url = input("Enter the url: ")
# url = "https://example.com"

response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example: Print the title of the web page
    title = soup.title.string
    print(f"Title: {title}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
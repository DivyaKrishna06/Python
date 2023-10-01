import requests

url = "https://www.example.com"

response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Response Content:")
    print(response.text)
else:
    print(f"Request failed with status code {response.status_code}")
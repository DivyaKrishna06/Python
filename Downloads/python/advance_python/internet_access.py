import requests
from ftplib import FTP

# Access a website using HTTP
def fetch_web_content(url):
    try:
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("HTTP Request Successful")
            print("Response Content:")
            print(response.text)
        else:
            print("HTTP Request Failed with Status Code:", response.status_code)
    except Exception as e:
        print("Error:", e)

# Access an FTP server and list directory contents
def list_ftp_directory(hostname, username, password, directory):
    try:
        with FTP(hostname) as ftp:
            ftp.login(user=username, passwd=password)
            ftp.cwd(directory)
            file_list = ftp.nlst()
            print("FTP Directory Listing:")
            for file in file_list:
                print(file)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    # Example URLs
    website_url = "https://www.example.com"
    ftp_hostname = "ftp.example.com"
    ftp_username = "your_username"
    ftp_password = "your_password"
    ftp_directory = "/public_html"

    # Access the website using HTTP
    fetch_web_content(website_url)

    # Access an FTP server and list directory contents
    list_ftp_directory(ftp_hostname, ftp_username, ftp_password, ftp_directory)
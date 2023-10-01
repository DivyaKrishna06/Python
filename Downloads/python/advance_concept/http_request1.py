import requests as req

# Requesting from server
r = req.get('https://www.example.com/')

print(r)

# Printing some lines 
print(r.text[0:1000])
import socket

def is_valid_ip(ip):
    try:
        # Use socket library to attempt to convert the string to an IP address
        socket.inet_pton(socket.AF_INET, ip)
        return True
    except socket.error:
        try:
            # Try IPv6 format
            socket.inet_pton(socket.AF_INET6, ip)
            return True
        except socket.error:
            return False

# Input IP address
ip_address = input("Enter an IP address: ")

if is_valid_ip(ip_address):
    print(f"{ip_address} is a valid IP address.")
else:
    print(f"{ip_address} is not a valid IP address.")
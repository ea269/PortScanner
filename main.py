import socket


# Retrieving our target address
with open('target.txt', 'r') as f:
    target = f.readline().strip()

# Function to scan ports with argument of port number
def port_scan(port):
    try:
        # socket('IPv4', 'TCP')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect and pass target and port
        s.connect((target, port))
        return True
    except:
        return False


# Range of the Standarized ports
for port in range(1, 1024):
    result = port_scan(port)
    # Print open/closed ports
    if result:
        print(f'Port {port} is open!')
    else:
        print(f'Port {port} is closed!')

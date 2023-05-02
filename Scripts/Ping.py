import ping3

# IP address of the device you want to ping
ip = '192.168.15.47'

# Ping the IP adress
response_time = ping3.ping(ip)

# Print the outcome
if response_time is not None:
    print(f"{ip} is online (response time: {response_time} ms)")
else:
    print(f"{ip} is offline")

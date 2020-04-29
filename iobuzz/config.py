# Your socket.io server
# See https://github.com/dmpasilva/iobuzz-server for an example

SERVER_URL = "http://192.168.1.79:3000/game"

# Your socket.io server secret
# This is a very rudimentary technique to ensure only specific applications can join
SERVER_SECRET = "secret"

# Your Buzz Controllers configuration
# Comment the one that does not apply to you

# Wireless Buzz Controllers
#VENDOR_ID = 0x54c
#DEVICE_ID = 0x02

# Wired Buzz Controllers
VENDOR_ID = 0x54c
DEVICE_ID = 0x1000
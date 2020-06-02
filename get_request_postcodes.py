# first we need a way talk to http
# we will use the requests
# the same way we can import math or time, we can import requests
import requests

# import time
#
#
# time.sleep(2)
# requests is not a standard library and must be installed with a package manager
# package is an external library, not native to vanilla versions of python
# a package manager installs and manages said package


# i want to make a get request to get more info on a postcode o_O
# then build the target url with path and arguments
# then I need to use the package request to make the request

# I will recieve a JSON that needs to be parsed into a dictionary, in turn which needs to be turned into another dictionary

path = 'http://api.postcodes.io/postcodes/'
arguments = 'HA39TP'


# Build URL
url_target = path + arguments
print(url_target)

# Requesting and capturing data

response = requests.get(url_target)

print(response)

print(type(response))
#TASK 4

import sys
import requests

try:
    site = sys.argv
    response = requests.get(site)
    a = response.status_code
    if a == 200:
        print ("website is active!")
    else:
        print ("no response, url may be incorrect or site not")

except:
    print ("error in command line argument, couldnt run website check-")
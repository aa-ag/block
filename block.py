############------------ IMPORTS ------------############
import time
from datetime import datetime as dt
import os


############------------ GLOBAL VARIABLE(S) ------------############
### host
hosts_path = '/etc/hosts'

### local host's IP
redirect = '127.0.0.1'

### websites to block
list_of_websites_to_block = ['https://www.youtube.com/']


############------------ FUNCTION(S) ------------############
def block_websites_from_list():
    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now():
            print("Working hours")
            with open(hosts_path, 'r+') as file:
                content = file.read()
                for website in list_of_websites_to_block:
                    if website in content:
                        pass
                    else:
                        file.write(redirect + " " + website + "\n")
        else:
            with open(hosts_path, 'r+') as file:
                content=file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in list_of_websites_to_block):
                        file.write(line)
    
                file.truncate()
    
            print("Personal time")
        time.sleep(5)

############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    block_websites_from_list()
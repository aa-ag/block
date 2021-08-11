############------------ IMPORTS ------------############
import time
from datetime import datetime as dt


############------------ GLOBAL VARIABLE(S) ------------############
### host
hosts_path = '/etc/hosts'

### local host's IP
redirect = '127.0.0.1'

### websites to block
list_of_websites_to_block = ["www.youtube.com","youtube.com"]


############------------ FUNCTION(S) ------------############
def block_websites_from_list():
    while True:
  
        # time of your work
        if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,20):
            print("Working hours")
            with open(hosts_path, 'r+') as file:
                content = file.read()
                for website in list_of_websites_to_block:
                    if website in content:
                        pass
                    else:
                        # mapping hostnames to your localhost IP address
                        file.write(redirect + " " + website + "\n")
        else:
            with open(hosts_path, 'r+') as file:
                content=file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in list_of_websites_to_block):
                        file.write(line)
    
                # removing hostnmes from host file
                file.truncate()
    
            print("Fun hours")
        time.sleep(5)

############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    block_websites_from_list()
import time
import sys

#.__                    .___  .___     .__                .__  ._____.   ________  
#|  |   _________     __| _/__| _/____ |  | _____  ___.__.|  | |__\_ |__ \_____  \ 
#|  |  /  _ \__  \   / __ |/ __ |/ __ \|  | \__  \<   |  ||  | |  || __ \  _(__  < 
#|  |_(  <_> ) __ \_/ /_/ / /_/ \  ___/|  |__/ __ \\___  ||  |_|  || \_\ \/       \
#|____/\____(____  /\____ \____ |\___  >____(____  / ____||____/__||___  /______  /
#                \/      \/    \/    \/          \/\/                  \/       \/ 
#-----v1.2

class delay:
    def print(words, delay):
        d2 = float(delay)
        for char in words:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(d2)
        sys.stdout.write("""
""")
        sys.stdout.flush()
    def in_pr(words, delay):
        d2 = float(delay)
        for char in words:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(d2)


# DEBUG STUFF
ERROR = '\033[91m' # Red
WARNING = '\033[93m' # Yello
NORMAL = '\033[0m' # Black
GOOD = '\033[92m' # Green

def errorMessage(*items):
    global ERROR
    out = ERROR + "[-] "
    for item in items:
        out += str(item)
    print out + NORMAL

def warningMessage(*items):
    global WARNING
    out = WARNING + "[-] "
    for item in items:
        out += str(item)
    print out + NORMAL

def infoMessage(*items):
    global NORMAL
    out = NORMAL + "[+] "
    for item in items:
        out += str(item)
    print out + NORMAL    

def goodMessage(*items):
    global GOOD
    out = GOOD + "[*] "
    for item in items:
        out += str(item)
    print out + NORMAL

if __name__ == "__main__":
    errorMessage("FAILED TO INIT SOMETHING")
    warningMessage("The baby is in the oven")
    infoMessage("I LIKE TRAINS")
    goodMessage("The oven is off")
    print "NOWAI"


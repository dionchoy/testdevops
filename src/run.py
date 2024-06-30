import os
from threading import Thread

def startServer():
    os.system('python -m http.server --d webpage')

def startWebpage():
    os.system('python webpage/webpage.py')
def startLib():
    os.system('python libInterface.py')

def main():
    serverThread = Thread(target=startServer)
    webpageThread = Thread(target=startWebpage)
    libThread = Thread(target=startLib)

    serverThread.start()
    webpageThread.start()
    libThread.start()

if __name__ == "__main__":
    main()


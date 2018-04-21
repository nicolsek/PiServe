# client.py -- The client, ever leeching off of the server.

import socket
import json
import sys

def fail(msg):
    print("[!] " + msg)
    sys.exit(0)

class Client:
    def __init__(self, address, port):
        self.address = address
        self.port = int(port)

        self.socket = socket.socket()

    def send(self, conn, data):
        if sys.version_info[0] > 2:
            data = data.encode()

        conn.send(data)
        conn.close()    

    def serve(self, URL):
        try: 
            conn = self.socket.connect((self.address, self.port))
        except:
            fail("Could not connect to server.")
        
        self.send(conn, URL)
        conn.close()

def parseJSON(jsonObj, key):
    return jsonObj[key]

def loadFile():
    with open('config.json', 'r') as fileObj:
        return json.load(fileObj)

if __name__ == "__main__":
    data = loadFile()
    config = parseJSON(data, 'config')
    address, port = parseJSON(config, 'address'), parseJSON(config, 'port')
    
    if len(sys.argv) != 2:
        fail("Not enough arguments. Expected 1.")

    URL = sys.argv[1]

    client = Client(address, port)
    client.serve(URL)
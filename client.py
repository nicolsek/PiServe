# client.py -- The client, ever leeching off of the server.

import socket
import json
import sys

class Client:
    def __init__(self, address, port):
        self.address = address
        self.port = int(port)

        self.socket = socket.socket()

    def serve(URL):
        conn = socket.connect((self.address, self.port))
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

    client = Client(address, port)
    client.serve()
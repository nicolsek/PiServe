# server.py -- The server always listening... Forever.

import socket
import json
import sys

class Server:
	def __init__(self, interface, port):
		self.interface = interface
		self.port = int(port)

		self.socket = socket.socket()

	def serve(URL):
		os.makedirs('repo')
	
	def disconnect(self, conn):	
		conn.close()

	def recv(data):
		data = self.socket(4096)

		if (sys.version[0] > 2):
			data = data.decode()
	
		return data	

	def listen(self):
		self.socket.bind((self.interface, self.port))
		self.socket.listen(1)

		print('Listening on ', self.interface, 'at', str(self.port))

		addr, conn = self.socket.accept()
	
		with conn:
			data = recv(data)
			self.serve(data)

def loadFile():
	with open('config.json', 'r') as fileObj:
		return json.load(fileObj)	

def parseJSON(jsonObj, key):
	return jsonObj[key]	

if __name__ == "__main__":	
	data = loadFile()

	config = parseJSON(data, 'config')

	interface, port = parseJSON(config, 'interface'), parseJSON(config, 'port')

	server = Server(interface, port)
	server.listen() 

# server.py -- The server always listening... Forever.

# TODO ------ Cross compatibility from python3 to python2.

import http.server
import socketserver

# TODO ------ Cross compatibility from python3 to python2.

import subprocess
import socket
import json
import sys
import os

def fail(msg):
	print("[!] " + msg)
	sys.exit()

def inform(msg):
	print("[*] " + msg)

class Server:
	def __init__(self, interface, port):
		self.interface = interface
		self.port = int(port)

		self.socket = socket.socket()

	def recv(self, conn, buffer):
		data = conn.recv(buffer)

		if sys.version_info[0] > 2:
			data = data.decode()
		
		return data

	def serve(self, URL):
		self.socket.close()

		subprocess.call(["rm", "-rf", "repo/"])
		subprocess.call(["mkdir", "repo"])
		subprocess.call(["git", "clone", URL, "repo"])

		os.chdir("repo")

		handler = http.server.SimpleHTTPRequestHandler

		with socketserver.TCPServer((self.interface, self.port), handler) as httpd:
			httpd.serve_forever()

			inform("Serving at " + self.interface + " on " + self.port)
		
	def listen(self):
		try:
			self.socket.bind((self.interface, self.port))
			self.socket.listen(1)
		except:
			fail("Could not bind or listen to interface.")
		
		inform("Listening on interface: [" + interface + "]")
		conn, addr = self.socket.accept()

		with conn:
			try:
				data = self.recv(conn, 4096)
			except:
				conn.close()
				self.socket.close()
				fail("Could not recieve data from connection.")

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
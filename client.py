# -*- coding: utf-8 -*-
import socket #for sockets
import rsa
import cPickle

(pub_keyz, priv_key) = rsa.newkeys(512)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket Created")

to_send = cPickle.dumps(pub_keyz)

#Get host and port info to connect
host = '127.0.0.1' # qua l'ip del server a cui connettersi
port = 4444
s.connect((host, port))

ks = s.recv(1024)
pub_key=cPickle.loads(ks)
print "Key server ricevuta"

s.send(to_send)

while True:
	#encoding e encrypt del messaggio
	message = raw_input("scrivi qua il messaggio=> ")
	message = message.encode('utf8')
	encrypt = rsa.encrypt(message, pub_key)

	#invio del messaggio criptato
	s.send(encrypt)

	data = s.recv(1024)
	decrypt = rsa.decrypt(data, priv_key)
	print decrypt.decode('utf8')

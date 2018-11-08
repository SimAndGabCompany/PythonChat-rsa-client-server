import socket
import rsa
import cPickle

(pub_keyz, priv_key) = rsa.newkeys(512)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

to_send=cPickle.dumps(pub_keyz)

host = '127.0.0.1'
port = 4444

s.bind((host,port))
s.listen(1)

conn, addr = s.accept()
conn.send(to_send)

kc = conn.recv(1024)
pub_key = cPickle.loads(kc)
print "Key client ricevuta"

while True:
    data = conn.recv(1024)
    decrypt = rsa.decrypt(data, priv_key)
    print decrypt.decode('utf8')

    message = raw_input("Inserisci il messaggio qui => ")
    message = message.encode('utf8')
    encrypt = rsa.encrypt(message, pub_key)
    conn.send(encrypt)

conn.colse()

import socket

site = input('Digite aqui o site: ')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('whois.iana.org', 43))
s.send((site +'\r\n').encode())
resposta = s.recv(1024).split()
whois = resposta[19]
s.close()

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect((whois, 43))
s1.send((site + '\r\n').encode())
resp = s1.recv(1024)

print(resp)
from socket import *
from threading import *
import sys
import nmap

requestHeader = 'GET %s HTTP/1.0\r\nHost: %s\r\n\r\n'

def portScan(host, port):
	try:
		skt = socket(AF_INET, SOCK_STREAM)
		skt.connect((host,port))
		#print('connect successfully')
		skt.send('PythonScanner')	#'PythonScanner'
		results = skt.recv(100)
		print('[+] %d/tcp'% port)
		print('[+] ' + str(results))
		skt.close()
	except :
		print('[-] %d/tcp close'% port)
		

def nmapScan(host, port):
	nmScan = nmap.PortScanner()
	nmScan.scan(host, port)
	state = nmScan[host]['tcp'][int(port)]['state']
	print('[*] %s tcp/%s %s'% (host, port, state))

	pass


def main():
	host = sys.argv[1]
	start = int(sys.argv[2])
	end = int(sys.argv[3])
	for port in range(start, end+1):
		t = Thread(target = nmapScan, args = (host, str(port)))
		t.start()
if __name__ == '__main__':
	main()
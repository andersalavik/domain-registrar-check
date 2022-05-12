import whois
import time

domains = open("domains.txt",'r')



for domain in domains.readlines():
	print('')
	print('Kontrollerar:',domain.strip('\n'))
	try:
		w = whois.whois(domain.strip('\n'))
		print('Registrar:',w['registrar'])
		print('Status:',w['status'])
		print('Name server:',w['name_servers'])
	except:
		print('Hittar inte')
	
	time.sleep(0.5)
	
	
	
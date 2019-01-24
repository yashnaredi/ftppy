import ftplib




#filename = 

def ftp_connect():
	while True:
		site_address = input('Please enter the FTP address:')
		username= input('enter username')
		password= input('enter password')
		try:
			with ftplib.FTP(site_address) as ftp:
				ftp.login(user=username,passwd=password)
				print(ftp.getwelcome())
				print('Current Directory', ftp.pwd())
				ftp.dir()
				print('Valid commands are cd/get/ls/upl/exit')
				print('Ex get readme.txt')
				ftp_command(ftp)
				break
		except ftplib.all_errors as e:
			print('Connection Failure,Check your input',e)





def ftp_commands(ftp):
	while True:
		command = input('enter a command:')
		commands = command.split()

		if commands[0] == 'cd': #change directory
			try:
				ftp.cwd(commands[1])
				print('Directory of', ftp.pwd())
				ftp.dir()
				print('Current Directory',ftp.pwd())
			except ftplib.error_perm as e:
				error_code = str(e).split(None,1)
				if error_code[0] == '550':
					print(error_code[1],'Directory not found')
		elif commands[0] =='get': #file download
			try:
				ftp.retrbinary('RETR '+ commands[1], open(commands[1], 'wb').write)
				print('file downloaded')
			except ftplib.error_perm as e:
				error_code = str(e).split(None,1)
				if error_code[0] == '550':
					print(error_code[1],'File not found')
		elif commands[0] =='ls': #lists all the files
			print('Directory of',ftp.pwd())
			ftp.dir()
		elif commands[0] =='upl':
			
			file = open(commands[1],'rb')                 # file to send
			ftp.storbinary('STOR '+commands[1], file)
			print('file uploaded')
		elif commands[0] == 'exit':
			ftp.quit()
			print('goodbye')
			break
		else:
			print('invalid input,try again')

print('Welcome to Python FTP client')
ftp_connect()












	
	#myfile  = open('/Users/yashnaredi/desktop/ftppy/test.html','rb')
	#ftp.storlines('STOR '+ filename, myfile)
	#print('file uploaded')









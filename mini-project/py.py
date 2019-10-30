#modules used...
import sys, pickle
import subprocess as sp





#creating files....





#class user.....starts here
class user:
    
    #class user: >__init__()
	def __init__(self):                                               
		self.flag = flag = 0
		self.ex = ex = 0
		self.name = name = ''

    
    #class user: >userfunc()
	def userfunc(self):
		users = []

		inp = input('Existing user? y/n')

		if inp == 'n':

			while True:
				flag = 0

				ent = input('new username : ')
				self.name = ent	

				try:
					with open('user', 'rb') as u:
						users = pickle.load(u)

				except EOFError:
					users.append(ent)	
					with open('user', 'wb') as u:
						pickle.dump(users, u)
					flag = 2

					passwrd = input('Enter password : ')



					try:
						with open('all_user_data', 'rb') as aud:
							all_user_data = pickle.load(aud)

					except EOFError:
						all_user_data = {}
						all_user_data[self.name] = {}
						all_user_data[self.name]['pass'] = passwrd	

						with open('all_user_data', 'wb') as aud:
							pickle.dump(all_user_data, aud)

					else:
						with open('all_user_data', 'rb') as aud:
							all_user_data = pickle.load(aud)

						all_user_data[self.name] = {}
						all_user_data[self.name]['pass'] = password	

						with open('all_user_data', 'wb') as aud:
							pickle.dump(all_user_data, aud)


					finally:
						print('\nlogin success....\n')	




				else:
					with open('user', 'rb') as u:
						users = pickle.load(u)
					flag = 3				


					for username in users:
						if username == ent:
							flag = 1
							print('\n Already taken...try another\n')
							
							break

				if flag == 3:
					users.append(ent)

					passwrd = input('Enter password : ')


					with open('all_user_data', 'rb') as aud:
						all_user_data = pickle.load(aud)

					all_user_data[self.name] = {}
					all_user_data[self.name]['pass'] = passwrd	

					with open('all_user_data', 'wb') as aud:
						pickle.dump(all_user_data, aud)
			


					with open('user', 'wb')	as u:
						pickle.dump(users, u)
						print('\nlogin success....\n')
					break

				if flag == 2:
					break		

					
			
				




		elif(inp == 'y')    	:
			ent = input('Username : ')

			try:
				with open('user', 'rb') as u:
					users = pickle.load(u)

				with open('all_user_data', 'rb') as aud:
					all_user_data = pickle.load(aud)	

			except EOFError:
				print('no match found...\nexitting..')
				sys.exit()

			else:
				with open('user', 'rb') as u:
					users = pickle.load(u)	
						



				if ent in users:
					
					with open('all_user_data', 'rb') as aud:
						all_user_data = pickle.load(aud)

					password = input('Enter password : ')	

					if all_user_data[ent]['pass'] == password:
						print('access granted...')
						

						self.ex = 1                                
						self.name = ent	

					else:
						print('incorrect password...')
						sys.exit()


				else:
					print('invalid username...')	
					sys.exit()












#admin class........starts here
class admin:



    #class admin > __init__()
	def __init__(self): 

		self.flag = flag = 0
		self.access = access = 0



    #class admin > auth() -->> to authenticate the admin to make changes to hardwares.... 
	def auth(self):


		                                   
		ent = input('\n\nenter password : ')

		
		try:
			with open('password', 'rb')	as f:
				passwrd = pickle.load(f)

		except EOFError:
			passwrd = 'admin'
			self.flag = 1
			with open('password', 'wb') as f:
				pickle.dump(passwrd, f)	

		finally:
			with open('password', 'rb') as f:
				passwrd = pickle.load(f)			

		



			if ent == passwrd:
				self.flag = 1
			  
    


    
	def changepass(self):

		
		passwrd = input('\nExisting password : ')

		with open('password', 'rb') as f:
			p = pickle.load(f)


		if passwrd == p:
			print('Access granted......')
			self.access = 1	

		else:
			print('access denied.....')    
			sys.exit()

		if self.access == 1:
			
			new_pass = input('\n\nEnter new password : ')

			with open('password', 'wb') as f:
				pickle.dump(new_pass, f)

			print('\n\npassword changed successfully')	


	def rem_user(self):

		users = []
		all_user_data = {}

		

		try:
			with open('user', 'rb') as u:
				users = pickle.load(u)

		except EOFError:
			print('\n No user in the list...\n')	

		else:
			with open('user', 'rb') as u:
				users = pickle.load(u)

			for user_name in users:
				print(user_name)

			rem = input('\n\nUsername : ')		

			if rem in users:
				users.remove(rem)

				with open('all_user_data', 'rb') as aud:
					all_user_data = pickle.load(aud)

				try:	
					all_user_data.pop(rem, None)

				except KeyError:
					print('No user found...')
					sys.exit()

				else:	
					all_user_data.pop(rem, None)

					with open('user', 'wb') as u:
						pickle.dump(users, u)

					with open('all_user_data', 'wb') as aud:
						pickle.dump(all_user_data, aud)

					print('user removed...')	

			else:
				print('\nno such user exists....\n')	


	def disp_userdata(self):

		try:
			with open('all_user_data', 'rb') as aud:
				all_user_data = pickle.load(aud)

		except EOFError:
			print('Empty....user list')

		else:
			with open('all_user_data', 'rb') as aud:
				all_user_data = pickle.load(aud)

			f = 0	

			with open('user', 'rb') as u:
				users = pickle.load(u)

			for user_name in users:
				print(user_name)

			print('\n')	

			name = input('\nenter username : ')



			for username, data in all_user_data.items():
				if username == name:

					f = 1	
					n = 0
					y = 0
					d = 0				
					
					print('\nPASSWORD : ')
					print(data['pass'], end = '\n\n')

					print('RAM : ')

					try:
						

						for i, j in data['ram'].items():
							print(i, end = ' -> ')

							for m, n in j.items():
								print(m, '->', 'Rs.',  n)

					except KeyError:
						print('No ram selected\n')		

												

					

					print('\nMOTHERBOARD :')

					try:

						for x,y in data['mobo'].items():
							print(x,'Rs.', y)

					except KeyError:
						print('No mobo selected')

					



					print('\nPROCESSOR :')	

					try:

						for a, b in data['pro'].items():
							print(b, end = ' -> ')

							for c, d in j.items():
								print(c,'->','Rs.', d)

					except KeyError:
						print('No processor selected')

															


					print('\nTOTAL PRICE : Rs.', int(n) + int(y) + int(d))		

					break		



		if f == 0:
			print('No user found....')				
							


























#class ram ...... startas here
class ram:




	def display(self):
		ram = {}

		try:
			with open('ram', 'rb') as r:
				ram  = pickle.load(r)

		except EOFError:
			print('nothings here')

		else:
			with open('ram', 'rb') as r:
				ram  = pickle.load(r)
						

		

		

		for key, value in ram.items():
			print(f'\n\n{key} :')

			for i, j in ram[key].items():
				print(i, ' : ', j)
		




	def append(self):

		
		inp = int(input('1. ram\t\t2. ram_type\n'))

		ram = {}
		ram1 = ''
		ram2 = []
		price = []
		new_ram = {}


		if inp == 1:
			
			ram1 = input('\n\nEnter ram name : ')

			
			ram2 = input('\nEnter ramtypes : ').split()

			print('Price of ram types : \n')
			for item in ram2:
				print('\n', item, ' : ')
				ent = int(input())
				price.append(ent)



			for i in range(len(ram2)):
				new_ram[ram2[i]] = price[i]	

			pic = 0	

			try:	
				with open('ram', 'rb') as r:
					ram = pickle.load(r)

			except EOFError:
				ram[ram1] = new_ram
				with open('ram', 'wb') as r:
					pickle.dump(ram, r)

				pic = 1	

			else:
				with open('ram', 'rb') as r:
					ram = pickle.load(r)


			if pic != 1:		
				ram[ram1] = new_ram


				with open('ram', 'wb') as r:
					pickle.dump(ram, r)





		elif inp == 2:
			ram2 = ''
			ram = {}
			try:
				with open('ram', 'rb') as r:
					ram = pickle.load(r)

			except EOFError:
				print('\nnothings here...')

			else:	
				with open('ram', 'rb') as r:
					ram = pickle.load(r)

			
			
			ram1 = input('\n\nEnter ram name : ')

			if ram1 in ram:
				pass
			else:
				print('\n\ninvalid ram...')	
				sys.exit()

			print('\nEnter ramtype and price : ')
			ram2, price = input().split()
			price = int(price)

			

			ram[ram1][ram2] = price	

			with open('ram', 'wb') as r:
				pickle.dump(ram, r)





	



	def search(self):

		
		ent = input('\n\nEnter ram name : ')

		try:
			with open('ram', 'rb') as r:
				ram  = pickle.load(r)

		except EOFError:
			print('nothings here')

		else:
			with open('ram', 'rb') as r:
				ram  = pickle.load(r)



		try:	
			displ = ram[ent]

		except KeyError:
			print('invalid search...')
			sys.exit()


		print('\n\nram : ', ent)
		for key, value in displ.items():
			print(key, ' : ', value, '\n')








	def delete(self):

		flag = 0
		inp = 0

		

		try:
			
			inp = int(input('1. ram\t\t2. ram_type : '))

		except ValueError:
			print('invalid entry..')

		else:
			inp = int(input('1. ram\t\t2. ram_type : '))		

		if inp == 1:
			
			ram1 = input('\n\nEnter ram name : ')

			try:
				with open('ram', 'rb') as r:
					ram  = pickle.load(r)

			except EOFError:
				print('nothings here')

			else:
				with open('ram', 'rb') as r:
					ram  = pickle.load(r)

			if ram1 in ram:
				pass

			else:
				print('\n\ninvalid ram...')
				sys.exit()		

			for key, value in ram.items():

				if key == ram1:
					ram.pop(key)
					flag = 1
					ram.update(ram)

					with open('ram', 'wb') as r:
						pickle.dump(ram, r)
					print('ram deleted successfully..')	

					break	

			if flag == 0:
				print('\n\nno such ram exists....')
				sys.exit()

			
				    


	    
		elif(inp == 2):

			flag = 0

			
			ram1 = input('\n\nEnter ram name : ')

			with open('ram' , 'rb') as r: 
				ram = pickle.load(r)

			if ram1 in ram:
				pass

			else:
				print('\n\ninvalid ram...')
				sys.exit()		

			
			ram2 = input('\nenter ram type : ')

			

			for key, value in ram.items():

				if key == ram1:
					ram[key].pop(ram2)
					flag = 1
					ram[key].update(ram[key])

					with open('ram', 'wb') as r:
						pickle.dump(ram, r)

					print('\nram_type deleted successfully...')	

					break	

			if flag == 0:
				print('\n\nno such ram_type exists....')
				sys.exit()




			
	    	
	    	

















#class mobo ...... startas here
class mobo:

	def __init__(self):
		pass



	def display(self):
		mobo = {}

		try:
			with open('mobo', 'rb') as m:
				mobo  = pickle.load(m)

		except EOFError:
			print('\nnothings, here')

		else:
			with open('mobo', 'rb') as m:
				mobo  = pickle.load(m)	


		for key, value in mobo.items():
			print(key, ' : ', value, '\n')	




	def append(self):

		mobo = {}

		mobo_type, price = input('\n\nEnter mobo type and price : ').split()
		int(price)

		try:
			with open('mobo', 'rb') as m:
				mobo  = pickle.load(m)

		except EOFError:
			mobo[mobo_type]	= price

			with open('mobo', 'wb') as m:
				pickle.dump(mobo, m)
			
		else:
			with open('mobo', 'rb') as m:
				mobo  = pickle.load(m)

		mobo[mobo_type]	= price

		with open('mobo', 'wb') as m:
			pickle.dump(mobo, m)



	
	def search(self):

		flag = False
		

		mobo_type = input('\n\nenter mobo_type to search : ')

		try:
			with open('mobo', 'rb') as m:
				mobo  = pickle.load(m)

		except EOFError:
			print('\nnothings, here')
			
		else:
			with open('mobo', 'rb') as m:
				mobo  = pickle.load(m)

		flag = mobo_type in mobo

		if flag == True:
			print(mobo_type, ' : ', mobo[mobo_type])	

		else:
			print('Invalid search.....')    




	def delete(self):

		
		delete = input('Enter mobo_type : ')

		try:
			with open('mobo', 'rb') as m:
				mobo  = pickle.load(m)

		except EOFError:
			print('\nnothings, here')
			
		else:
			with open('mobo', 'rb') as m:
				mobo  = pickle.load(m)

		flag = delete in mobo	

		if flag == True:
			print('mobo deleted')
			mobo.pop(delete)
			mobo.update(mobo)

		else:
			print('invalid deletion...')
	        	






















#class processor ...... startas here
class processor:


	def __init__(self):
		pass




	def display(self):
		pro = {}
		try:

			with open('processor', 'rb') as p:
				pro  = pickle.load(p)

		except EOFError:
			print('nothings here')

		else:			
			with open('processor', 'rb') as p:
				pro  = pickle.load(p)	

		

		for key, value in pro.items():
			print(f'\n\n{key} :')

			for i, j in pro[key].items():
				print(i, ' : ', j)



	def append(self):

		
		inp = int(input('1. processor\t\t2. processor_type\n'))

		pro = {}
		pro1 = ''
		pro2 = []
		price = []
		new_pro = {}


		if inp == 1:
			
			pro1 = input('\n\nEnter processor name : ')

			print()
			pro2 = input('\nEnter processor_types : ').split()

			print('Price of processor types : \n')
			for item in pro2:
				print('\n', item, ' : ')
				ent = int(input())
				price.append(ent)



			for i in range(len(pro2)):
				new_pro[pro2[i]] = price[i]	

			pic = 0	

			try:	
				with open('processor', 'rb') as p:
					pro = pickle.load(p)

			except EOFError:
				pro[pro1] = new_pro
				with open('processor', 'wb') as p:
					pickle.dump(pro, p)

				pic = 1	

			else:
				with open('processor', 'rb') as p:
					pro = pickle.load(p)


			if pic != 1:		
				pro[pro1] = new_pro


				with open('processor', 'wb') as p:
					pickle.dump(pro, p)





		elif inp == 2:
			pro2 = ''

			with open('processor', 'rb') as p:
				pro = pickle.load(p)
			
			
			pro1 = input('\n\nEnter processor name : ')

			if pro1 in pro:
				pass
			else:
				print('\n\ninvalid processor...')	
				sys.exit()

			
			pro2, price = input('\nEnter processor_type and price : ').split()
			price = int(price)

			

			pro[pro1][pro2] = price	

			with open('processor', 'wb') as p:
				pickle.dump(pro, p)






	

	def search(self):

		
		ent = input('\n\nEnter processor name : ')

		try:
			with open('processor', 'rb') as p:
				pro = pickle.load(p)

		except EOFError:
			print('nothings here')

		else:
			with open('processor', 'rb') as p:
				pro = pickle.load(p)
						
				
		try:	
			displ = pro[ent]

		except KeyError:
			print('\ninvalid search...')
			sys.exit()


		print('\n\nprocessor : ', ent, '\n')
		for key, value in displ.items():
			print(key, ' : ', value)







	def delete(self):

		
		inp = int(input('\n\n1. ram\t\t2. ram_type'))


		if inp == 1:
			pro1 = input('\nEnter processor name : ')

			try:
				with open('processor', 'rb') as p:
					pro = pickle.load(p)

			except EOFError:
				print('nothings here')

			else:
				with open('processor', 'rb') as p:
					pro = pickle.load(p)
							

			for key in pro.items():
				if key == ram1:
					pro.pop(key, None)
					flag = 1
					break	

			if flag != 0:
				print('\n\nno such key exists....')

			elif flag == 1:
				with open('processor', 'wb') as p:
					pickle.dump(pro, p)    


	    
		elif(inp == 2):

			
			pro1 = input('\n\nEnter processor name : ')

			
			pro2 = input('\nenter processor type : ')

			try:
				with open('processor' , 'rb') as p: 
					pro = pickle.load(p)

			except EOFError:
				print('nothings here...')

			else:
				with open('processor' , 'rb') as p: 
					pro = pickle.load(p)
							

			for key in pro.items():

				if key == pro1:
					pro[key].pop(pro2, None)
					flag = 1
					break

			if flag != 0:
				print('\n\nno such key exists....')

			elif flag == 1:
				with open('processor', 'wb') as p:
					pickle.dump(pro, p)        	

	    	
	    	







#creating the objects of the class....
u = user()
a = admin()
r = ram()
m = mobo()
p = processor()






#global function...
def new_details(m, p, r, u):

	all_user_data = {}

	print('\n Enter ur choice : \n')
	
	e = int(input('1. Ram\n2. Motherboard\n3. Processor\n4. Exit\n'))




	if e == 1:
		print('\navailable rams : ')
		r.display()

		ram, ram_type = input('\n\nEnter ram, ram_type : ').split()

		with open('ram', 'rb') as r:
			all_ram = pickle.load(r)

		if ram in all_ram and ram_type in all_ram[ram]:

			try:
				with open('all_user_data', 'rb') as aud:
					all_user_data = pickle.load(aud)

			except EOFError:
				all_user_data[u.name] = {}
				all_user_data[u.name]['ram'] = {}
				all_user_data[u.name]['ram'][ram] = {}
				all_user_data[u.name]['ram'][ram][ram_type] = all_ram[ram][ram_type]

				with open('all_user_data', 'wb') as aud:
					pickle.dump(all_user_data, aud)

			else:
				with open('all_user_data', 'rb') as aud:
					all_user_data = pickle.load(aud)
						
				
				all_user_data[u.name]['ram'] = {}
				all_user_data[u.name]['ram'][ram] = {}
				all_user_data[u.name]['ram'][ram][ram_type] = all_ram[ram][ram_type]

				with open('all_user_data', 'wb') as aud:
						pickle.dump(all_user_data, aud)		
						

		else:
			print('no such entry found...')
			sys.exit()		
					



	elif e == 2:
		print('\nAvailable Motherboards : ')
		m.display()

		
		mobo = input('\nEnter mobo type : ')

		with open('mobo', 'rb') as m:
			all_mobo = pickle.load(m)

		if mobo in all_mobo:
			try:
				with open('all_user_data', 'rb') as aud:
					all_user_data = pickle.load(aud)

			except EOFError:
				
				all_user_data[u.name]['mobo'] = {}
				all_user_data[u.name]['mobo'][mobo] = all_mobo[mobo]
				with open('all_user_data', 'wb') as aud:
					pickle.dump(all_user_data, aud)	

			else:
				with open('all_user_data', 'rb') as aud:
					all_user_data = pickle.load(aud)
				
				all_user_data[u.name]['mobo'] = {}
				all_user_data[u.name]['mobo'][mobo] = all_mobo[mobo]

				with open('all_user_data', 'wb') as aud:
					pickle.dump(all_user_data, aud)
		else:
			print('no such entry found...')
			sys.exit()		




	elif e == 3:
		print('\nAvailable processors : \n')
		p.display()

		pro, pro_type = input('Enter processor and its type : ').split()	

		with open('processor', 'rb') as p:
			all_pro = pickle.load(p)

		if pro in all_pro and pro_type in all_pro[pro]:
			try:
				with open('all_user_data', 'rb') as aud:
					all_user_data = pickle.load(aud)
			except EOFError:		
				
				all_user_data[u.name]['pro'] = {}
				all_user_data[u.name]['pro'][pro] = {}
				all_user_data[u.name]['pro'][pro][pro_type] = all_pro[pro][pro_type]

				with open('all_user_data', 'wb') as aud:
					pickle.dump(all_user_data, aud)

			else:
				with open('all_user_data', 'rb') as aud:
					all_user_data = pickle.load(aud)

					
				all_user_data[u.name]['pro'] = {}
				all_user_data[u.name]['pro'][pro] = {}
				all_user_data[u.name]['pro'][pro][pro_type] = all_pro[pro][pro_type]	

				with open('all_user_data', 'wb') as aud:
					pickle.dump(all_user_data, aud)	

		else:
			print('no such entry found...')
			sys.exit()

			
	elif e == 4:
		print('exiting...')
		sys.exit()				













def display_details(m, p, r, u):

	n = 0
	y = 0
	d = 0

	all_user_data = {}

	try:
		with open('all_user_data', 'rb') as aud:
			all_user_data = pickle.load(aud)

	except EOFError:
		print('no previous details exists..')

	else:
		with open('all_user_data', 'rb') as aud:
			all_user_data = pickle.load(aud)

			f = 0

	
		
		for username, data in all_user_data.items():

			if username == u.name:
				
								
				print('\nPASSWORD : ')
				print(data['pass'], end = '\n\n')


				print('RAM : ')

				try:
						

					for i, j in data['ram'].items():
						print(i, end = ' -> ')

						for m, n in j.items():
							print(m, '->', 'Rs.',  n)

				except KeyError:
					print('No ram selected\n')		

				

				

				print('\nMOTHERBOARD :')

				try:

					for x,y in data['mobo'].items():
						print(x,'Rs.', y)

				except KeyError:
					print('No mobo selected')

				


				print('\nPROCESSOR :')	

				try:

					for a, b in data['pro'].items():
						print(a, end = ' -> ')

						for c, d in j.items():
							print(c,'->','Rs.', d)

				except KeyError:
					print('No processor selected')

				


				print('\nTOTAL PRICE : Rs.', int(n) + int(y) + int(d))		

				f = 1

				break

	if f == 0:
		print('No previous details...')		
					




	











#the main() program starts here......


while True:

	adminnn = 0

	print('.........WELCOME..........')
	inp = int(input('1. Admin\n2. User\n'))

	if inp == 1:
		adminnn = 1

		counter = 0


		for _ in range(4):
			a.auth()


			if a.flag == 1:
				
				print('access granted....')
				counter = 1
				break

			else:
			    print(f'\n{3 - _} chances left..\n\n')


		if counter == 0:
			sys.exit()	    	



		while True:	

			wht = int(input('\n\n1. Change admin password\n2. Change database\n3. Remove User data\n4. Display user data\n'))



		
			if wht == 1:
				a.changepass()



			elif wht == 2:
				while True:

					ch = int(input('1. Ram\n2. Processor\n3. Motherboard\n'))

					if ch == 1:
						print('\nno. of operations you can perform :\n ')
						ram_choice = int(input('1. Delete\n2. Search\n3. Append\n4. Display\n'))

						if ram_choice == 1:
							r.delete()

						elif ram_choice == 2:
							r.search()

						elif ram_choice == 3:
							r.append()

						elif ram_choice == 4:
							r.display()

						else:
							print('...wrong entry...')  
							sys.exit()  	

					
					elif ch == 2:
						print('\nno. of operations you can perform :\n ')
						print('1. Delete\n2. Search\n3. Append\n4. Display\n')
						pro_choice = int(input())

						if pro_choice == 1:
							p.delete()

						elif pro_choice == 2:
							p.search()

						elif pro_choice == 3:
							p.append()

						elif pro_choice == 4:
							p.display()

						else:
							print('...wrong entry...')  
							sys.exit()  	


					elif ch == 3:
						print('\nno. of operations you can perform :\n ')
						mobo_choice = int(input('1. Delete\n2. Search\n3. Append\n4. Display\n'))

						if mobo_choice == 1:
							m.delete()

						elif mobo_choice == 2:
							m.search()

						elif mobo_choice == 3:
							m.append()

						elif mobo_choice == 4:
							m.display()

						else:
							print('...wrong entry...')  
							sys.exit()  	


					else:
						print('\ninvalid entry...')
						break		


					cont = input('\n\ndo u want to cont...? y/n')
					if cont == 'n':
						break	

			elif wht == 3:
				a.rem_user()

			elif wht == 4:
				a.disp_userdata()
								
					


			edit = input('\nexit admin? y/n')
			
			print('\n\n')

			if edit == 'y':
				sp.call('cls',shell=True)
				break

			elif edit == 'n':
				pass

			else:
				print('invalid entry...')
				sys.exit()		


		

			
			
			

















	elif inp == 2:
		adminnn = 0
		u.userfunc()

		while True:



			if u.ex == 0:
				disp = int(input('\n1. Dispaly previous details\n2. Enter new details\n'))

				if disp == 1:
					display_details(m, p, r, u)

				elif disp == 2:
					new_details(m, p, r, u)

				else:
					print('invalid entry....')
					sys.exit()			



			elif u.ex == 1:
				disp = int(input('\n1. Dispaly previous details\n2. Enter new details\n'))

				if disp == 1:
					display_details(m, p, r, u)

				elif disp == 2:
					new_details(m, p, r, u)

				else:
					print('invalid entry....')
					sys.exit()



			cont = input('\ndo u want to cont..? y/n : ')
			print('\n\n')
	 		
			if cont == 'n':
				sp.call('cls',shell=True)
				break    	




	else:
		print('invalid entry...')
		sys.exit()


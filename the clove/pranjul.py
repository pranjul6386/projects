

#importing libraries
import tkinter
from tkinter import *
from tkinter.ttk import *
import urllib.request
import time
import csv
import numpy as np
import pandas as pd
from tkinter import messagebox



flat = 0
flag = 0



root_url = "192.168.137.73"  # ESP's url, ex: https://192.168.102 (Esp serial prints it when connected to wifi)








dataset=pd.read_csv("data2.csv",error_bad_lines=False)   # read the csv file
x=dataset.iloc[:,:4].values                              # x features
y=dataset.iloc[:,4].values                               # y features



# encoding of months
from sklearn.preprocessing import LabelEncoder           
labelencoder = LabelEncoder()
x[:, 0] = labelencoder.fit_transform(x[:, 0])



# splitting of dataset
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)



# applying algorithm
from sklearn.ensemble import RandomForestClassifier
classifier=RandomForestClassifier()
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)


# confusion matrix for the testing data
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
print(cm)







class sensor():


	def __init__(self):
        
		self.t = t = 0
		self.h = h = 0
		self.soil = soil = 0
		self.smoke = smoke = 0
		self.flame = flame = 0
        

    #requesing for flame(digital)
	def send_flame_request(self, flame_url):
        
		send_flame_url = urllib.request.urlopen(flame_url) # send request to ESP
		flame_data = send_flame_url.readline()
		self.flame = flame_data.decode()
		print('flame : ', self.flame)


		
			

		

    #requesting for smoke(analog)
	def send_smoke_request(self, smoke_url):

		send_smoke_url = urllib.request.urlopen(smoke_url) # send request to ESP
		smoke_data = send_smoke_url.readline()
		self.smoke = smoke_data.decode()
		print('smoke : ', self.smoke)
		





		

			


    #requesting for temperature(analog)
	def send_temp_request(self, temp_url):

		send_temp_url = urllib.request.urlopen(temp_url) # send request to ESP
		temp_data = send_temp_url.readline()
		self.t = temp_data.decode()
		print('temp : ', self.t)
		return self.t



    #requesting for humidity(analog)
	def send_humidity_request(self, humidity_url):

		send_humidity_url = urllib.request.urlopen(humidity_url) # send request to ESP
		humidity_data = send_humidity_url.readline()
		self.h = humidity_data.decode()
		print('humidity : ', self.h) 
		return self.h




    #requesting for soil moisture(analog)
	def send_soil_moisture_request(self, soil_moisture_url):

		send_soil_moisture_url = urllib.request.urlopen(soil_moisture_url) # send request to ESP
		soil_moisture_data = send_soil_moisture_url.readline()
		self.soil = soil_moisture_data.decode()
		print('soil_moisture : ', self.soil)
		return self.soil






s = sensor()


def clicked():

	
		



	while True:



		if s.smoke == 1 or s.flame == 1:
		
			
			

			root.destroy()

			time.sleep(2)


			room = tkinter.Tk()
			


			messagebox.showwarning("LOCATION 1","EMERGENCY!!!")


        



		s.send_flame_request('http://' + root_url + "/flame")
		

            
                

		s.send_smoke_request('http://' + root_url + "/smoke")
		
            
                

		s.send_temp_request('http://' + root_url + "/temp")
            
                

		s.send_humidity_request('http://' + root_url + "/humidity")
            
                
		s.send_soil_moisture_request('http://' + root_url + "/soil_moisture")

		print('\n')



		





            
            
            



        #getting the current month
		x = time.gmtime()[1]
            
		if x==1:
			month="jan"
		elif x==2:
			month="feb"
		elif x==3:
			month="march"
		elif x==4:
			month="april"
		elif x==5:
			month="may"
		elif x==6:
			month="june"
		elif x==7:
			month="july"
		elif x==8:
			month="aug"
		elif x==9:
			month="sept"
		elif x==10:
			month="oct"
		elif x==11:
			month="nov"
		elif x==12:
			month="dec"



		row = [month, s.soil, s.t, s.h]   

            



		try:
			with open("new1.csv",mode =  "r",newline = '') as fp:
				wr = csv.reader(fp, dialect = 'excel')
                    

		except FileNotFoundError:
			with open("new1.csv",mode =  "w",newline = '') as fp:
				wr = csv.writer(fp, dialect = 'excel')
				wr.writerow(row)        


		else:
			with open("new1.csv",mode =  "a",newline = '') as fp:
				wr = csv.writer(fp, dialect = 'excel')
				wr.writerow(row) 

                
        #empty file to read x features
		dataset2=pd.read_csv("new1.csv",error_bad_lines=False)
		x_apna=dataset2.iloc[:,:4].values
           
            

         #encoding of first column
		from sklearn.preprocessing import LabelEncoder
		labelencoder = LabelEncoder()

		x_apna[:,0] = labelencoder.fit_transform(x_apna[:,0])

            
            

            
            
            
        # predicting the probablity
		y_predict = classifier.predict_proba(x_apna)[:,1]
		print(y_predict[-1])



        
		pgbar['value'] = y_predict[-1]*100
		root.update()



    


        




root = tkinter.Tk()
root.geometry('550x500')

        

    


t = tkinter.Text(root, height = 1, width = 10)
t.pack()
t.insert(tkinter.END, 'LOCATION-1\n')

pgbar = Progressbar(root, length = 200, orient = VERTICAL, maximum = 100, value = 0)



   
btn = Button(root, text = 'Start', command = clicked)

pgbar.pack()
btn.pack()



      

root.mainloop()



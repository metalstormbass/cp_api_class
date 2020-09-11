import getpass
import json
import csv
from login_logout import login
from login_logout import logout
from login_logout import post

#Gather variables from user
ip = input("Management Server Address: ")
user = input("Username: ")
pw = getpass.getpass('Password:')

#Login
sid = login(ip, user, pw)

#Add or delete
selection = raw_input("1. Add host \n2. Delete host\nSelection: ")
if selection == "1":
    command = "add-host"
    print ("Add host selected")
elif selection == "2":
        command = "delete-host"
        print ("Delete host selected")
else:  
        print ("Please enter number 1 or 2")
    
path = input("Enter the file you wish to import. Use forward slashes, even on Windows: ")

csv_file = path
with open(path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    line_count = 0
    for row in csv_reader:
        #Create Variables
        hostname = row[0]
        host_ip = row[1]
        
        #Assemble JSON
        json_data = {}
        json_data['name']=hostname
        json_data['ip-address']=host_ip
        
        #Create hosts and print result.
        result = post(sid, ip, command, json_data)
        print (result)
        
#Publish
print ("Publishing...")
command = "publish"
json_data = {}
result = post(sid, ip, command, json_data)

print (result)

#Logout
logout(sid, ip)



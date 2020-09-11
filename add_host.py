import getpass
import json
from login_logout import login
from login_logout import logout
from login_logout import post

#Gather variables from user
ip = input("Management Server Address: ")
user = input("Username: ")
pw = getpass.getpass('Password:')

#Login
sid = login(ip, user, pw)

#Add Host
command = "add-host"
hostname = raw_input("Enter host name: ")
host_ip = raw_input("Enter host IP address: ")

json_data = {}
json_data['name']=hostname
json_data['ip-address']=host_ip

result = post(sid, ip, command, json_data)

print (result["name"] + " has successfully been created. Publishing now.")

#Publish
command = "publish"
json_data = {}
result = post(sid, ip, command, json_data)

print (result)

#Logout
logout(sid, ip)

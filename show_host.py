import getpass
import json
import requests
from login_logout import login
from login_logout import logout
from login_logout import post

#Gather variables from user
ip = raw_input("Management Server Address: ")
user = raw_input("Username: ")
pw = getpass.getpass("Password: ")

#Login
sid = login(ip, user, pw)

#Show Host
command = "show-host"
hostname = raw_input("Enter host name: ")

json_data = {}
json_data['name']=hostname

result = post(sid, ip, command, json_data)


print result['name']
print result ['ipv4-address']

#Logout
logout(sid,ip)
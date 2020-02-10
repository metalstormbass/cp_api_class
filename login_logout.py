import requests
import json
import sys

#remove https warning
requests.packages.urllib3.disable_warnings()

#Login Function
def login(ip,user,pw):
    payload_list={}
    payload_list['user']=user
    payload_list['password']=pw

    headers = {
            'content-type': "application/json",
            'Accept': "*/*",
        }
    try:
        response = requests.post("https://"+ip+"/web_api/login", json=payload_list, headers=headers, verify=False)
        #print response
        response_json = json.loads(response.content)
        #print response_json
        sid = response_json['sid']
        return sid
    
    except Exception as error:
        print "Unable to login. Ensure the API is enabled and check credentials"
        print error
        sys.exit()
        

#Post Functionality
def post(sid, ip, command, json_data):
    headers = {
            'content-type': "application/json",
            'Accept': "*/*", 'x-chkp-sid': sid,
        }
    try:
        response = requests.post("https://"+ip+"/web_api/" + command, json=json_data, headers=headers, verify=False)
        
        response_json = json.loads(response.content)
        
        return response_json
    except:
        print "Error Occured"
        sys.exit()
        
#Logout function
def logout(sid,ip):
    payload_list={}
    headers = { 'content-type': "application/json", 'Accept' : "*/*", 'x-chkp-sid': sid, }
    
    response = requests.post("https://"+ip+"/web_api/logout", json=payload_list, headers = headers, verify=False)
    
    return response
    
    
    
    
    
    
    
    
    
    
    
    
    
        
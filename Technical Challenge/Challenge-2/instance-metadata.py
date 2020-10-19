#This Code retrieves the Instance Metadata in JSON Output 
import requests
import json

token_url = "http://169.254.169.254/latest/api/token"  #Request token.

token_header = {"X-aws-ec2-metadata-token-ttl-seconds" : "21600"} #Header for token request.

token=requests.put(token_url, data ="",headers=token_header) #Call token api/token stored in token (data/body) is empty.

meta_url= "http://169.254.169.254/latest/meta-data/" #Instance Metadata URL.

meta_header={"X-aws-ec2-metadata-token" : token.text} #token.text retrieves only the body of the request. 

meta_response = requests.get(meta_url,headers=meta_header)

data = meta_response.text

data = data.split("\n") #Removing new line to get an array like space seprated keys. 

#data = list(data)

print len(data)

dict_data = {}  #Created an empty array/object/dict.

for item in data:

  #json_data[item.rstrip("/")] = ""

  metadata_url = meta_url + item 

  metadata_header = meta_header

  metadata_response = requests.get(metadata_url,headers=metadata_header) #Travese each key and create a metadata URL call for each key.

  dict_data[item.rstrip("/")] = metadata_response.text.rstrip("/") 


json_data =  json.dumps(dict_data) #Change the recieved key/value pair to json format.

print json_data
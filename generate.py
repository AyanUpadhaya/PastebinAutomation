
import requests
"""
generate user key for posting as pastebin member
================================================
from https://pastebin.com/doc_api get the api_dev_key and save it in your creds.py file as api_dev_key varible
to generate the user key create a separate py file, copy the below codes.
Then pass your api_dev_key, your username and password of pastebin as arguments(line: 57) in generate_user_key funtion()
This will return an user key. copy that and save it in your creds.py file as 
api_user_key variable
"""

def generate_user_key(api_dev_key,api_user_name,api_user_password):
    API_ENDPOINT="https://pastebin.com/api/api_login.php"

    data={
    'api_dev_key':api_dev_key,
    'api_user_name':api_user_name,
    'api_user_password':api_user_password
    }
    r=requests.post(url=API_ENDPOINT,data=data)
    return r.text

print(generate_user_key(api_dev_key,api_user_name,api_user_password))

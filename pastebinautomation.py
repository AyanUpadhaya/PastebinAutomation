import requests
from creds import*

class Pastebin:
    def __init__(self):
        self.API_ENDPOINT="https://pastebin.com/api/api_post.php"
        self.api_dev_key  = api_dev_key
        self.api_user_key = api_user_key
    
    def post_pastebin(self,file_path,paste_name):

        with open(file_path,'r') as f:
            source_data=f.read()
        data={
        'api_dev_key':self.api_dev_key,
        'api_user_key':self.api_user_key,
        'api_option':'paste',
        'api_paste_code':source_data,
        'api_paste_format':api_paste_format,
        'api_folder_key':api_folder_key,
        'api_paste_name':paste_name,}

        r=requests.post(url=self.API_ENDPOINT,data=data,timeout=6)

        print(r)
        print(r.text)


def main():
    file_path=input("Enter the file path:")
    paste_name=input("Enter paste name:")
    try:
        paste=Pastebin()
        paste.post_pastebin(file_path,paste_name)
    except Exception as e:
        print(e)


if __name__=="__main__":
    main()






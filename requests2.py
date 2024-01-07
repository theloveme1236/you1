import requests
import time
def add():
    with open('api.txt') as fffda:
        api_list = fffda.read().splitlines()
    for api_code in api_list:
        database_url = 'https://ahmed-3cacf-default-rtdb.firebaseio.com/'
        users_endpoint = 'users.json'
        new_user_data = {"name": "mohamed", "email" : api_code.split('@')[-1],"apk":"com.zhiliaoapp.musically.gp" ,"id":"متابعة"}
        response_put = requests.put(f'{database_url}/{users_endpoint}', json=new_user_data)
        while True:
            #time.sleep(10)
            response_get = requests.get(f'{database_url}/{users_endpoint}')
            
            user_data = response_get.json()
            email = user_data['email']
            print(response_get.text)
            print(email)
            if email == 'stop':
                print('stop')
                break



add()

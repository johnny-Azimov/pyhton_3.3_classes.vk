from urllib.parse import urlencode
import requests

APP_ID = 7358346
BASE_URL = 'https://oauth.vk.com/authorize'
auth_data = {
    'client_id' : APP_ID,
    'display' : 'page',
    'scope' : 'status',
    'response_type' : 'token',
    'v': '5.95',
    'redirect_uri': 'https://example.com/'
}
# print('?'.join((BASE_URL, urlencode(auth_data))))


TOKEN = 'db1f0d36a4cb69cde615794e7c8a2f6748e25ce140598fd4e7767aa9dd8823c24f1bb562049521ff7a1fb'

class User_id:
    def __init__(self, id):
        self.id = id


class User:
    def __init__(self,user_id, token):
        self.token = token
        self.user_id = user_id
        

    def get_params(self):
        return {
            'access_token' : self.token,
            'v' : '5.95',
            'user_id' : self.user_id
        }

    def request(self, method, params):
        response = requests.get(
                'https://api.vk.com/method/' + method,
                params=params
            )
        return response


    def get_friends(self):
        params = self.get_params()
        response = self.request(
            'friends.get',
            params=params
        )
        return response.json()['response']

    def __and__(self, other_user, mutal_user_lust=list()):
        user_1 = other_user.get_friends()
        user_2= self.get_friends()
        for i in user_1.get('items'):
            for ii in user_2.get('items'):
                if i == ii:
                    adress = 'https://vk.com/id' + str(ii)
                    mutal_user_lust.append(adress)
        return mutal_user_lust

    def user(self, id):
        response = requests.get('https://vk.com/id' + id,)
        return response


user1 = User(input('ввести ID user1: '),TOKEN)
user2 = User(input('ввести ID user2: '),TOKEN)
print(user1 & user2)


user = User_id(7358346)
user = f'\nhttps://vk.com/id{user.id}'
print(user)
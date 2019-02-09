from pprint import pprint
from rocketchat_API.rocketchat import RocketChat

#proxy_dict = {
#              "http"  : "http://127.0.0.1:3128",
#              "https" : "https://127.0.0.1:3128",
#            }

rocket = RocketChat('user', 'password', server_url='https://chat.clubelek.fr')
#, proxies=proxy_dict)
pprint(rocket.me().json())
pprint(rocket.channels_list().json())

while True:
    pprint(rocket.chat_post_message('Benoit', channel='poubelle', alias='Benoit').json())
#pprint(rocket.channels_history('GENERAL', count=5).json())

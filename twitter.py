import requests
import json
url = 'https://maker.ifttt.com/trigger/post/with/key/dxWmXFqjD_1VvODSaB4ogA'
class Twitter():
	def tweet(self, message):
		#### Old method ####
#		message = message.replace(' ', '+')
#		os.system('curl -X POST https://maker.ifttt.com/trigger/post/with/key/dxWmXFqjD_1VvODSaB4ogA?value1=\"%s\"'% message)
		#### New method ####
		data = {'value1': message}
		r = requests.post(url, json=data)
	def tweet_photo(self, message, pic_url):
		pass

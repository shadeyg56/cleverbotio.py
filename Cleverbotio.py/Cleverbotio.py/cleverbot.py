import requests

class Cleverbot():
	def __init__(self, user, api_key, nick="Bot"):
		self.session = requests.Session()
		self.user = user
		self.key = api_key
		self.nick = nick


	def create_session(self):
		params = {
			"user": self.user,
			"key": self.key,
			"nick": self.nick
		}
		resp = self.session.post("https://cleverbot.io/1.0/create", data=params)
	
	def say(self, text):
		params = {
			"user": self.user,
			"key": self.key,
			"nick": self.nick,
			"text": text
		}

		resp = self.session.post("https://cleverbot.io/1.0/ask", data=params)
		data = resp.json()
		return data
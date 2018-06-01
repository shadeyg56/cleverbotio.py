import aiohttp
import asyncio

class Cleverbot():
	def __init__(self, user, api_key, nick="Bot"):
		self.session = aiohttp.ClientSession()
		self.user = user
		self.key = api_key
		self.nick = nick

	def __del__(self):
		if not self.session.closed:
			if self.session._connector_owner:
				self.session._connector.close()
				self.session._connector = None

	async def create_session(self):
		params = {
			"user": self.user,
			"key": self.key,
			"nick": self.nick
		}
		async with self.session.post("https://cleverbot.io/1.0/create", data=params) as resp:
			data = await resp.json()
	
	async def say(self, text):
		params = {
			"user": self.user,
			"key": self.key,
			"nick": self.nick,
			"text": text
		}
		async with self.session.post("https://cleverbot.io/1.0/ask", data=params) as resp:
			data = await resp.json()
		return data

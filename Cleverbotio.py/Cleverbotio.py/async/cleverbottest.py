from cleverbot import Cleverbot
import asyncio

cb = Cleverbot("ud577fnPv6KuTKJ8", "XN0Q5y6wpHn83S9NZXuNf3PJnTc75qXD", "testing")



async def test():
	await cb.create_session()
	c = await cb.say("test")
	print(c["response"])

event = asyncio.get_event_loop()
event.run_until_complete(test())
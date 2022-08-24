from jokeapi import Jokes # Import the Jokes class
import asyncio
import time

async def print_joke():
	j = await Jokes() 
	joke = await j.get_joke(blacklist=["nsfw", "religious", "racist", "sexist"]) 
	if joke["type"] == "single": 
		print(joke["joke"])
	else:
		print(joke["setup"])
		time.sleep(2)
		print(joke["delivery"])

while True:
	a = input("Would you like a joke? (y/n): ")
	if a.startswith('y') or a.startswith("Y"):
		print("\n")
		asyncio.run(print_joke())
		print("\n")
	else:
		break
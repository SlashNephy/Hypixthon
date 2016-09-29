# coding=utf-8
from hypixthon import Hypixthon

apiKey = "PUT YOUR API KEY YOU CAN GET WITH /api"

if __name__ == "__main__":
	client = Hypixthon(apiKey)

	# Get player data.
	client.getPlayer(uuid="player uuid")
	# Get player's friend data.
	client.getFriends(uuid="player uuid")

	# First get guild ID.
	client.findGuild(uuid="player uuid")
	# Get guild data.
	client.getGuild(guildId="guild uuid")

	# Get player's session data.
	client.getSession(uuid="player uuid")

	# Get API Key's information.
	client.getKey(key=apiKey)

	# Get Coin Boosters information.
	client.getBoosters()

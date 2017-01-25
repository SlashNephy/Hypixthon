# coding=utf-8
import warnings

from hypixthon.request import Request
from hypixthon.exceptions import ArgumentException

def parseArguments(**kwargs):
	if "uuid" in kwargs:
		return True, kwargs["uuid"]
	if "mcid" in kwargs:
		warnings.warn("`mcid` parameter is deprecated. Please consider using `uuid` instead of `mcid`.", DeprecationWarning)
		return False, kwargs["mcid"]
	raise ArgumentException("`uuid` or `mcid` must be set. (`mcid` is deprecated.)")

def isUUIDArgument(parsed):
	return parsed[0]

class Wrapper:
	def __init__(self, apiKey):
		self.apiKey = apiKey
		self.request = Request(apiKey)

	def getPlayerUUID(self, mcid):
		return self.request.MojangAPI("/users/profiles/minecraft/{}".format(mcid)).get("id")

	def getPlayerMinecraftID(self, uuid):
		return self.request.MojangAPI("/user/profiles/{}/names".format(uuid))[-1].get("name")

	def getPlayer(self, **kwargs):
		parsed = parseArguments(**kwargs)
		key = "uuid" if isUUIDArgument(parsed) else "name"
		data = {
			key: parsed[1]
		}

		return self.request.HypixelAPI("/player", data)

	def findGuild(self, **kwargs):
		parsed = parseArguments(**kwargs)
		key = "byUuid" if isUUIDArgument(parsed) else "byName"
		data = {
			key: parsed[1]
		}

		return self.request.HypixelAPI("/findGuild", data)

	def getGuild(self, guildId):
		data = {
			"id": guildId
		}

		return self.request.HypixelAPI("/guild", data)

	def getFriends(self, uuid):
		data = {
			"uuid": uuid
		}

		return self.request.HypixelAPI("/friends", data)

	def getSession(self, **kwargs):
		parsed = parseArguments(**kwargs)
		key = "byUuid" if isUUIDArgument(parsed) else "byName"
		data = {
			key: parsed[1]
		}

		return self.request.HypixelAPI("/session", data)

	def getKey(self):
		data = {
			"key": self.apiKey
		}

		return self.request.HypixelAPI("/key", data)

	def getBoosters(self):
		return self.request.HypixelAPI("/boosters")

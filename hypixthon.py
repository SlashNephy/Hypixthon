# coding=utf-8
import json

import requests

class Hypixthon:
	baseUrl = "https://api.hypixel.net"

	def __init__(self, apiKey):
		self.apiKey = apiKey

	def call(self, path, data=None):
		if not data:
			data = {}
		data["key"] = self.apiKey

		url = path
		if path.startswith("/"):
			url = self.baseUrl + path
		url += "?" + "".join(["{}={}".format(x, y) for x, y in data.items()])

		response = requests.get(url)
		return json.loads(response.text)

	def getPlayer(self, uuid=None, mcid=None):
		if not uuid and not mcid:
			raise Exception("uuid or mcid must be set.")
		if uuid:
			data = {"uuid": uuid}
		else:
			data = {"name": mcid}
		return self.call("/player", data)

	def findGuild(self, uuid=None, mcid=None):
		if not uuid and not mcid:
			raise Exception("uuid or name must be set.")
		if uuid:
			data = {"byUuid": uuid}
		else:
			data = {"byName": mcid}
		return self.call("/findGuild", data)

	def getGuild(self, guildId):
		data = {"id": guildId}
		return self.call("/guild", data)

	def getFriends(self, uuid=None, mcid=None):
		if not uuid and not mcid:
			raise Exception("uuid or player must be set.")
		if uuid:
			data = {"byUuid": uuid}
		else:
			data = {"byName": mcid}
		return self.call("/friends", data)

	def getSession(self, uuid=None, mcid=None):
		if not uuid and not mcid:
			raise Exception("uuid or player must be set.")
		if uuid:
			data = {"byUuid": uuid}
		else:
			data = {"byName": mcid}
		return self.call("/session", data)

	def getKey(self, key):
		data = {"key": key}
		return self.call("/key", data)

	def getBoosters(self):
		return self.call("/boosters")

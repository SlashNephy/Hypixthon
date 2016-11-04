# coding=utf-8
import requests

from hypixthon.exceptions import APIError

class Request:
	baseUrlForHypixelAPI = "https://api.hypixel.net"
	baseUrlForMojangAPI = "https://api.mojang.com"
	userAgent = "Hypixthon/1.0 (Hypixel API Wrapper for Python; https://github.com/SlashNephy/Hypixthon)"
	timeout = 10

	def __init__(self, apiKey):
		self.apiKey = apiKey

	def __call(self, url, header):
		try:
			response = requests.get(url, headers=header, timeout=self.timeout)
			if response.status_code != 200:
				raise APIError("API returned `{}`. Response was `{}`.".format(response.status_code, response.text))
		except requests.exceptions.Timeout:
			raise APIError("Request timed out. ({} secs)".format(self.timeout))

		try:
			return response.json()
		except:
			raise APIError("Could not decode response json. Response was `{}`.".format(response.text))

	def HypixelAPI(self, path, data=None):
		if not data:
			data = {}
		data["key"] = self.apiKey

		url = self.baseUrlForHypixelAPI + path if path.startswith("/") else path
		url += "?" + "&".join(["{}={}".format(key, value) for key, value in data.items()])
		header = {
			"User-Agent": self.userAgent
		}

		return self.__call(url, header)

	def MojangAPI(self, path):
		url = self.baseUrlForMojangAPI + path if path.startswith("/") else path
		header = {
			"User-Agent": self.userAgent
		}

		return self.__call(url, header)

# Hypixthon
Hypixel API Wrapper for Python 2 / 3

set up with your API Key.<br>
if you do NOT have an API key, you can get an API Key with `/api` in Minecraft while you are logging in `mc.hypixel.net`.
```python
from hypixthon import Hypixthon

client = Hypixthon("PUT YOUR API KEY")
```

get request like this.
```python
# Get player data.
client.getPlayer(uuid="player uuid")
# Get player's friend data.
client.getFriends(uuid="player uuid")

# First get guild ID.
client.findGuild(uuid="player uuid")
# Get guild data.
client.getGuild(guildId="guild id")

# Get player's session data.
client.getSession(uuid="player uuid")

# Get API Key's information.
client.getKeyInfo()

# Get Coin Boosters information.
client.getBoosters()
```

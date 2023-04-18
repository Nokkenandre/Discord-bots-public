import nextcord
import re
from time import sleep

# nextcord needs to be installed via pip or similar
# re and time comes prepacked in python
# bot needs bot mermissions: Manage Messages, Read Message History, Add Reactions and Read Messages/View Channels when beeing invited
# bot needs special intents: SERVER MEMBERS INTENT and MESSAGE CONTENT INTENT when beeing created

TOKEN = "hemmelig"
# add your bot token ^

pingable = ["role", "role", "user"]
# roles and players that the bot alerts you to ^

reactable = ["user", "user"]
# id of user(s) to be alerted ^

myintents = nextcord.Intents.default()
myintents.reactions = True
myintents.message_content = True
client = nextcord.Client(intents=myintents)


@client.event
async def on_raw_reaction_add(payload):
    user = await client.fetch_user(payload.user_id)
    if not payload.guild_id and user != client.user:
        reaction = payload.emoji
        channel = await client.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        match = re.search("(?P<url>https?://\S+)", message.content)
        if match is not None:
            link = match.group("url")
            # Extract the channel and message IDs from the link
            pattern = "https://discord\.com/channels/(?P<guild_id>\d+)/(?P<channel_id>\d+)/(?P<message_id>\d+)"
            match = re.search(pattern, link)
            if match is not None:
                guild_id = int(match.group("guild_id"))
                channel_id = int(match.group("channel_id"))
                message_id = int(match.group("message_id"))

                # Get the channel and message objects
                channel = client.get_channel(channel_id)
                message = await channel.fetch_message(message_id)

                await message.clear_reactions()
                sleep(1)
                await message.add_reaction(reaction)


@client.event
async def on_ready():
    print("logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    text = str(message.content)
    author = str(message.author)
    channel = str(message.channel)
    server = str(message.guild)

    if not message.guild:
        if message.author == client.user:
            await message.add_reaction("\U0001F440")
            await message.add_reaction("\U00002705")
            await message.add_reaction("\U0000274E")
        return

    link = f'https://discord.com/channels/{message.guild.id}/{message.channel.id}/{message.id}'

    for roles in pingable:
        ids = [member.id for member in message.mentions]
        rids = [role.id for role in message.role_mentions]
        if roles in rids:
            for Id in reactable:
                user = await client.fetch_user(Id)
                await user.send(f"""{server}: {author} mentioned @{str(roles)} in {channel}
link : {link}
    > {text}""")
            return

        elif roles in ids:
            user = await client.fetch_user(roles)
            await user.send(f"""{server}: {author} mentioned @{str(roles)} in {channel}
            link : {link}
                > {text}""")
            return


client.run(TOKEN)

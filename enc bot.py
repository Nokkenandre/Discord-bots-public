import nextcord

#last username
global lun
lun = ""
# lun = Last UserName

TOKEN = "Secret token here"

myintents = nextcord.Intents.default()
myintents.message_content = True


client = nextcord.Client(intents=myintents)
reactto = [["User 1", "\U0001F60E"], ["User 2", "\U0001F957"], ["User 3", "\U0001F681"], ["User 4", "\U0001F408"], ["User 5", "\U0001F427"], ["User 6", "\U0001F1F8\U0001F1EA"]]
# usernames replaced with "User x" for anonymity

@client.event
async def on_ready():
    print("logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    global lun
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username} said {user_message} in (#{channel})")

# Makes sure the bot does not reply multiple times to a block of diffrent texts from the same user
    if username == lun:
        return
    else:
        lun = username

    for react in reactto:
        if username == react[0]:
            await message.add_reaction(react[1])


client.run(TOKEN)

import nextcord
import random
prompt = ["I used to be an adventurer like you. Then I took an arrow in the knee....", "Let me guess - someone stole your sweetroll..", "Gotta keep my eyes open. Damn dragons could swoop down at any time.", "My cousin is out fighting dragons, and what do I get? Guard duty.", "Disrespect the law, and you disrespect me.", "Watch the skies, traveler.", "No lollygaggin'.", "They say Ulfric Stormcloak murdered the High King... with his voice! Shouted him apart!", "I'd be a lot warmer and a lot happier with a bellyful of mead...", "Got to thinking, maybe I'm the Dragonborn, and I just don't know it yet.", "I have to wonder... what does the Dragonborn do once he's summoned by the Greybeards? Can the Thu'um be taught, like any skill?", "You see those warriors from Hammerfell? They've got curved swords. Curved. Swords.", "I mostly deal with petty thievery and drunken brawls. Been too long since we've had a good bandit raid.", "Trouble?", "What is it? Dragons?", "Fancy yourself an alchemist, hmm? Never could get the hang of that.", "Staying safe, I hope?", "Fear not. Come dragon or giant, we'll be ready.", "Citizen.", "Everything's all right?", "They say if a vampire so much as scratches you, you'll turn into one. That better not be true.", "Dragons breathing fire in the sky. Vampires brazenly attacking people on the street. It's the end of the world I tell you.", "We need to do something about these vampire attacks.", "Heard they're reforming the Dawnguard. Vampire hunters or something, in the old fort near Riften. Might consider joining up myself.", "They say that vampires attacked the Hall of the Vigilant. Burned it to the ground! Never heard of vampires doing anything like that before."]
chrime = ["You have committed crimes against Skyrim and her people. What say you in your defense?", "By order of the Jarl, stop right there!", "You've committed crimes against Skyrim and her people, and it's time to face the Jarl's justice.", "STOP, you violated the law"]
TOKEN = "Secret token here"

client = nextcord.Client(intents=nextcord.Intents.all())

@client.event
async def on_ready():
    print("logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)

    if message.author == client.user:
        return
    # Makes sure it does not respond to itself

    if any(word in user_message.lower() for word in ["*kills chicken*"]):
        await message.channel.send(chrime[random.randint(0, 3)])
    elif client.user.mentioned_in(message) or user_message.lower() in ["guard", "solitude guard", "frank"]:
        await message.channel.send(prompt[random.randint(0, 24)])




client.run(TOKEN)

# Invite link: https://discord.com/api/oauth2/authorize?client_id=1064835298225303572&permissions=534723950656&scope=bot

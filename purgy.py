import discord
import asyncio

SECRET = "feds"     # Keyword for deleting messages
TOKEN = "..."       # Replace with your user token

msg_log = open("deleted.log", "a")

class MyClient(discord.Client):
    async def on_message(self, message):
        if(message.author!=self.user):
            return
        channels=[]
        if(message.content=="purge2"):
            channels=message.channel.guild.channels
        elif(message.content==SECRET):
            channels.append(message.channel)
        else:
            return
        for channel in channels:
            print("Purging messages from: " + str(channel))
            msg_log.write("Purging messages from: " + str(channel) + "\n")

            try:
                # Fetch all message, you might want to purge channel by channel to speedup if the server is old and big
                async for mss in channel.history(limit=None):
                    if(mss.author==self.user):
                        print(f"[{mss.created_at}] {mss.content}")
                        msg_log.write(f"[{mss.created_at}] {mss.content}\n")

                        try:
                            await mss.delete()
                        except:
                            # This shouldn't happen unless you call purge multiple time
                            print("Can't delete!\n")
            except:
                print("Can't read history!\n")


if (TOKEN == "..."):
    print("Error. Invalid token. Make sure you replace it in line 5.")
    exit(1)

client=MyClient(heartbeat_timeout=86400, guild_subscriptions=False)
client.run(TOKEN, bot=False)
msg_log.close()


import discord
import asyncio
class MyClient(discord.Client):
    async def on_message(self, message):
        if(message.author!=self.user):
            return
        channels=[]
        if(message.content=="purge2"):
            channels=message.channel.guild.channels
        elif(message.content=="feds"):  #change that to anything you want so when u type it in the channel it'll delete
            channels.append(message.channel)
        else:
            return
        for channel in channels:
            print(channel)
            try:
                async for mss in channel.history(limit=None):
                #fetch all message, you might want to purge channel by channel to speedup if the server is old and big
                    if(mss.author==self.user):
                        print(mss.content)
                        try:
                            await mss.delete()
                        except:
                            print("Can't delete!\n")#this shouldn't happen unless you call purge multiple time
            except:
                print("Can't read history!\n")
            

client=MyClient(heartbeat_timeout=86400, guild_subscriptions=False)
client.run("Insert token here!", bot=False)

from Bot import bot
from pyrogram import idle
from os import listdir
from os.path import isfile, join
import importlib
import asyncio


	
      
async def main():
    mypath = 'Bot/plugins'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    Files = []
    for file in onlyfiles:
        if file.split('.')[-1] == 'py':
            Files.append(file)
        else:
            pass
        
    Imported = []
    for file in Files:
        Imported.append(importlib.import_module(
            'Bot.plugins.{}'.format(file.split('.')[0])))
    print("Plugins Loaded: ", len(Imported))





if __name__ == "__main__":
    try:
        bot.start()
        bot.loop.run_until_complete(main())
        idle()
        print("Bot is running...")
    except Exception as e:
        print(str(e))

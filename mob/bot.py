from pyrogram import Client, idle
from pyromod import listen
from   𝒎𝒐𝒅 ❤️y import caes,   𝒎𝒐𝒅 ❤️y, group, source, photosource,   𝒎𝒐𝒅 ❤️id, ch, bot_token, bot_token2

bot = Client("CAR", api_id=25107638, api_hash="54cbd7f70f120b03ab93b04ed13aa636", bot_token=bot_token, plugins=dict(root="  𝒎𝒐𝒅 ❤️"))
lolo = Client("hossam", api_id=25107638, api_hash="54cbd7f70f120b03ab93b04ed13aa636", session_string=bot_token2)    

DEVS = caes
DEVSs = []
bot_id = bot.bot_token.split(":")[0]

async def start_zombiebot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    await lolo.start()
    try:
      await bot.send_message(  𝒎𝒐𝒅 ❤️y, "**تم تشغيل الصانع بنجاح..💗**")
    except:
      pass
    await idle()

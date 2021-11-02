import asyncio

from program import BOT_ID, USERBOT_ID
from driver.veez import bot, call_py
from pytgcalls import idle


def all_info(bot, call_py):
    global BOT_ID, USERBOT_ID
    getme = bot.get_me()
    getme1 = call_py.get_me()
    BOT_ID = getme.id
    USERBOT_ID = getme1.id


async def mulai_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    print("[INFO]: STARTING PYTGCALLS CLIENT")
    await call_py.start()
    print("[INFO]: GENERATING CLIENT PROFILE")
    all_info(bot, call_py)
    await idle()
    print("[INFO]: STOPPING BOT")
    await bot.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(mulai_bot())

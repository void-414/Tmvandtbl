import asyncio
from aiohttp import web
from pyrogram import Client, idle
from plugins import omg_server
from config import API_ID, API_HASH, USER_SESSION, PORT

user = Client(
    name="User", 
    api_id=API_ID,
    api_hash=API_HASH, 
    session_string=USER_SESSION,
    plugins={"root": "plugins"}
)

async def run_server():
    app = web.AppRunner(await omg_server())
    await app.setup()
    bind_address = "0.0.0.0"
    await web.TCPSite(app, bind_address, PORT).start()

async def main(user):
    from plugins.tamilmv import tamilmv_rss
    from plugins.tamilblasters import tamilblasters_rss
    while True:
        print("Starting TMV scraping...")
        await tamilmv_rss(user)
        await asyncio.sleep(20)
        print("Starting TBL scraping...")
        await tamilblasters_rss(user)
        await asyncio.sleep(20)

if __name__ == '__main__':
    user.start()
    user.loop.run_until_complete(run_server())
    user.loop.run_until_complete(main(user))
    user_info = user.get_me()
    user.username = user_info.username
    print(f"🕵️‍♀️ User Name : @{user.username} Rss Start !!!🚀")
    idle()
    user.stop()

from telethon import TelegramClient, events
from config import API_ID, API_HASH, SESSION_NAME
from games import play_game

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond("تم تشغيل سورس داينو المعدل بنجاح!\nاكتب /game للعب.")

@client.on(events.NewMessage(pattern='/game'))
async def game(event):
    await play_game(event)

print("تم تشغيل البوت... انتظر تسجيل الدخول")
client.start()
client.run_until_disconnected()

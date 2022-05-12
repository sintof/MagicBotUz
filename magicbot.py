import time
from telethon import TelegramClient, events
from animations import Smiles
from alphabit import Alphabit


ip_id = input("API_id kodini kiriting:")
ip_hash = input("API_hash kodini kiriting:")

api_id = ip_id
api_hash = ip_hash

client = TelegramClient('anon', api_id, api_hash)

smiles = Smiles()


@client.on(events.NewMessage)
async def my_event_handler(event):
    if '.d' in event.raw_text:
        time.sleep(0.5)
        for i in range(5):
            time.sleep(0.5)
            for j in smiles.d:
                time.sleep(0.5)
                await event.edit(j)
    elif ".type" == event.raw_text[:5] and len(event.raw_text) > 6:
        orig_text = event.raw_text.split(".type ", maxsplit=1)[1]
        text = orig_text
        pb = ""
        typing_symbol = "➪"

        while (pb != orig_text):
            try:
                await event.edit(pb + typing_symbol)
                time.sleep(0.09)

                pb += text[0]
                text = text[1:]

                await event.edit(pb)
                time.sleep(0.09)

            except Exception as e:
                print(e)
    elif ".anim" == event.raw_text[:5] and len(event.raw_text) > 6:
        orig_text = event.raw_text.split(".type ", maxsplit=1)[1]
        await event.edit(Alphabit.get_word)
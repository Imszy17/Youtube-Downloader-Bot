from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Untuk mengunduh, anda cukup mengirimkan tautan video yang akan anda unduh dari youtube"
    await message.reply_text(helptxt)

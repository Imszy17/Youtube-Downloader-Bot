from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/Imszycloud")],
        [InlineKeyboardButton(
            "Kontak saya", url="https://t.me/Imszy01")]
    ])
    welcomed = f"Hai, <b>{message.from_user.first_name}</b>\nSaya adalah bot pengunduh youtube yang dibuat oleh @Imszy01\nKetik /help untuk info selengkapnya"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation

# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/YouTube-Video-Download-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/YouTube-Video-Download-Bot



from pyrogram import Client, filters
from Youtube.config import Config

# Create a Pyrogram client
app = Client(
    "24989642",
    api_id=Config.24989642, 
    api_hash=Config.9f180413e280308b85c6f177e9bde825, 
    bot_token=Config.7541623387:AAFm4RMFpJWGwaEVleSIn0EFHOZDxXNpoa4,
    plugins=dict(root="Youtube")
)



# Start the bot
print("🎊 I AM ALIVE 🎊")
app.run()

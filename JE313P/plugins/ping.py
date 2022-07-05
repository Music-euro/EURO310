import os

from telethon import Button, events

from JE313P import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/d49949a966c8219f4fa8c.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@JE313P"
)

CAPTION = f"**سرعة البنك:** {ms}\n المالك:『{ALIVE}』"


@JE313P.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("السورس", "https://t.me/E_U_R_O_1")]]
    await JE313P.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)

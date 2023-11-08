from fastapi import FastAPI
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from config import token, webhook_url
from start import private_router

stroge = MemoryStorage()

webhook_path = f"/bot/{token}"
webhook_link = webhook_url + webhook_path
print(webhook_link)

app = FastAPI()

bot = Bot(token=token, parse_mode='html')
dp = Dispatcher(storage=stroge)


@app.on_event("startup")
async def on_startup():
    await bot.set_webhook(url=webhook_link)
    print("Bot started")
    dp.include_router(router=private_router)

@app.post(webhook_path)
async def bot_webook(update: dict):
    telegram_update = types.Update(**update)
    await dp.feed_update(bot=bot, update=telegram_update)

@app.on_event('shutdown')
async def on_shutdown():
    await bot.session.close()
    print('Bot stoped')

@app.get('/')
async def root():
    return {'message': "Bosh saxifa"}
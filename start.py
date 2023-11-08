from aiogram import types, Router, F
from aiogram.filters import CommandStart
from private import IsPrivate

private_router = Router()
private_router.message.filter(IsPrivate())

@private_router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Salom {}".format(message.from_user.full_name))

@private_router.message(F.text)
async def echo_handler(message:types.Message):
    await message.answer(message.text)

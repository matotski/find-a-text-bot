import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject
from aiogram.enums.dice_emoji import DiceEmoji
from config_reader import config
from aiogram.enums import ParseMode
from aiogram.utils.formatting import Text, Bold
from aiogram import F, html
from datetime import datetime
from text_reader import find_string_by_word, test_text
from file_reader import file_reader
logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()



@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer(f"Hello, <b>{message.from_user.full_name}</b>", parse_mode=ParseMode.HTML)



async def main():
    await dp.start_polling(bot)



@dp.message(Command("hello"))
async def cmd_hello(message: types.Message):
    content = Text("Hello, ", Bold(message.from_user.full_name))
    await message.answer(**content.as_kwargs())



@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji=DiceEmoji.BOWLING)



@dp.message(Command("settimer"))
async def cmd_settimer(message: types.Message, command: CommandObject):
    if command.args is None:
        await message.reply("Необходимо передать аргументы!")
        return
    try:
        delay_time, text_to_send = command.args.split(" ", maxsplit=1)
    except ValueError:
        await message.reply("Неправильный формат данных\nПример: /settimer <time> <message> ")
        return
    await message.answer(f"Таймер добавлен:\nВремя: {delay_time}\nСообщение: {text_to_send}")


# @dp.message(F.text)
# async def text_reader(message: types.Message):
#     data = {"url": "", "email": "", "code": ""}
#     entities = message.entities or []
#     for item in entities:
#         if item.type in data.keys():
#             data[item.type] = item.extract_from(message.text)
#     message_list = message.text.split('.')
#     out = find_string_by_word(message_list, data["code"])
#     if out:
#         await message.answer(f"Искомое слово '{data["code"]}' найдено в строке: {html.quote(out)}")
#     else:
#         await message.answer(f"Искомое слово '{data["code"]}' не найдено.")



@dp.message(Command("search"))
async def text_reader(message: types.Message, command: CommandObject):
    if command.args is None:
        await message.reply("Вы не ввели данные!")
        return
    try:
        text,word_to_find = command.args.split("&", maxsplit=1)
    except ValueError:
        await message.reply("Неправильный формат данных!\nПример: /search текст &искомое слово")
    text_list = text.split('.')
    line_from_text = find_string_by_word(text_list, word_to_find)
    await message.answer(f"Искомое слово '{word_to_find}' найдено в строке: {line_from_text}")

# @dp.message_handler(commands=['parse'])
# async def parse_sentences(message: types.Message):
#     """
#     Parse sentences from a text file by a given search word.
#
#     Example: /parse file.txt search_word
#     """
#     args = message.get_args().split()
#     if len(args) != 2:
#         await message.reply('Invalid arguments. Usage: /parse file.txt search_word')
#         return
#
#     file_path, search_word = args
#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             text = file.read()
#     except FileNotFoundError:
#         await message.reply(f'File not found: {file_path}')
#         return
#
#     sentences = sent_tokenize(text)
#     matching_sentences = [sentence for sentence in sentences if re.search(r'\b' + search_word + r'\b', sentence, re.IGNORECASE)]
#
#     if not matching_sentences:
#         await message.reply(f'No sentences found containing "{search_word}"')
#     else:
#         await message.reply('\n'.join(matching_sentences))
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)




# @dp.message(Command("search"))
# async def text_reader(message: types.Message):
#     await message.answer(f'Пожалуйста, введите текст')
#     if message.text != None:
#         await message.answer((f"Отлично, теперь введите искомое слово"))




# @dp.message(F.text)
# async def echo_with_time(message: types.Message):
#     time_now = datetime.now().strftime('%H:%M')
#     added_text = html.underline(f'Создано в {time_now}')
#     await message.answer(f'{message.html_text}\n\n{added_text}',parse_mode="HTML")



# @dp.message(F.text)
# async def extract_data(message: types.Message):
#     data = {"url": "", "email": "", "code": ""}
#     entities = message.entities or []
#     for item in entities:
#         if item.type in data.keys():
#             data[item.type] = item.extract_from(message.text)
#     await message.reply(
#         f"Данные добавлены:\nUrl: {html.quote(data['url'])}\nEmail: {html.quote(data['email'])}\nPassword: {html.quote(data['code'])}")



if __name__ == "__main__":
    asyncio.run(main())
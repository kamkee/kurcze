from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint

bot = Bot(token='5774531366:AAECG7T2q5XWrbptTTFZyjOVMriNbssA1xY')
dp = Dispatcher(bot)

button1 = InlineKeyboardButton(text="Правила катаний по билетам-браслетам")
button2 = InlineKeyboardButton(text="Кто придумал ограничения по росту для детей при катании на аттракционах?")
button3 = InlineKeyboardButton(text="Какие появились новые аттракционы в парке?")

keyboard_inline = InlineKeyboardMarkup().add(button1, button2, button3)

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("Правила катаний по "
                                                                                  "билетам-браслетам",
                                                                                  "Кто придумал ограничения по росту "
                                                                                  "для детей при катании"
                                                                                  " на аттракционах?",
                                                                                  "Какие появились новые "
                                                                                  "аттракционы в парке?",)


@dp.message_handler(commands=['random'])
async def random_answer(message: types.Message):
    await message.reply("Select a range:", reply_markup=keyboard_inline)


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply('Привет, я бот которому можешь задать вопросы про парк',
                        reply_markup=keyboard1)


@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == 'Правила катаний по билетам-браслетам':
        await message.reply("По билетам-браслетам катание осуществляется на аттракционах 'СМОЛЯНКАГРАД': "
                            "«Колесо обозрения», «Гравитация», «Автодром», «Адреналин», Паровозик «Rio Grande»,"
                            "«Конвой», «Тачки», «Отважный капитан», "
                            "«Мотор шоу», Батут «Мадагаскар», Карусель «Лошадки», «Пиратский корабль»,"
                            "«Цепочная карусель», «Индейская река», "
                            "Карусель «Фантастик», игровой модуль «По щучьему велению». "
                            "Цена билета-браслета 42,00 руб., цена для детей ростом до 135см – 38,00 руб. "
                            "Допуск на аттракционы осуществляется только по правильно (плотно застегнутым) "
                            "билетам-браслетам, имеющим логотип предприятия, "
                            "идентификационный номер, соответствующий дню реализации билета-браслета. "
                            "Билеты-браслеты приобретаются в день катания. "
                            "По врежденные или снятые с руки браслеты недействительны. "
                            "Действие билета-браслета распространяется только на того посетителя, "
                            "у которого на руке имеется билет-браслет, "
                            "сопровождающий при этом проходит на аттракцион на общих условиях "
                            "(с билетом, либо по клиентской карте, либо со своим билетом-браслетом). "
                            "Повторное катание по билету-браслету на одном "
                            "аттракционе осуществляется после выхода из аттракциона, "
                            "и последующего входа в порядке общей очереди "
                            "(после завершения цикла катания нужно выйти и снова стать "
                            "в очередь для следующего катания) с целью "
                            "предоставления равных возможностей для всех посетителей парка. "
                            "Билеты-браслеты возврату и обмену не подлежат. "
                            "Подробные правила катания по билету-браслету размещены на сайте http://smolyanka.by/.%27")
    elif message.text == 'Кто придумал ограничения по росту для детей при катании на аттракционах?':
        await message.reply("Правила катания разрабатываются производителем аттракциона и мы не вправе их менять, "
                            "правила катания предусматривают безопасные способы "
                            "использования аттракциона с целью недопущения травмирования пассажиров.")

    if message.text == 'Какие появились новые аттракционы в парке?':
        await message.reply("Мы занимаемся подбором новых аттракционов! Следите за информацией на сайте "
                            "www.smolyanka.by и в социальных сетях: https://www.instagram.com/smolyankagrad/ "
                            "https://vk.com/id240650153 https://ok.ru/smolyanka.grad")


if __name__ == '__main__':
    print('bot polling started')
    executor.start_polling(dp)

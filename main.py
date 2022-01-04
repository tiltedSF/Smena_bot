import telebot
from telebot import types
import config

bot = telebot.TeleBot(config.token)

global lFilms
lFilms = ["чел-пук", "lxst богатырь", "чел с шашками"]
global dFilms
dFilms = {"чел-пук": "URL - на чек-пука", "lxst богатырь": "URL - на богатыря", "чел с шашками": "URL - на шахматы"}

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу!", "Расписание сеансов", "/help")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать больше о кино?', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею:\nничего')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу!":
        markup = types.InlineKeyboardMarkup()

        button1 = types.InlineKeyboardButton("VK", url='https://vk.com/smenakino')
        button2 = types.InlineKeyboardButton("INST", url='https://instagram.com/smena.kino')
        button3 = types.InlineKeyboardButton("Сайт кинотетра", url='https://smena-kino.ru/')

        markup.add(button1)
        markup.add(button2)
        markup.add(button3)

        bot.send_message(message.chat.id, 'Тогда переходи в группу в ВК,Inst или оф. сайт \nВскоре и тут будут новости!'.format(message.from_user), reply_markup=types.ReplyKeyboardRemove())
        bot.send_message(message.chat.id, 'Вот ссылочки:', reply_markup=markup)

    if message.text.lower() == "расписание сеансов" or message.text.lower() == "выбрать другой фильм":
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.row("Чел-пук", "LXST богатырь", "Чел с шашками",)
        bot.send_message(message.chat.id, 'Выберите фильм', reply_markup=keyboard)
        img = open('images/img_smena.jpg', 'rb')
        bot.send_photo(message.chat.id, img)

    if message.text.lower() in lFilms:
        keyboard = types.ReplyKeyboardMarkup()
        keyboard.row("О фильме", "Заказать билеты на фильм", "/help")
        global film
        film = message.text.lower()
        bot.send_message(message.chat.id, 'Хотите ли вы узнать о фильме или сразу купить билеты', reply_markup=keyboard)

    if message.text.lower() == "заказать билеты на фильм":
        bot.send_message(message.chat.id, 'Тогда переходите на оф. сайт', reply_markup=types.ReplyKeyboardRemove())

    if message.text.lower() == "о фильме":
        if film == "":
            bot.send_message(message.chat.id, 'Вы не выбрали фильм до этого')
    #   реализовать breake
    #     Фигачит туда сюда данные как бешанный

        keyboard = types.ReplyKeyboardMarkup()
        keyboard.row("Выбрать другой фильм", "Заказать билеты на фильм", "/help")
        msg = dFilms[film]
        bot.send_message(message.chat.id, f'Вот тот фильм - {msg}', reply_markup=keyboard)


bot.polling()
# Amaliyot

# from dotenv import load_dotenv
# import os
# from telebot import TeleBot
# from user8 import User

# load_dotenv()
#
# TOKEN = os.getenv("TOKEN")
#
# bot = TeleBot("6448262820:AAEElmIZlYw1zohSOI0O_mbXNkqOOrG6Cxw")

# f = open('config.jpg', 'rb')
# @bot.message_handler(commands=['start'])
# def echo(message):
#     username = message.from_user.username
#     tg_id = message.from_user.tg_id
#     name = message.from_user.name
#     surname = message.from_user.surname
#     user = User(tg_id, username, name, surname)
#     user.save()
#     bot.send_message(chat_id=message.chat.id, text=f"Welcome{message.from_user.username}")
#
#
# @bot.message_handler(content_types=['text'])
# def echo(message):
#     dt = {
#         "Farg'ona": "Bagʻdod tumani Beshariq tumani Buvayda tumani Dangʻara tumani Fargʻona tumani Furqat tumani Oltiariq tumani Oʻzbekiston tumani Qoʻshtepa tumani Quva tumani Rishton tumani Soʻx tumani Toshloq tumani Uchkoʻprik tumani Yozyovon tumani",
#         "Sirdaryo": "Sirdaryo tumani Guliston tumani Sayxunobod tumani Mirzaobod tumani Xovos tumani Boyovut tumani Oqoltin tumani Sardoba tumani",
#         "Navoiy": "Karmana tumani Navbahor tumani Nurata tumani Qiziltepa tumani Tomdi tumani Uchquduq tumani Xatirchi tumani Zarafshon tumani Konimex tumani",
#         "Jizzax": "Arnasoy tumani Baxmal tumani Dostlik tumani Forish tumani Gallaorol tumani Sharof Rashidov tumani Mirzachol tumani Paxtakor tumani Yangiobod tumani Zafarobod tumani Zomin tumani",
#         "Xorazm": "Bog'ot tumani, Gurlan tumani, Xiva tumani, Xonqa tumani, Hazorasp tumani, Qo'shko'pir tumani, Shovot tumani, Urganch tumani, Yangiariq tumani, Yangibozor tumani",
#         "Buxoro": "Buxoro tumani, G'ijduvon tumani, Jondor tumani, Kogon tumani, Olot tumani, Peshku tumani, Qorako'l tumani, Qorovulbozor tumani, Romitan tumani, Shofirkon tumani, Vobkent tumani",
#         "Surxandaryo": "Angor tumani, Bandixon tumani, Boysun tumani, Denov tumani, Jarqo'rg'on tumani, Muzrabot tumani, Oltinsoy tumani, Qiziriq tumani, Qumqo'rg'on tumani, Sariosiyo tumani, Sherobod tumani, Sho'rchi tumani, Termiz tumani, Uzun tumani",
#         "Namangan": "Chortoq tumani, Chust tumani, Kosonsoy tumani, Mingbuloq tumani, Namangan tumani, Norin tumani, Pop tumani, To'raqo'rg'on tumani, Uchqo'rg'on tumani, Uychi tumani, Yangiqo'rg'on tumani",
#         "Andijon": "Andijon tumani, Asaka tumani, Baliqchi tumani, Bo'z tumani, Buloqboshi tumani, Izboskan tumani, Jalolquduq tumani, Marhamat tumani, Oltinko'l tumani, Paxtaobod tumani, Qo'rg'ontepa tumani, Shahrixon tumani, Ulug'nor tumani, Xo'jaobod tumani",
#         "Qashqadaryo": "Chiroqchi tumani, Dehqonobod tumani, G'uzor tumani, Kasbi tumani, Kitob tumani, Koson tumani, Mirishkor tumani, Muborak tumani, Nishon tumani, Qarshi tumani, Shahrisabz tumani, Yakkabog' tumani",
#         "Samarqand": "Bulungur tumani, Ishtixon tumani, Jomboy tumani, Kattaqo'rg'on tumani, Kibray tumani, Narpay tumani, Nurobod tumani, Oqdaryo tumani, Payariq tumani, Pastdarg'om tumani, Samarkand tumani, Tayloq tumani, Urgut tumani",
#         "Toshkent": "Angren tumani, Bostanliq tumani, Buka tumani, Chinaz tumani, Chirchiq tumani, Ohangaron tumani, Oltiariq tumani, Parkent tumani, Piskent tumani, Qibray tumani, Quyi Chirchiq tumani, Toshkent tumani, Yangiyo'l tumani, Yuqori Chirchiq tumani"
#         }
#     if message.text.lower() == "viloyatlar":
#         bot.send_message(chat_id=message.chat.id, text="Sirdaryo, Navoiy, Jizzax, Xorazm, Buxoro, Surxondaryo, Namangan, Andijon, Qashqadaryo, Samarqand, Fargʻona, Toshkent")
#     elif message.text.capitalize() in dt:
#         bot.send_message(chat_id=message.chat.id, text=dt[message.text.capitalize()])
#     else:
#         bot.send_message(chat_id=message.chat.id, text=message.text)
#
#
# bot.polling()

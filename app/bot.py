import telebot
import math
import random
from datetime import datetime
from telebot import types

bot = telebot.TeleBot("7943448608:AAE1IYaj8whgUvJHYDCBOFc770yH2uX9_UU")

def greet(name):
    return f"Привет, {name}! Я твой Python-помощник."

def power(base, exponent=2):
    return base ** exponent

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

square = lambda x: x * x
cube = lambda x: x ** 3

def get_random_number():
    return random.randint(1, 100)

def get_circle_area(radius):
    return math.pi * radius ** 2

def get_current_time():
    return datetime.now().strftime("%H:%M:%S")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Функции")
    btn2 = types.KeyboardButton("Модули")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, greet(message.from_user.first_name), reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "Функции")
def show_functions(message):
    text = """📌 Доступные функции:
/fact - Вычислить факториал
/power - Возвести число в степень
/lambda - Примеры лямбда-функций"""
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda message: message.text == "Модули")
def show_modules(message):
    text = """📦 Работа с модулями:
/random - Случайное число
/circle - Площадь круга
/time - Текущее время"""
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['fact'])
def handle_factorial(message):
    try:
        num = int(message.text.split()[1])
        if num < 0:
            bot.reply_to(message, "Факториал определен только для целых неотрицательных чисел!")
        else:
            bot.reply_to(message, f"{num}! = {factorial(num)}")
    except (IndexError, ValueError):
        bot.reply_to(message, "Используйте: /fact [число]")

@bot.message_handler(commands=['power'])
def handle_power(message):
    try:
        args = message.text.split()
        base = float(args[1])
        exponent = float(args[2]) if len(args) > 2 else 2
        bot.reply_to(message, f"{base}^{exponent} = {power(base, exponent)}")
    except (IndexError, ValueError):
        bot.reply_to(message, "Используйте: /power [основание] [степень=2]")

@bot.message_handler(commands=['lambda'])
def handle_lambda(message):
    examples = [
        f"Квадрат числа 5: {square(5)}",
        f"Куб числа 3: {cube(3)}",
        "Лямбда-сортировка: sorted([3,1,4], key=lambda x: -x) → [4, 3, 1]"
    ]
    bot.reply_to(message, "\n".join(examples))

@bot.message_handler(commands=['random'])
def handle_random(message):
    bot.reply_to(message, f"Случайное число: {get_random_number()}")

@bot.message_handler(commands=['circle'])
def handle_circle(message):
    try:
        radius = float(message.text.split()[1])
        bot.reply_to(message, f"Площадь круга: {get_circle_area(radius):.2f}")
    except (IndexError, ValueError):
        bot.reply_to(message, "Используйте: /circle [радиус]")

@bot.message_handler(commands=['time'])
def handle_time(message):
    bot.reply_to(message, f"Текущее время: {get_current_time()}")

bot.polling()

import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import config as cfg
import markups as nav
import json

API_TOKEN = cfg.TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
#PROXY_URL = 'http://proxy.server:3128'
#bot = Bot(token=cfg.TOKEN, proxy=PROXY_URL)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Создаем функцию для загрузки JSON-файла с данными
def load_language_data(language_code):
    file_name = f"info_{language_code}.json"
    with open(file_name, "r", encoding="utf-8") as json_file:
        return json.load(json_file)

'''
@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/cats.jpg', 'rb') as photo:
        await bot.send_photo(message.chat.id, photo, caption='Kočky jsou zde 😺',
                             reply_to_message_id=message.message_id)
'''

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Отправляем сообщение с просьбой выбрать язык
    await message.answer("🌟 Пожалуйста, выберите предпочитаемый язык интерфейса 🌐\n\n🌍 Интерфейстің тілін таңдауыңызды сұраймыз 📣\n\n🌟 Please select your preferred interface language 🌐", reply_markup=nav.language_keyboard)

# Обработчик нажатий на кнопки клавиатуры
@dp.message_handler(lambda message: message.text in ["Қазақша", "Русский", "English"])
async def process_language(message: types.Message):
    if message.text == "Қазақша":
      selected_language = "kz"
    elif message.text == "Русский":
      selected_language = "ru"
    else:
      selected_language = "eng"

    # Загружаем данные для выбранного языка
    global uni_bot_data
    uni_bot_data = load_language_data(selected_language)

    # Создаем кнопки для меню
    btn_stud = KeyboardButton(text=uni_bot_data["buttons"]["student"]) #Студент
    btn_entr = KeyboardButton(text=uni_bot_data["buttons"]["applicant"]) #Абитуриент
    btn_alum = KeyboardButton(text=uni_bot_data["buttons"]["alumni_club"]) #Алумни
    btn_empl = KeyboardButton(text=uni_bot_data["buttons"]["employee"]) #Сотрудник
    btn_social = KeyboardButton(text=uni_bot_data["buttons"]["social_media"]) #Социальные сети
    btn_info = KeyboardButton(text=uni_bot_data["buttons"]["contacts"]) #Контакты
    btn_fb = KeyboardButton(text=uni_bot_data["buttons"]["feedback"]) #Предложения, замечания по Боту

    # Создаем клавиатуру с кнопками
    global menu_markup
    menu_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    menu_markup.row(btn_stud, btn_entr)
    menu_markup.row(btn_alum, btn_empl)
    menu_markup.add(btn_social)
    menu_markup.add(btn_info)
    menu_markup.add(btn_fb)

    # Создаем кнопки для меню студентов
    btn_stud1 = KeyboardButton(text=uni_bot_data["buttons"]["platonus"])
    btn_stud2 = KeyboardButton(text=uni_bot_data["buttons"]["corporate_mail"])
    btn_stud3 = KeyboardButton(text=uni_bot_data["buttons"]["institute_contacts"])
    btn_stud4 = KeyboardButton(text=uni_bot_data["buttons"]["tsak"])
    btn_stud5 = KeyboardButton(text=uni_bot_data["buttons"]["rector_blog"])
    btn_stud6 = KeyboardButton(text=uni_bot_data["buttons"]["reset_password"])
    btn_stud7 = KeyboardButton(text=uni_bot_data["buttons"]["accounting"])
    btn_stud8 = KeyboardButton(text=uni_bot_data["buttons"]["faq"])
    btn_stud9 = KeyboardButton(text=uni_bot_data["buttons"]["back"])

    # Создаем клавиатуру с кнопками для меню студентов
    global stud_menu_markup
    stud_menu_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    stud_menu_markup.row(btn_stud1, btn_stud2)
    stud_menu_markup.row(btn_stud3, btn_stud4)
    stud_menu_markup.row(btn_stud5, btn_stud6)
    stud_menu_markup.row(btn_stud7, btn_stud8)
    stud_menu_markup.add(btn_stud9)

    # Создаем кнопки для меню абитуриентов
    btn_bachelor = KeyboardButton(text=uni_bot_data["buttons"]["bachelor_degree"])
    btn_master = KeyboardButton(text=uni_bot_data["buttons"]["master_degree"])
    btn_phd = KeyboardButton(text=uni_bot_data["buttons"]["doctoral_degree"])
    btn_college = KeyboardButton(text=uni_bot_data["buttons"]["college"])
    btn_courses = KeyboardButton(text=uni_bot_data["buttons"]["entrance_exam_courses"])

    # Создаем клавиатуру с кнопками для меню абитуриентов
    global applicant_menu_markup
    applicant_menu_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    applicant_menu_markup.add(btn_bachelor, btn_master)
    applicant_menu_markup.add(btn_phd, btn_college, btn_courses)
    applicant_menu_markup.add(btn_stud9)

    # Создаем кнопки для меню выпускников
    btn_alum1 = KeyboardButton(text=uni_bot_data["buttons"]["events"])
    btn_alum2 = KeyboardButton(text=uni_bot_data["buttons"]["join_club"])
    btn_alum3 = KeyboardButton(text=uni_bot_data["buttons"]["alumni_contacts"])

    # Создаем клавиатуру с кнопками для меню выпускников
    global alumni_menu_markup
    alumni_menu_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    alumni_menu_markup.add(btn_alum1)
    alumni_menu_markup.add(btn_alum2)
    alumni_menu_markup.add(btn_alum3)
    alumni_menu_markup.add(btn_stud9)

    # Создаем кнопки для меню сотрудников
    btn_dit_application = KeyboardButton(text=uni_bot_data["buttons"]["dit_application"])
    btn_documents_templates = KeyboardButton(text=uni_bot_data["buttons"]["documents_templates"])
    btn_qa = KeyboardButton(text=uni_bot_data["buttons"]["qa"])

    # Создаем клавиатуру с кнопками для меню сотрудников
    global employee_menu_markup
    employee_menu_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    employee_menu_markup.row(btn_dit_application)
    employee_menu_markup.row(btn_documents_templates)
    employee_menu_markup.row(btn_qa)
    employee_menu_markup.add(btn_stud9)

    await message.answer(uni_bot_data["general_info"]["greeting"], reply_markup=menu_markup)

# Обработчик нажатия на кнопку "Студент"
@dp.message_handler(lambda message: message.text == uni_bot_data["buttons"]["student"])
async def stud(message: types.Message):
    await bot.send_message(message.chat.id, "Студентам", reply_markup=stud_menu_markup)

# Обработчик нажатия на кнопку "Абитуриент"
@dp.message_handler(lambda message: message.text == uni_bot_data["buttons"]["applicant"])
async def entr(message: types.Message):
    await bot.send_message(message.chat.id, "Программы", reply_markup=applicant_menu_markup)

# Обработчик нажатия на кнопку "Выпускник Alumni club"
@dp.message_handler(lambda message: message.text == uni_bot_data["buttons"]["alumni_club"])
async def alum(message: types.Message):
    await bot.send_message(message.chat.id, "Ассоциация выпускников - подразделение, организующее взаимодействие выпускников с вузом.", reply_markup=alumni_menu_markup)

# Обработчик нажатия на кнопку "Сотрудник"
@dp.message_handler(lambda message: message.text == uni_bot_data["buttons"]["employee"])
async def empl(message: types.Message):
    await bot.send_message(message.chat.id, "Сотрудникам", reply_markup=employee_menu_markup)

# Обработчик нажатия на кнопку "Социальные сети"
@dp.message_handler(lambda message: message.text == uni_bot_data["buttons"]["social_media"])
async def social(message: types.Message):
    await bot.send_message(message.chat.id, uni_bot_data["general_info"]["social"], parse_mode="Markdown")

# Обработчик нажатия на кнопку "Контакты"
@dp.message_handler(lambda message: message.text == uni_bot_data["buttons"]["contacts"])
async def info(message: types.Message):
    await bot.send_message(message.chat.id, uni_bot_data["general_info"]["contacts"], parse_mode="Markdown")

# Обработчик нажатия на кнопку "Предложения, замечания по Боту"
@dp.message_handler(lambda message: message.text == uni_bot_data["buttons"]["feedback"])
async def feedback_handler(message: types.Message):
    await message.answer("Есть предложения или замечания по работе Бота? Пожалуйста, оставьте свой отзыв [здесь](https://forms.gle/c4zobjd6ob3DzXHJA).", parse_mode="Markdown")
  
# Обработчик нажатия на кнопки со ссылками
@dp.message_handler(lambda message: message.text in [uni_bot_data["buttons"]["platonus"], uni_bot_data["buttons"]["corporate_mail"], uni_bot_data["buttons"]["rector_blog"], uni_bot_data["buttons"]["reset_password"]])
async def send_link(message: types.Message):
    if message.text == uni_bot_data["buttons"]["platonus"]:
        await message.answer("Система управления учебным процессом АУЭС: [Platonus](https://edu2.aues.kz/)", parse_mode="Markdown")
    elif message.text == uni_bot_data["buttons"]["corporate_mail"]:
        await message.answer("Единая система корпоративной электронной почты: [Корпоративная почта](https://www.google.com/intl/ru/gmail/about/)", parse_mode="Markdown")
    elif message.text == uni_bot_data["buttons"]["rector_blog"]:
        await message.answer("Информация об университете, ключевые сведения, обращение ректора: [Блог ректора](https://aues.edu.kz/ru/site/blog-rektora)", parse_mode="Markdown")
    elif message.text == uni_bot_data["buttons"]["reset_password"]:
        await message.answer("Если забыли или хотите поменять пароль на своей почте, жмите сюда: [Сброс пароля](https://recovery.aues.kz/new-sbros.php)", parse_mode="Markdown")

# Обработчик нажатия на кнопку "Контакты институтов" (если необходимо)
@dp.message_handler(lambda message: message.text == uni_bot_data["buttons"]["institute_contacts"])
async def contacts(message: types.Message):
    await message.answer(uni_bot_data["student_info"]["inst"]["full_info"], parse_mode="Markdown")

# Обработчик нажатия на кнопку "ЦАК" (если необходимо)
@dp.message_handler(lambda message: message.text == uni_bot_data["buttons"]["tsak"])
async def tsak(message: types.Message):
    await message.answer(uni_bot_data["student_info"]["tsak"], parse_mode="Markdown")

# Обработчик нажатия на кнопку "Бухгалтерия" (если необходимо)
@dp.message_handler(lambda message: message.text == uni_bot_data["buttons"]["accounting"])
async def accounting(message: types.Message):
    await message.answer(uni_bot_data["student_info"]["ACC"], parse_mode="Markdown")

# Обработчик нажатия на кнопку "Вопрос-ответ" (если необходимо)
@dp.message_handler(lambda message: message.text == uni_bot_data["buttons"]["faq"])
async def faq(message: types.Message):
    await message.answer(uni_bot_data["QADataset"]["student"], parse_mode="Markdown")

# Обработчик нажатия на кнопку "Назад" (если необходимо)
@dp.message_handler(lambda message: message.text == uni_bot_data["buttons"]["back"])
async def back(message: types.Message):
    await message.answer("Возвращаемся в главное меню", reply_markup=menu_markup)

# Обработчик нажатия на кнопки меню абитуриентов
@dp.message_handler(lambda message: message.text in [uni_bot_data["buttons"]["bachelor_degree"], uni_bot_data["buttons"]["master_degree"], uni_bot_data["buttons"]["doctoral_degree"], uni_bot_data["buttons"]["college"], uni_bot_data["buttons"]["entrance_exam_courses"]])
async def send_admission_link(message: types.Message):
    if message.text == uni_bot_data["buttons"]["bachelor_degree"]:
        await message.answer("Информация для поступления в бакалавриат смотреть [здесь](https://aues.edu.kz/ru/bachelor)", parse_mode="Markdown")
    elif message.text == uni_bot_data["buttons"]["master_degree"]:
        await message.answer("Информация для поступления в магистратуру смотреть [здесь](https://aues.edu.kz/ru/magistracy)", parse_mode="Markdown")
    elif message.text == uni_bot_data["buttons"]["doctoral_degree"]:
        await message.answer("Информация для поступления в докторантуру смотреть [здесь](https://aues.edu.kz/ru/doctorate)", parse_mode="Markdown")
    elif message.text == uni_bot_data["buttons"]["college"]:
        await message.answer("Информация для поступления в колледж смотреть [здесь](https://aues.edu.kz/ru/site/college)", parse_mode="Markdown")
    elif message.text == uni_bot_data["buttons"]["entrance_exam_courses"]:
        await message.answer("Курсы ЕНТ помогут в подготовке к единому национальному тестированию. [Подробнее здесь](https://aues.edu.kz/ru/kursy-ent)", parse_mode="Markdown")

# Обработчики нажатия на кнопки в меню выпускников
@dp.message_handler(lambda message: message.text in [uni_bot_data["buttons"]["events"]])
async def send_event_link(message: types.Message):
    if message.text == uni_bot_data["buttons"]["events"]:
        # Send the media group
        media = types.MediaGroup()
        media.attach_photo(types.InputFile('data/photo_1.jpg'), 'Дискуссия попечительского совета АУЭС о кадровом голоде в отрасли')
        media.attach_photo(types.InputFile('data/photo_4.jpg'), 'Встреча выпускников 2001-2002 годов в Energo University')
        media.attach_photo(types.InputFile('data/photo_5.jpg'), 'Встреча выпускника "Alumni club ЭНЕРГО" в Energo University')
        media.attach_photo(types.InputFile('data/photo_6.jpg'), 'Двойное мероприятие в рамках Alumni club в Energo University')
        media.attach_photo(types.InputFile('data/photo_7_1.jpg'), 'Встреча студентов с основателем Supros engineering & Supply')
        media.attach_photo(types.InputFile('data/photo_7_2.jpg'), 'Встреча студентов с основателем Supros engineering & Supply')
        await bot.send_media_group(message.chat.id, media=media)

        # Send the caption message
        await bot.send_message(message.chat.id, uni_bot_data["alumni_club"]["events_details"])

@dp.message_handler(lambda message: message.text == uni_bot_data["buttons"]["join_club"])
async def join_club(message: types.Message):
    await message.answer("Извините, запрошенная вами информация недоступна.")

@dp.message_handler(lambda message: message.text == uni_bot_data["buttons"]["alumni_contacts"])
async def alumni_contacts(message: types.Message):
    await message.answer("Извините, запрошенная вами информация недоступна.")

# Обработчики нажатия на кнопки в меню сотрудников
# Обработчик нажатия на кнопку "Заявка в ДИТ"
@dp.message_handler(lambda message: message.text == uni_bot_data["buttons"]["dit_application"])
async def dit_application(message: types.Message):
    await message.answer("Извините, запрошенная вами информация недоступна.")

# Обработчик нажатия на кнопку "Документы, шаблоны"
@dp.message_handler(lambda message: message.text == uni_bot_data["buttons"]["documents_templates"])
async def documents_templates(message: types.Message):
    await message.answer("Извините, запрошенная вами информация недоступна.")

# Обработчик нажатия на кнопку "Вопросы, ответы"
@dp.message_handler(lambda message: message.text == uni_bot_data["buttons"]["qa"])
async def qa(message: types.Message):
    await message.answer("Извините, запрошенная вами информация недоступна.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
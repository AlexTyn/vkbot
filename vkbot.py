import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import pymysql.cursors
import requests
import wikipedia
import re
from math import sqrt
words = {
"why": ["почему", "почему?"],
"hello": ["начать", "привет", "хай", "хей", "здравствуй", "здравствуйте", "здарова"]
}
wikipedia.set_lang("RU")
osinniki = [53.577475, 53.658998, 87.277901, 87.451449]
lenin = [53.598598, 87.338041]
lion = [53.598330, 87.330634]
pandf = [53.600084, 87.337079]
"""
def get_connection():
    connection = pymysql.connect(host='you_host',
                                 user='you_user',
                                 password='you_password',
                                 db='you_db'
                                 charset='utf8mb4',
                                 cursorclass=mymysql.cursors.DictCursor)
    return connection
"""
vk_session = vk_api.VkApi(token="84f5135f5087af2ad34de6fa05a40ea44d4d6b70364fbc9ebd519860233eeab6bce5b7bc00d2d951dc908")
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, "2789c566")
n = 0
k = 0
s = 0
p = 0
for event in longpoll.listen(): #Проверка действий
	if event.type == VkBotEventType.MESSAGE_NEW:
		i = 0
		for word in words["why"]:
			if event.obj.text.lower() == word:
				i = 1
				if event.from_user:
					vk.messages.send(
						user_id=event.obj.from_id,
						random_id=get_random_id(),
						message="Это жизнь🙃")
		if event.obj.text.lower() == "жизнь":
				i = 1
				if event.from_user:
					vk.messages.send(
							user_id=event.obj.from_id,
							random_id=get_random_id(),
							message="- боль")
		if s == 1 and p == 1:
			try:
				keyboard3 = VkKeyboard(one_time = True)
				keyboard3.add_location_button()
				geo = event.obj.geo
				coordinates = geo.get("coordinates")
				latitude = coordinates.get("latitude")
				longitude = coordinates.get("longitude")
				if osinniki[0] < latitude and latitude < osinniki[1] and osinniki[2] < longitude and longitude < osinniki[3]:
					latitude1 = abs(lenin[0] - latitude) * 111135
					latitude2 = abs(lion[0] - latitude) * 111135
					latitude3 = abs(pandf[0] - latitude) * 111135
					longitude1 = abs(lenin[1] - longitude) * 111321
					longitude2 = abs(lion[1] - longitude) * 111321
					longitude3 = abs(pandf[1] - longitude) * 111321
					distance1 = round(sqrt(latitude1**2 + longitude1**2))
					distance2 = round(sqrt(latitude2**2 + longitude2**2))
					distance3 = round(sqrt(latitude3**2 + longitude3**2))
					if distance1 < 20:
						vk.messages.send(
							user_id=event.obj.from_id,
							random_id=get_random_id(),
							keyboard=keyboard3.get_keyboard(),
							message="Отлично!\nТы дошёл до Памятника В.И.Ленину :D")
						vk.messages.send(
							user_id=event.obj.from_id,
							random_id=get_random_id(),
							keyboard=keyboard3.get_keyboard(),
							message="✅Памятник В.И.Ленину - " + str(distance1) + " м" + "\nФонтан \"Лев\" - " + str(distance2) + " м" + "\nПамятник Петру и Февронии - " + str(distance3) + " м")
					elif distance2 < 20:
						vk.messages.send(
							user_id=event.obj.from_id,
							random_id=get_random_id(),
							keyboard=keyboard3.get_keyboard(),
							message="Отлично!\nТы около Фонтана \"Лев\" :D")
						vk.messages.send(
							user_id=event.obj.from_id,
							random_id=get_random_id(),
							keyboard=keyboard3.get_keyboard(),
							message="Памятник В.И.Ленину - " + str(distance1) + " м" + "\n✅Фонтан \"Лев\" - " + str(distance2) + " м" + "\nПамятник Петру и Февронии - " + str(distance3) + " м")
					elif distance3 < 20:
						vk.messages.send(
							user_id=event.obj.from_id,
							random_id=get_random_id(),
							keyboard=keyboard3.get_keyboard(),
							message="Отлично!\nТы находишься около Памятника Петру и Февронии 👌")
						vk.messages.send(
							user_id=event.obj.from_id,
							random_id=get_random_id(),
							keyboard=keyboard3.get_keyboard(),
							message="Памятник В.И.Ленину - " + str(distance1) + " м" + "\nФонтан \"Лев\" - " + str(distance2) + " м" + "\n✅Памятник Петру и Февронии - " + str(distance3) + " м")
					else:
						vk.messages.send(
							user_id=event.obj.from_id,
							random_id=get_random_id(),
							message="Город Осинники\nДостопримечательности и расстояния до них:\n" + "• Памятник В.И.Ленину - " + str(distance1) + " м" + "\n• Фонтан \"Лев\" - " + str(distance2) + " м" + "\n• Памятник Петру и Февронии - " + str(distance3) + " м")
						vk.messages.send(
							user_id=event.obj.from_id,
							random_id=get_random_id(),
							keyboard=keyboard3.get_keyboard(),
							message="Когда будешь около достопримечательности, просто нажми на кнопку")
				else:
					vk.messages.send(
						user_id=event.obj.from_id,
						random_id=get_random_id(),
						message="Прости, но я пока не знаю твоего города :(")
					s = 0
				i = 1
			except:
				keyboard4 = VkKeyboard(one_time = True)
				keyboard4.add_button("Конечно!", color = VkKeyboardColor.POSITIVE)
				keyboard4.add_button("Может, позже", color = VkKeyboardColor.NEGATIVE)
				vk.messages.send(
					user_id=event.obj.from_id,
					random_id=get_random_id(),
					message="Без отправки местоположения ты не сможешь пройти квест😰")
				vk.messages.send(
					user_id=event.obj.from_id,
					random_id=get_random_id(),
					keyboard=keyboard4.get_keyboard(),
					message="Ты хочешь его пройти?")
				p = 0
				i = 1
		if event.obj.text.lower() == "конечно!" and s == 1 and p == 0:
			keyboard3 = VkKeyboard(one_time = True)
			keyboard3.add_location_button()
			vk.messages.send(
					user_id=event.obj.from_id,
					random_id=get_random_id(),
					keyboard=keyboard3.get_keyboard(),
					message="Тогда отправь мне свои координаты :3")
			p = 1
			i = 1
		elif event.obj.text.lower() == "может, позже" and s == 1 and p == 0:
			vk.messages.send(
					user_id=event.obj.from_id,
					random_id=get_random_id(),
					message="Поздоровайся со мной снова, когда будешь готов :3")
			p = 0
			s = 0
			i = 1
		if re.search(r"\bчто такое\b", str(event.obj.text.lower())):
			if event.from_user:
				try:
					vk.messages.send(
						user_id=event.obj.from_id,
						random_id=get_random_id(),
						message=wikipedia.summary(str(event.obj.text.lower())[10:]))
				except:
					vk.messages.send(
						user_id=event.obj.from_id,
						random_id=get_random_id(),
						message="А вот этого я не знаю😔")
				i = 1
		for word in words["hello"]:
			if event.obj.text.lower() == word:
				i = 1
	            #проверяем пришло сообщение от пользователя или нет
				if event.from_user:
					keyboard1 = VkKeyboard(one_time = True)
					keyboard1.add_button("Ага", color = VkKeyboardColor.POSITIVE)
					keyboard1.add_button("Не-а", color = VkKeyboardColor.NEGATIVE)
					vk.messages.send(
							user_id=event.obj.from_id,
							random_id=get_random_id(),
							message="Привет)")
					vk.messages.send(
							user_id=event.obj.from_id,
							random_id=get_random_id(),
							keyboard=keyboard1.get_keyboard(),
							message="Хочешь пройти квест?"
							)
					i = 1
					n = 1
		if event.obj.text.lower() == "ага" and n == 1:
			if event.from_user:
				keyboard2 = VkKeyboard(one_time = True)
				keyboard2.add_button("Осинники", color = VkKeyboardColor.PRIMARY)
				keyboard2.add_button("Новокузнецк", color = VkKeyboardColor.PRIMARY)
				keyboard2.add_line()
				keyboard2.add_button("Кемерово", color = VkKeyboardColor.PRIMARY)
				keyboard2.add_button("???", color = VkKeyboardColor.PRIMARY)
				vk.messages.send(
						user_id=event.obj.from_id,
						random_id=get_random_id(),
						keyboard=keyboard2.get_keyboard(),
						message="Тогда выбери свой город из списка😀")
				i = 1
				n = 0
				k = 1
		elif event.obj.text.lower() == "не-а" and n == 1:
			if event.from_user:
				vk.messages.send(
						user_id=event.obj.from_id,
						random_id=get_random_id(),
						message="Возвращайся, когда будешь готов :D")
				i = 1
				n = 0
		if event.obj.text.lower() == "осинники" and k == 1:
			if event.from_user:
				keyboard3 = VkKeyboard(one_time = True)
				keyboard3.add_location_button()
				vk.messages.send(
					user_id=event.obj.from_id,
					random_id=get_random_id(),
					keyboard=keyboard3.get_keyboard(),
					message="Нажми на кнопку, чтоб я нашел ближайшую контрольную точку :D")
				s = 1
				p = 1
				i = 1
				k = 0
		if event.obj.text.lower() == "новокузнецк" and k == 1:
			if event.from_user:
				vk.messages.send(
					user_id=event.obj.from_id,
					random_id=get_random_id(),
					message="Coming soon..")
				i = 1
				k = 0
		if event.obj.text.lower() == "кемерово" and k == 1:
			if event.from_user:
				vk.messages.send(
					user_id=event.obj.from_id,
					random_id=get_random_id(),
					message="Coming soon..")
				i = 1
				k = 0
		if event.obj.text.lower() == "???" and k == 1:
			if event.from_user:
				vk.messages.send(
					user_id=event.obj.from_id,
					random_id=get_random_id(),
					message="Coming soon..")
				i = 1
				k = 0
		elif i == 0:
			if event.from_user:
						vk.messages.send(
								user_id=event.obj.from_id,
								random_id=get_random_id(),
								message="Я не понимать ;(")

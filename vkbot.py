from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text
from vkbottle import BaseStateGroup
from vkbottle import CtxStorage
from vkbottle import DocMessagesUploader
import sqlite3
import datetime


bot = Bot(token="token")
ctx = CtxStorage()

class RegData(BaseStateGroup):

    OSHY = 0
    NUMBER1 = 1
    NUMBER2 = 2
    NUMBER3 = 3



@bot.on.message(text=['Привет', 'Меню', 'Начать', 'привет', 'меню', 'начать', 'как дела',\
							'Как дела', 'что ты умеешь', 'Что ты умеешь', 'ку', 'Ку'])
@bot.on.message(payload={"cmd": "menu"})
async def menu_handler(message: Message):
	everyd = datetime.datetime.today()
	userq = await bot.api.users.get(message.from_id)
	inf = [userq[0].first_name, userq[0].last_name, userq[0].id, everyd.strftime("%d/%m/%Y")]
	tyy = message.from_id
	conn = sqlite3.connect('Vkbot.db')
	cursor = conn.cursor()
	cursor.execute(f"SELECT idred FROM Data WHERE idred = {tyy}")
	gera = cursor.fetchone()
	if gera is None:
		cursor.execute("INSERT INTO Data VALUES (?,?,?,?)", inf)
	conn.commit()
	conn.close()

	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Контактная информация учителей", {"cmd": "inf"}), color=KeyboardButtonColor.POSITIVE)
		.row()
		.add(Text("Подать заявление в школу", {"cmd": "zai"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Список отсутствующих", {"cmd": "spisok"}), color=KeyboardButtonColor.PRIMARY)
		.row()
		.add(Text("Ошибка", {"cmd": "oshi"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("О программе", {"cmd": "prog"}))
		)

	await message.answer("Привет, я бот!\n🔎 Выбери из меню, что ты хочешь узнать.", keyboard=keyboard)



@bot.on.message(text=['Данные', 'данные', 'информация', 'Информация', 'Контакты', 'контакты'])
@bot.on.message(payload={"cmd": "inf"})
async def inf_handler(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Математика", {"prm": "mat"}), color=KeyboardButtonColor.NEGATIVE)
		.add(Text("Физика", {"prm": "fiz"}), color=KeyboardButtonColor.POSITIVE)
		.row()
		.add(Text("Иностранный язык", {"prm": "inostr"}), color=KeyboardButtonColor.POSITIVE)
		.add(Text("Информатика", {"prm": "inform"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Русский язык (Литература)", {"prm": "lit"}), color=KeyboardButtonColor.PRIMARY)
		.row()
		.add(Text("Биология", {"prm": "bio"}), color=KeyboardButtonColor.NEGATIVE)
		.add(Text("Химия", {"prm": "xim"}), color=KeyboardButtonColor.POSITIVE)
		.row()
		.add(Text("Музыка", {"prm": "muz"}), color=KeyboardButtonColor.POSITIVE)
		.add(Text("Обществознание", {"prm": "obs"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("География", {"prm": "geo"}), color=KeyboardButtonColor.PRIMARY)
		.add(Text("Технология", {"prm": "texn"}), color=KeyboardButtonColor.NEGATIVE)
		.add(Text("История", {"prm": "istor"}), color=KeyboardButtonColor.POSITIVE)
		.row()
		.add(Text("ИЗО", {"prm": "izo"}), color=KeyboardButtonColor.POSITIVE)
		.add(Text("Физкультура", {"prm": "fizra"}), color=KeyboardButtonColor.PRIMARY)
		.add(Text("ОБЖ", {"prm": "obj"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}))
		)

	await message.answer("✅ Контактные данные учителя какого 📚 предмета ты хочешь узнать?\n\
✏ Или просто напиши имя и отчество учителя.", keyboard=keyboard)


@bot.on.message(text=['Метематика', 'математика', 'Матеша', 'матеша', 'алгебра', 'алгебра', 'геометрия', 'Геометрия'])
@bot.on.message(payload={"prm": "mat"})
async def match_handler(message: Message):
	keyboard = (
		Keyboard(inline=True)
		.add(Text("Бехметьева Юлия Владимировна", {"teather": "matbex"}), color=KeyboardButtonColor.PRIMARY)
		.row()
		.add(Text("Гильмутдинова Зоя Васильевна", {"teather": "matgil"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Гараева Светлана Анатольевна", {"teather": "matgar"}), color=KeyboardButtonColor.POSITIVE)
		.row()
		.add(Text("Павлова Надежда Валентиновна", {"teather": "matpav"}), color=KeyboardButtonColor.PRIMARY)
		.row()
		.add(Text("Рябова Жанна Владимировна", {"teather": "matrjb"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Ядрова Ольга Викторовна", {"teather": "matjad"}), color=KeyboardButtonColor.POSITIVE)
		)

	await message.answer("✅ Выбери учителя математике\n(Все ФИО в алфавитном порядке)", keyboard=keyboard)

	keyboard = Keyboard(inline=True).add(Text("⬅️", {"cmd": "inf"}))

	await message.answer("📚 Выбор предмета", keyboard=keyboard)


@bot.on.message(text=['Физика', 'физика', 'физ', 'Физ'])
@bot.on.message(payload={"prm": "fiz"})
async def fizika_handler(message: Message):
	keyboard = (
		Keyboard(inline=True)
		.add(Text("Гараев Игорь Васильевич", {"teather": "fizgar"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Калинина Алефтина Алексеевна", {"teather": "fizkal"}), color=KeyboardButtonColor.POSITIVE)
		)

	await message.answer("✅ Выбери учителя физики\n(Все ФИО в алфавитном порядке)", keyboard=keyboard)

	keyboard = Keyboard(inline=True).add(Text("⬅️", {"cmd": "inf"}))

	await message.answer("📚 Выбор предмета", keyboard=keyboard)


@bot.on.message(text=['иностранный язык', 'Иностранный язык', 'английский', 'Английский', 'англ', 'немецкий'])
@bot.on.message(payload={"prm": "inostr"})
async def inostran_handler(message: Message):
	keyboard = (
		Keyboard()
		.add(Text("Галимова Анастасия Валерьевна", {"teather": "inostrgal"}), color=KeyboardButtonColor.PRIMARY)
		.row()
		.add(Text("Комарова Надежда Борисовна", {"teather": "inostrkom"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Полубицкая Екатерина Леонидовна", {"teather": "inostrpol"}), color=KeyboardButtonColor.POSITIVE)
		.row()
		.add(Text("Самарина Елена Алексеевна", {"teather": "inostrsam"}), color=KeyboardButtonColor.PRIMARY)
		.row()
		.add(Text("Суханова Ирина Николаевна", {"teather": "inostrsux"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Сафина Светлана Валентиновна", {"teather": "inostrsaf"}), color=KeyboardButtonColor.POSITIVE)
		.row()
		.add(Text("Шляпина Наталья Анатольевна", {"teather": "inostrshla"}), color=KeyboardButtonColor.PRIMARY)
		.row()
		.add(Text("Шадрина Олеся Талгатовна", {"teather": "inostrshad"}), color=KeyboardButtonColor.NEGATIVE)
	)

	await message.answer("✅ Выбери учителя иностранного языка\n(Все ФИО в алфавитном порядке)", keyboard=keyboard)

	keyboard = Keyboard(inline=True).add(Text("⬅️", {"cmd": "inf"}))

	await message.answer("📚 Выбор предмета", keyboard=keyboard)


@bot.on.message(text=['Информатика', 'Инф'])
@bot.on.message(payload={"prm": "inform"})
async def inform_handler(message: Message):
	keyboard = (
		Keyboard(inline=True)
		.add(Text("Галлямова Галина Динусовна", {"teather": "informgal"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Пупышев Антон Алексеевич", {"teather": "informpup"}), color=KeyboardButtonColor.POSITIVE)
		)

	await message.answer("✅ Выбери учителя инорматике\n(Все ФИО в алфавитном порядке)", keyboard=keyboard)

	keyboard = Keyboard(inline=True).add(Text("⬅️", {"cmd": "inf"}))

	await message.answer("📚 Выбор предмета", keyboard=keyboard)


@bot.on.message(text=['Русский язык', 'Русский', 'Рус яз'])
@bot.on.message(payload={"prm": "lit"})
async def ry_handler(message: Message):
	keyboard = (
		Keyboard()
		.add(Text("Алексеева Елена Юрьевна", {"teather": "litale"}), color=KeyboardButtonColor.PRIMARY)
		.row()
		.add(Text("Винокурова Наталья Геннадьевна", {"teather": "litvin"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Гареева Гузалия Насимовна", {"teather": "litgar"}), color=KeyboardButtonColor.POSITIVE)
		.row()
		.add(Text("Каримова Гульнара Флюровна", {"teather": "litkar"}), color=KeyboardButtonColor.PRIMARY)
		.row()
		.add(Text("Костенкова Елена Викторовна", {"teather": "litkos"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Короткова Ирина Виленовна", {"teather": "litkor"}), color=KeyboardButtonColor.POSITIVE)
		.row()
		.add(Text("Калабина Светлана Аркадьевна", {"teather": "litkal"}), color=KeyboardButtonColor.PRIMARY)
		.row()
		.add(Text("Муратова Олеся Ленаровна", {"teather": "litmur"}), color=KeyboardButtonColor.NEGATIVE)
	)

	await message.answer("✅ Выбери учителя русского языка (литературы)\n(Все ФИО в алфавитном порядке)", keyboard=keyboard)

	keyboard = Keyboard(inline=True).add(Text("⬅️", {"cmd": "inf"}))

	await message.answer("📚 Выбор предмета", keyboard=keyboard)


@bot.on.message(text=['Биология', 'Био'])
@bot.on.message(payload={"prm": "bio"})
async def bio_handler(message: Message):
	keyboard = (
		Keyboard(inline=True)
		.add(Text("Деветьярова Елена Владимировна", {"teather": "boidev"}), color=KeyboardButtonColor.PRIMARY)
		.row()
		.add(Text("Зарипова Светлана Владимировна", {"teather": "boizar"}), color=KeyboardButtonColor.POSITIVE)
		)

	await message.answer("✅ Выбери учителя биологии\n(Все ФИО в алфавитном порядке)", keyboard=keyboard)

	keyboard = Keyboard(inline=True).add(Text("⬅️", {"cmd": "inf"}))

	await message.answer("📚 Выбор предмета", keyboard=keyboard)


@bot.on.message(text=['Химия', 'Хим'])
@bot.on.message(payload={"prm": "xim"})
async def xim_handler(message: Message):
	keyboard = (
		Keyboard(inline=True)
		.add(Text("Каримова Валерия Владимировна", {"teather": "ximkar"}), color=KeyboardButtonColor.NEGATIVE)
		)
		
	await message.answer("✅ Выбери учителя химии\n(Все ФИО в алфавитном порядке)", keyboard=keyboard)

	keyboard = Keyboard(inline=True).add(Text("⬅️", {"cmd": "inf"}))

	await message.answer("📚 Выбор предмета", keyboard=keyboard)


@bot.on.message(text=['География', 'Гео'])
@bot.on.message(payload={"prm": "geo"})
async def geogra_handler(message: Message):
	keyboard = (
		Keyboard(inline=True)
		.add(Text("Устюгова Елена Владимировна", {"teather": "geoyst"}), color=KeyboardButtonColor.NEGATIVE)
		)
		
	await message.answer("✅ Выбери учителя географии\n(Все ФИО в алфавитном порядке)", keyboard=keyboard)

	keyboard = Keyboard(inline=True).add(Text("⬅️", {"cmd": "inf"}))

	await message.answer("📚 Выбор предмета", keyboard=keyboard)


@bot.on.message(text="Технология")
@bot.on.message(payload={"prm": "texn"})
async def texnologia_handler(message: Message):
	keyboard = (
		Keyboard(inline=True)
		.add(Text("Буранова Ольга Александровна", {"teather": "texnbur"}), color=KeyboardButtonColor.POSITIVE)
		.row()
		.add(Text("Щербаков Валерий Сергеевич", {"teather": "texnsher"}), color=KeyboardButtonColor.NEGATIVE)
		)
		
	await message.answer("✅ Выбери учителя технологии\n(Все ФИО в алфавитном порядке)", keyboard=keyboard)

	keyboard = Keyboard(inline=True).add(Text("⬅️", {"cmd": "inf"}))

	await message.answer("📚 Выбор предмета", keyboard=keyboard)


@bot.on.message(text="История")
@bot.on.message(payload={"prm": "istor"})
async def istori_handler(message: Message):
	keyboard = (
		Keyboard(inline=True)
		.add(Text("Алабужева Юлия Сергеевна", {"teather": "istorala"}), color=KeyboardButtonColor.POSITIVE)
		.row()
		.add(Text("Зонова Ирина Анатольевна", {"teather": "istorzon"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Калинина Надежда Михайловна", {"teather": "istorkal"}), color=KeyboardButtonColor.PRIMARY)
		.row()
		.add(Text("Казанцева Светлана Алексеевна", {"teather": "istorkaz"}), color=KeyboardButtonColor.POSITIVE)
		.row()
		.add(Text("Моисеева Наталья Артемьевна", {"teather": "istormou"}), color=KeyboardButtonColor.NEGATIVE)
		)

	await message.answer("✅ Выбери учителя истории\n(Все ФИО в алфавитном порядке)", keyboard=keyboard)

	keyboard = Keyboard(inline=True).add(Text("⬅️", {"cmd": "inf"}))

	await message.answer("📚 Выбор предмета", keyboard=keyboard)


@bot.on.message(text="Музыка")
@bot.on.message(payload={"prm": "muz"})
async def muza_handler(message: Message):
	keyboard = (
		Keyboard(inline=True)
		.add(Text("Землянская Ирина Генадьевна", {"teather": "muzzem"}), color=KeyboardButtonColor.PRIMARY)
		.row()
		.add(Text("Моисеева Марина Александровна", {"teather": "muzmou"}), color=KeyboardButtonColor.POSITIVE)
		)

	await message.answer("✅ Выбери учителя музыки\n(Все ФИО в алфавитном порядке)", keyboard=keyboard)

	keyboard = Keyboard(inline=True).add(Text("⬅️", {"cmd": "inf"}))

	await message.answer("📚 Выбор предмета", keyboard=keyboard)


@bot.on.message(text="Обществознание")
@bot.on.message(payload={"prm": "obs"})
async def obs_handler(message: Message):
	keyboard = (
		Keyboard(inline=True)
		.add(Text("Казанова Алла Валерьевна", {"teather": "obskaz"}), color=KeyboardButtonColor.NEGATIVE)
		)
		
	await message.answer("✅ Выбери учителя обществознания\n(Все ФИО в алфавитном порядке)", keyboard=keyboard)
	
	keyboard = Keyboard(inline=True).add(Text("⬅️", {"cmd": "inf"}))

	await message.answer("📚 Выбор предмета", keyboard=keyboard)



@bot.on.message(text="ИЗО")
@bot.on.message(payload={"prm": "izo"})
async def izo_handler(message: Message):
	keyboard = (
		Keyboard(inline=True)
		.add(Text("Гоголева Надежда Леонидовна", {"teather": "izogog"}), color=KeyboardButtonColor.POSITIVE)
		)
		
	await message.answer("✅ Выбери учителя ИЗО\n(Все ФИО в алфавитном порядке)", keyboard=keyboard)

	keyboard = Keyboard(inline=True).add(Text("⬅️", {"cmd": "inf"}))

	await message.answer("📚 Выбор предмета", keyboard=keyboard)


@bot.on.message(text="Физкультура")
@bot.on.message(payload={"prm": "fizra"})
async def fizra_handler(message: Message):
	keyboard = (
		Keyboard(inline=True)
		.add(Text("Андриянов Дмитрий Николаевич", {"teather": "fizraand"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Завьялова Анастасия Александровна", {"teather": "fizrazav"}), color=KeyboardButtonColor.POSITIVE)
		.row()
		.add(Text("Москогло Дарья Михайловна", {"teather": "fizramos"}), color=KeyboardButtonColor.PRIMARY)
		.row()
		.add(Text("Черепанова Оксана Юрьевна", {"teather": "fizracher"}), color=KeyboardButtonColor.POSITIVE)
		.row()
		.add(Text("Якимова Ольга Николаевна", {"teather": "fizraaki"}), color=KeyboardButtonColor.NEGATIVE)
		)

	await message.answer("✅ Выбери учителя физкультуры\n(Все ФИО в алфавитном порядке)", keyboard=keyboard)

	keyboard = Keyboard(inline=True).add(Text("⬅️", {"cmd": "inf"}))

	await message.answer("📚 Выбор предмета", keyboard=keyboard)


@bot.on.message(text="ОБЖ")
@bot.on.message(payload={"prm": "obj"})
async def obj_handler(message: Message):
	keyboard = (
		Keyboard(inline=True)
		.add(Text("Луковников Александр Иванович", {"teather": "objluk"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Москов Виктор Николаевич", {"teather": "objmos"}), color=KeyboardButtonColor.POSITIVE)
		.row()
		.add(Text("Мигунов Сергей Иванович ", {"teather": "objmug"}), color=KeyboardButtonColor.PRIMARY)
		)

	await message.answer("✅ Выбери учителя ОБЖ\n(Все ФИО в алфавитном порядке)", keyboard=keyboard)

	keyboard = Keyboard(inline=True).add(Text("⬅️", {"cmd": "inf"}))

	await message.answer("📚 Выбор предмета", keyboard=keyboard)





@bot.on.message(text="Юлия Владимировна")
@bot.on.message(payload={"teather": "matbex"})
async def yl_teathermat(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "mat"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Бехметьева Юлия Владимировна, учитель метематики\n\nEmail:  Нет \
								\nVk: https://vk.com/behmetevaylia", keyboard=keyboard)

@bot.on.message(text="Зоя Васильевна")
@bot.on.message(payload={"teather": "matgil"})
async def zoi_teathermat(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "mat"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Гильмутдинова Зоя Васильевна, учитель метематики\n\nEmail: ajgrus@mail.ru \
								\nVk: https://vk.com/zoyavasilevna", keyboard=keyboard)

@bot.on.message(text="Светлана Анатольевна")
@bot.on.message(payload={"teather": "matgar"})
async def sveta_teathermat(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "mat"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Гараева Светлана Анатольевна, учитель метематики\n\nEmail: garaev1411@mail.ru \
								\nVk: https://vk.com/garaeva64", keyboard=keyboard)

@bot.on.message(text="Надежда Валентиновна")
@bot.on.message(payload={"teather": "matpav"})
async def nadia_teathermat(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "mat"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Павлова Надежда Валентиновна, учитель метематики\n\nEmail: nadya.pavlova.1962@list.ru \
								\nVk: https://vk.com/id173024274", keyboard=keyboard)

@bot.on.message(text="Жанна Владимировна")
@bot.on.message(payload={"teather": "matrjb"})
async def zhanna_teathermat(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "mat"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Рябова Жанна Владимировна, учитель метематики\n\nEmail: ryabova-1974@list.ru \
								\nVk: https://vk.com/id604291202", keyboard=keyboard)

@bot.on.message(text="Ольга Викторовна")
@bot.on.message(payload={"teather": "matjad"})
async def olga_teathermat(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "mat"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Ядрова Ольга Викторовна, учитель метематики\n\nEmail: jadrov2012@yandex.ru \
								\nVk: https://vk.com/id321808773", keyboard=keyboard)

@bot.on.message(text="Игорь Васильевич")
@bot.on.message(payload={"teather": "fizgar"})
async def igorek_tfiz(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "fiz"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Гараев Игорь Васильевич, учитель физики\n\nEmail: garaev1066@inbox.ru \
								\nVk: https://vk.com/id392973085", keyboard=keyboard)

@bot.on.message(text="Алефтина Алексеевна")
@bot.on.message(payload={"teather": "fizkal"})
async def alij_tfiz(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "fiz"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Калинина Алефтина Алексеевна, учитель физики\n\nEmail: Нет \
								\nVk: Нет", keyboard=keyboard)

@bot.on.message(text="Анастасия Валерьевна")
@bot.on.message(payload={"teather": "inostrgal"})
async def anastasia_tinostr(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "inostr"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Галимова Анастасия Валерьевна, учитель английского языка\n\nEmail: n.souvorova@gmail.com \
								\nVk: https://vk.com/shokolattt", keyboard=keyboard)

@bot.on.message(text="Комарова Надежда Борисовна")
@bot.on.message(payload={"teather": "inostrkom"})
async def naditer_tinostr(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "inostr"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Комарова Надежда Борисовна, учитель английского языка\n\nEmail: komarovanadezda385@gmail.com \
								\nVk: https://vk.com/id4515550", keyboard=keyboard)

@bot.on.message(text="Екатерина Леонидовна")
@bot.on.message(payload={"teather": "inostrpol"})
async def ekaterinz_tinostr(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "inostr"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Полубицкая Екатерина Леонидовна, учитель английского языка\n\nEmail: kat.pol1509@yandex.com \
								\nVk: https://vk.com/kuzametova", keyboard=keyboard)

@bot.on.message(text="Елена Алексеевна")
@bot.on.message(payload={"teather": "inostrsam"})
async def elenkaqq_tinostr(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "inostr"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Самарина Елена Алексеевна, учитель немецкого языка\n\nEmail: elena2018@yandex.ru \
								\nVk: https://vk.com/id157082892", keyboard=keyboard)

@bot.on.message(text="Ирина Николаевна")
@bot.on.message(payload={"teather": "inostrsux"})
async def irinkaq_tinostr(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "inostr"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Суханова Ирина Николаевна, учитель английского языка\n\nEmail: irishkakop130683@mail.ru \
								\nVk: https://vk.com/id394305607", keyboard=keyboard)

@bot.on.message(text="Светлана Валентиновна")
@bot.on.message(payload={"teather": "inostrsaf"})
async def svetlana_tinostr(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "inostr"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Сафина Светлана Валентиновна, учитель английского языка\n\nEmail: svetsvet0503@mail.ru \
								\nVk: https://vk.com/safina0503", keyboard=keyboard)

@bot.on.message(text="Наталья Анатольевна")
@bot.on.message(payload={"teather": "inostrshla"})
async def natal_tinostr(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "inostr"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Шляпина Наталья Анатольевна, учитель английского языка\n\nEmail: natasha.jwakina@yandex.ru \
								\nVk: https://vk.com/id18621302", keyboard=keyboard)

@bot.on.message(text="Олеся Талгатовна")
@bot.on.message(payload={"teather": "inostrshad"})
async def olesia_tinostr(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "inostr"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Шадрина Олеся Талгатовна, учитель английского языка\n\nEmail: talgatovna1@yandex.ru \
								\nVk: https://vk.com/id105887301", keyboard=keyboard)

@bot.on.message(text="Галина Динусовна")
@bot.on.message(payload={"teather": "informgal"})
async def galina_tinform(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "inform"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Галлямова Галина Динусовна, учитель информатики языка\n\nEmail: gallyamova_g@bk.ru \
								\nVk: https://vk.com/gg1967", keyboard=keyboard)

@bot.on.message(text="Антон Алексеевич")
@bot.on.message(payload={"teather": "informpup"})
async def anton_tinform(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "inform"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Пупышев Антон Алексеевич, учитель информатики языка\n\nEmail: Нет \
								\nVk: Нет", keyboard=keyboard)

@bot.on.message(text="Елена Юрьевна")
@bot.on.message(payload={"teather": "litale"})
async def elenklaq_tlit(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "lit"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Алексеева Елена Юрьевна, учитель русского языка и литературы\n\nEmail: alekseeva-1703@yandex.ru \
								\nVk: https://vk.com/id226642735", keyboard=keyboard)

@bot.on.message(text="Наталья Геннадьевна")
@bot.on.message(payload={"teather": "litvin"})
async def natalq_tlit(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "lit"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Винокурова Наталья Геннадьевна, учитель русского языка и литературы\n\nEmail: nata.vinokurova.000@mail.ru \
								\nVk: https://vk.com/id417591145", keyboard=keyboard)

@bot.on.message(text="Гузалия Насимовна")
@bot.on.message(payload={"teather": "litgar"})
async def gyza_tlit(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "lit"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Гареева Гузалия Насимовна, учитель русского языка и литературы\n\nEmail: gareeva.78@list.ru \
								\nVk: https://vk.com/id538283876", keyboard=keyboard)

@bot.on.message(text="Гульнара Флюровна")
@bot.on.message(payload={"teather": "litkar"})
async def gylnara_tlit(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "lit"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Каримова Гульнара Флюровна, учитель русского языка и литературы\n\nEmail: karimova024@mail.ru \
								\nVk: https://vk.com/id154801215", keyboard=keyboard)

@bot.on.message(text="Елена Викторовна")
@bot.on.message(payload={"teather": "litkos"})
async def eleqw_tlit(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "lit"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Костенкова Елена Викторовна, учитель русского языка и литературы\n\nEmail: kostenkova_yelena@mail.ru \
								\nVk: https://vk.com/id477205336", keyboard=keyboard)

@bot.on.message(text="Ирина Виленовна")
@bot.on.message(payload={"teather": "litkor"})
async def irinka_tlit(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "lit"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Короткова Ирина Виленовна, учитель русского языка и литературы\n\nEmail: maneww67@mail.ru \
								\nVk: https://vk.com/id175917902", keyboard=keyboard)

@bot.on.message(text="Светлана Аркадьевна")
@bot.on.message(payload={"teather": "litkal"})
async def svetys_tlit(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "lit"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Калабина Светлана Аркадьевна, учитель русского языка и литературы\n\nEmail: amper7@yandex.ru \
								\nVk: Нет", keyboard=keyboard)

@bot.on.message(text="Олеся Ленаровна")
@bot.on.message(payload={"teather": "litmur"})
async def oleska_tlit(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "lit"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Муратова Олеся Ленаровна, учитель русского языка и литературы\n\nEmail: Нет \
								\nVk: https://vk.com/muratova_oll", keyboard=keyboard)

@bot.on.message(text="Елена Владимировна")
@bot.on.message(payload={"teather": "boidev"})
async def elena_tbio(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "bio"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Деветьярова Елена Владимировна, учитель биологии\n\nEmail: devetyarova1979@mail.ru \
								\nVk: https://vk.com/id167710072", keyboard=keyboard)

@bot.on.message(text="Светлана Владимировна")
@bot.on.message(payload={"teather": "boizar"})
async def sveta_tbio(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "bio"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Зарипова Светлана Владимировна, учитель биологии\n\nEmail: luiza.zaripova.2015@mail.ru \
								\nVk: https://vk.com/id589270237", keyboard=keyboard)

@bot.on.message(text="Валерия Владимировна")
@bot.on.message(payload={"teather": "ximkar"})
async def valera_txim(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "xim"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Каримова Валерия Владимировна, учитель химии\n\nEmail: walerijas@mail.ru \
								\nVk: https://vk.com/id155058544", keyboard=keyboard)

@bot.on.message(text="Елена Владимировна")
@bot.on.message(payload={"teather": "geoyst"})
async def elenka_tgeo(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "geo"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Устюгова Елена Владимировна, учитель географии\n\nEmail: ustygova567@gmail.com \
								\nVk: https://vk.com/id241459681", keyboard=keyboard)

@bot.on.message(text="Юлия Сергеевна")
@bot.on.message(payload={"teather": "istorala"})
async def ylia_tistor(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "istor"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Алабужева Юлия Сергеевна, учитель истории\n\nEmail: aus2017udm@mail.ru \
								\nVk: https://vk.com/id56450007", keyboard=keyboard)

@bot.on.message(text="Ирина Анатольевна")
@bot.on.message(payload={"teather": "istorzon"})
async def irisha_tistor(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "istor"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Зонова Ирина Анатольевна, учитель истории\n\nEmail: sonovaia@mail.ru \
								\nVk: https://vk.com/sonovaia", keyboard=keyboard)

@bot.on.message(text="Надежда Михайловна")
@bot.on.message(payload={"teather": "istorkal"})
async def nad_tistor(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "istor"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Калинина Надежда Михайловна, учитель истории\n\nEmail: sergey11@udm.net \
								\nVk: https://vk.com/id462757808", keyboard=keyboard)

@bot.on.message(text="Светлана Алексеевна")
@bot.on.message(payload={"teather": "istorkaz"})
async def sveq_tistor(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "istor"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Казанцева Светлана Алексеевна, учитель истории\n\nEmail: ksaur74@mail.ru \
								\nVk: https://vk.com/id296202215", keyboard=keyboard)

@bot.on.message(text="Наталья Артемьевна")
@bot.on.message(payload={"teather": "istormou"})
async def nata_tistor(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "istor"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Моисеева Наталья Артемьевна, учитель истории\n\nEmail: natamoiseeva1960@mail.ru \
								\nVk: https://vk.com/id237126617", keyboard=keyboard)

@bot.on.message(text="Ирина Генадьевна")
@bot.on.message(payload={"teather": "muzzem"})
async def irina_tmuz(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "muz"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Землянская Ирина Генадьевна, учитель музыки\n\nEmail: irazemlyanskaya2017@bk.ru \
								\nVk: https://vk.com/id625909580", keyboard=keyboard)

@bot.on.message(text="Марина Александровна")
@bot.on.message(payload={"teather": "muzmou"})
async def marinka_tmuz(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "muz"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Моисеева Марина Александровна, учитель музыки\n\nEmail: Нет \
								\nVk: https://vk.com/id64314874", keyboard=keyboard)

@bot.on.message(text="Алла Валерьевна")
@bot.on.message(payload={"teather": "obskaz"})
async def alla_tobs(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "obs"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Казанова Алла Валерьевна, учитель обществознания\n\nEmail: alla.kazanova@yndex.ru \
								\nVk: https://vk.com/id466476448", keyboard=keyboard)

@bot.on.message(text="Надежда Леонидовна")
@bot.on.message(payload={"teather": "izogog"})
async def nadj_tizo(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "izo"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Гоголева Надежда Леонидовна, учитель ИЗО\n\nEmail: super.leonid41@yandex.ru \
								\nVk: Нет", keyboard=keyboard)

@bot.on.message(text="Дмитрий Николаевич")
@bot.on.message(payload={"teather": "fizraand"})
async def dmitr_tfizra(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "fizra"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Андриянов Дмитрий Николаевич, учитель физкультуры\n\nEmail: d_kamar@mail.ru \
								\nVk: https://vk.com/id79574772", keyboard=keyboard)

@bot.on.message(text="Анастасия Александровна")
@bot.on.message(payload={"teather": "fizrazav"})
async def anast_tfizra(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "fizra"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Завьялова Анастасия Александровна, учитель физкультуры\n\nEmail: nastasya.zavyalova@yandex.ru \
								\nVk: https://vk.com/id218503313", keyboard=keyboard)

@bot.on.message(text="Дарья Михайловна")
@bot.on.message(payload={"teather": "fizramos"})
async def dasha_tfizra(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "fizra"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Москогло Дарья Михайловна, учитель физкультуры\n\nEmail: Нет \
								\nVk: https://vk.com/id244973411", keyboard=keyboard)

@bot.on.message(text="Оксана Юрьевна")
@bot.on.message(payload={"teather": "fizracher"})
async def oksana_tfizra(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "fizra"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Черепанова Оксана Юрьевна, учитель физкультуры\n\nEmail: Нет \
								\nVk: Нет", keyboard=keyboard)

@bot.on.message(text="Ольга Николаевна")
@bot.on.message(payload={"teather": "fizraaki"})
async def olgaq_tfizra(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "fizra"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Якимова Ольга Николаевна, учитель физкультуры\n\nEmail: Нет \
								\nVk: Нет", keyboard=keyboard)

@bot.on.message(text="Александр Иванович")
@bot.on.message(payload={"teather": "objluk"})
async def aleks_tobj(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "obj"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Луковников Александр Иванович, учитель ОБЖ\n\nEmail: Нет \
								\nVk: Нет", keyboard=keyboard)

@bot.on.message(text="Виктор Николаевич")
@bot.on.message(payload={"teather": "objmos"})
async def viktor_tobj(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "obj"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Москов Виктор Николаевич, учитель ОБЖ\n\nEmail: Нет \
								\nVk: Нет", keyboard=keyboard)

@bot.on.message(text="Сергей Иванович")
@bot.on.message(payload={"teather": "objmug"})
async def sergeo_tobj(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "obj"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Мигунов Сергей Иванович, учитель ОБЖ\n\nEmail: Нет \
								\nVk: Нет", keyboard=keyboard)

@bot.on.message(text="Ольга Александровна")
@bot.on.message(payload={"teather": "texnbur"})
async def olga_ttexn(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "texn"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Буранова Ольга Александровна, учитель технологии\n\nEmail: olgaburanov@mail.ru \
								\nVk: https://vk.com/olgaburanova", keyboard=keyboard)

@bot.on.message(text="Валерий Сергеевич")
@bot.on.message(payload={"teather": "texnsher"})
async def vakeraq_ttexn(message: Message):
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"prm": "texn"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("Щербаков Валерий Сергеевич, учитель технологии\n\nEmail: Нет \
								\nVk: Нет", keyboard=keyboard)



@bot.on.message(text="Заявление")
@bot.on.message(payload={"cmd": "zai"})
async def zai_handler(message: Message):
	keyboard = ( 
	Keyboard(one_time=True)
	.add(Text("Заявление в 1 класс", {"zaya": "num1"}))
	.row()
	.add(Text("Заявление на льготу платных услуг", {"zaya": "num2"}))
	.row()
	.add(Text("Заявление на освобождение от занятий", {"zaya": "num3"}))
	.row()
	.add(Text("→", {"cmd": "zai"}), color=KeyboardButtonColor.POSITIVE)
	.row()
	.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.NEGATIVE)
	)
	await message.answer("🧾 В этом разделе вы можете подать любое заявление в школу.\n\
✅ Выберите из списка заявление, которое хотите подать.\n\n\
СТРАНИЦА 1.\n\n\
(чтобы перейти к следующей странице нажмите на стрелку)", keyboard=keyboard)


@bot.on.message(text="Заявление 1")
@bot.on.message(payload={"zaya": "num1"})
async def zayali_num1(message: Message):
	doc_apload = DocMessagesUploader(bot.api)
	docser = await doc_apload.upload("Форма заявления в 1 класс.doc", "Форма заявления в 1 класс.doc", peer_id=message.peer_id)
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"cmd": "zai"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("🧾 Пример формы заявления в 1 класс\n\n✅ Установите файл ворд, заполните поля и отправте обратно в чат.", keyboard=keyboard)
	await message.answer(attachment=docser)
	await message.answer("ожидание файла...")
	await bot.state_dispenser.set(message.peer_id, RegData.NUMBER1)


@bot.on.message(state=RegData.NUMBER1)
async def zakizka_handler(message: Message):
	keyboard = Keyboard(one_time=True).add(Text("Меню", {"cmd": "menu"}))
	userq1 = await bot.api.users.get(message.from_id)
	ctx.set("namber1", message.text)                                                                                            
	zaiva1 = ctx.get("namber1")
	qw = await message.answer("ожидайте...", keyboard=keyboard)
	await bot.api.messages.send(peer_id=291080599, message=f"Новое заявление в 1 класс от {userq1[0].first_name} {userq1[0].last_name}", random_id=0, forward_messages=qw.message_id-1, keyboard=keyboard)
	await bot.state_dispenser.delete(message.peer_id)
	return "✅ Ваше заявление отправленно на рассмотрение!"


@bot.on.message(text="Заявление 2")
@bot.on.message(payload={"zaya": "num2"})
async def zayali_num2(message: Message):
	doc_aplorty = DocMessagesUploader(bot.api)
	docqwea = await doc_aplorty.upload("Заявление на льготу платных услуг.doc", "Заявление на льготу платных услуг.doc", peer_id=message.peer_id)
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"cmd": "zai"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("🧾 Пример заявления на льготу платных услуг\n\n✅ Установите файл ворд, заполните поля и отправте обратно в чат.", keyboard=keyboard)
	await message.answer(attachment=docqwea)
	await message.answer("ожидание файла...")
	await bot.state_dispenser.set(message.peer_id, RegData.NUMBER2)


@bot.on.message(state=RegData.NUMBER2)
async def zakizka2_handler(message: Message):
	keyboard = Keyboard(one_time=True).add(Text("Меню", {"cmd": "menu"}))
	userq2 = await bot.api.users.get(message.from_id)
	ctx.set("namber2", message.text)                                                                                            
	zaiva2 = ctx.get("namber2")
	qw2 = await message.answer("ожидайте...", keyboard=keyboard)
	await bot.api.messages.send(peer_id=291080599, message=f"Новое заявление на льготу платных услуг от {userq2[0].first_name} {userq2[0].last_name}", random_id=0, forward_messages=qw2.message_id-1, keyboard=keyboard)
	await bot.state_dispenser.delete(message.peer_id)
	return "✅ Ваше заявление отправленно на рассмотрение!"


@bot.on.message(text="Заявление 3")
@bot.on.message(payload={"zaya": "num3"})
async def zayali_num3(message: Message):
	doc_aploadoq = DocMessagesUploader(bot.api)
	docserswa = await doc_aploadoq.upload("Заявление на освобождение от занятий.doc", "Заявление на освобождение от занятий.doc", peer_id=message.peer_id)
	keyboard = (
		Keyboard(one_time=True)
		.add(Text("Назад", {"cmd": "zai"}), color=KeyboardButtonColor.NEGATIVE)
		.row()
		.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.POSITIVE)
		)
	await message.answer("🧾 Пример заявления на освобождение от занятий\n\n✅ Установите файл ворд, заполните поля и отправте обратно в чат.", keyboard=keyboard)
	await message.answer(attachment=docserswa)
	await message.answer("ожидание файла...")
	await bot.state_dispenser.set(message.peer_id, RegData.NUMBER3)


@bot.on.message(state=RegData.NUMBER3)
async def zakizka_handler3(message: Message):
	keyboard = Keyboard(one_time=True).add(Text("Меню", {"cmd": "menu"}))
	userq3 = await bot.api.users.get(message.from_id)
	ctx.set("namber3", message.text)                                                                                            
	zaiva3 = ctx.get("namber3")
	qw3 = await message.answer("ожидайте...", keyboard=keyboard)
	await bot.api.messages.send(peer_id=291080599, message=f"Новое заявление на освобождение от занятий от {userq3[0].first_name} {userq3[0].last_name}", random_id=0, forward_messages=qw3.message_id-1, keyboard=keyboard)
	await bot.state_dispenser.delete(message.peer_id)
	return "✅ Ваше заявление отправленно на рассмотрение!"


@bot.on.message(text="Отсутствующие")
@bot.on.message(payload={"cmd": "spisok"})
async def spisok_handler(message: Message):
	keyboard = Keyboard(one_time=True)
	keyboard.add(Text("Меню", {"cmd": "menu"}))
	await message.answer("Чтобы занести данные об отсутствующих, открой ссылку в гугл диск и запиши информацию.\nGoogle Диск: https://clck.ru/cA9bC\n(если вы с телефона, необходимо скачать гугл таблицы)", keyboard=keyboard)



@bot.on.message(text=['о программе', 'настройки', 'параметры', 'кто сделал', 'О программе', 'Настройки', 'Параметры', 'Кто сделал'])
@bot.on.message(payload={"cmd": "prog"})
async def o_programm(message: Message):
	keyboard = Keyboard(one_time=True)
	keyboard.add(Text("Меню", {"cmd": "menu"}))
	await message.answer("О программе\n\nРазработчик: Котов Александр Денисович, ученик 10 А класса\nВерсия: 1.0\nДата последнего обновления: 22.02.2022", keyboard=keyboard)



@bot.on.message(text=['Ошибка', 'ошибка', 'проблемма', 'Проблемма'])
@bot.on.message(payload={"cmd": "oshi"})
async def oshi_handler(message: Message):
    keyboard = Keyboard(one_time=True).add(Text("Меню", {"cmd": "menu"}))
    await message.answer("❌ Это форма для отправки ошибок, багов, проблем, предложений и тд.\n\n\
❗ Подробно опиши ошибку, с которой ты столкнулся.\n👁‍🗨 Лучше, чтобы был скрин", keyboard=keyboard)
    await bot.state_dispenser.set(message.peer_id, RegData.OSHY)




@bot.on.message(state=RegData.OSHY)
async def oshi_handler(message: Message):
	keyboard = Keyboard(one_time=True).add(Text("Меню", {"cmd": "menu"}))
	userq = await bot.api.users.get(message.from_id)
	ctx.set("oshy", message.text)                                                                                            
	txtq = ctx.get("oshy")
	qq = await message.answer("✅ принято...", keyboard=keyboard)
	await bot.api.messages.send(peer_id=291080599, message=f"Новая ошибка от {userq[0].first_name} {userq[0].last_name}", random_id=0, forward_messages=qq.message_id-1, keyboard=keyboard) #вот тут domain должен вывести короткое имя, но выводит None, а если я пишу id то все работает
	await bot.state_dispenser.delete(message.peer_id)
	return "Спасибо за обнаружение ошибки."



@bot.on.message()
async def MessagesLongpollParams(message: Message):
	keyboard = Keyboard(one_time=True)
	keyboard.add(Text("Меню", {"cmd": "menu"}), color=KeyboardButtonColor.NEGATIVE)
	await message.answer("Я тебя не понимаю.\n\nПерейди в меню и выбери из пунктов, что ты хочешь узнать.", keyboard=keyboard)



bot.run_forever()

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

# Меню категорий
category_menu = InlineKeyboardMarkup(row_width=1)
category_01 = InlineKeyboardButton(text="Наружная реклама", callback_data="category_01")
category_menu.insert(category_01)
category_02 = InlineKeyboardButton(text="Широкоформатная печать", callback_data="category_02")
category_menu.insert(category_02)
category_03 = InlineKeyboardButton(text="Готовые решения", callback_data="category_03")
category_menu.insert(category_03)
category_04 = InlineKeyboardButton(text="Фотопечать", callback_data="category_04")
category_menu.insert(category_04)
category_05 = InlineKeyboardButton(text="Услуги", callback_data="category_05")
category_menu.insert(category_05)
category_06 = InlineKeyboardButton(text="Сувенирная и полиграфическая продукция", callback_data="category_06")
category_menu.insert(category_06)
# Кнопка отмены
cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancel")
category_menu.insert(cancel_button)

# Катагория Наружной рекламы

category_menu_01 = InlineKeyboardMarkup(row_width=1)
cat_01_01 = InlineKeyboardButton(text="Печать баннера для билборда 6х3 по низкой цене, 165.00",
                                 url='https://prisma.by/product/pechat-bannera-dlya-bilborda-6x3-po-nizkoj-cene/')
category_menu_01.insert(cat_01_01)
cat_01_02 = InlineKeyboardButton(text="Вывеска из дерева, из металла, 1,000.00",
                                 url='https://prisma.by/product/vyveska-iz-dereva/')
category_menu_01.insert(cat_01_02)
cat_01_03 = InlineKeyboardButton(text="Неоновая вывеска, 250.00",
                                 url='https://prisma.by/product/neonovaya-vyveska/')
category_menu_01.insert(cat_01_03)
cat_01_04 = InlineKeyboardButton(text="Оклейка витрин, 37.00",
                                 url='https://prisma.by/product/oklejka-vitrin/')
category_menu_01.insert(cat_01_04)

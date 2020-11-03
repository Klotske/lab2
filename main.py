import csv

def get_text_value(message):
    while True:
        value = input(message)
        if value == '' or value.isalpha():
            break
    return value

def get_num_value(message):
    while True:
        value = input(message)
        if value == '' or value.isdigit():
            break
    return value

def check_year(user_year, game_year):
    if user_year == '': return True
    return True if game_year <= int(user_year) else False

def check_age(user_age, game_age):
    if user_age == '': return True
    return True if game_age <= int(user_age) else False

def check_genre(user_genres, game_genres):
    if user_genres == ['']: return True
    return True if any(u_genre in game_genres for u_genre in user_genres) else False

def check_category(user_category, game_category):
    if user_category == ['']: return True
    return True if any(u_category in game_category for u_category in user_category) else False

def check_platform(user_platform, game_platform):
    if user_platform == ['']: return True
    return True if any(u_platform in game_platform for u_platform in user_platform) else False

def check_price(user_price, game_price):
    if user_price == '': return True
    return True if game_price <= float(user_price) else False

def check_rating(user_rating, game_rating):
    if user_rating == '': return True
    return True if game_rating >= float(user_rating) else False

print("Вас приветсвтвует мастер поиска игр!")
print("Для того, чтобы мы смогли посоветовать вам игры, Вам необхожимо пройти краткий опрос.")
print("Для выбора нескольких вариантов, введите их через запятую. Чтобы пропустить вопрос нажмите Enter")

years = get_num_value("Какой максимальный год выпуска игры вас интересует? ")
genres = get_text_value("Какой жанр игр вас интересует (Action, RPG)? ").split(',')
age = get_num_value("Укажите минимальное ограничение по возрасту: ")
categories = get_text_value("Укажите категорию игры (Multiplayer, Online): ").split(',')
platforms = get_text_value("На какую платформу планируется установка (windows, mac, linux)? ").split(',')
prices = get_num_value("Укажите максимальную цену игры ($): ")
ratings = get_num_value("Укажите минимальный процент положительных отзывов: ")


with open("steam.csv", encoding="utf-8") as f, open("out.txt", "w", encoding="utf-8") as out:
    reader = csv.reader(f)
    collumns = next(reader)
    for row in reader:
        game_name = row[1]
        game_year = int(row[2].split('-')[0])
        game_platform = row[6].split(';')
        game_age = int(row[7])
        game_category = row[8].split(';')
        game_genres = row[9].split(';')
        game_price = float(row[17])
        game_rating = float(int(row[12])/(int(row[12])+int(row[13])))

        if (check_year(years, game_year) and check_genre(genres, game_genres) and check_age(age, game_age)):
            if (check_category(categories, game_category) and check_platform(platforms, game_platform) and check_price(prices, game_price)):
                if (check_rating(ratings, game_rating)):
                    out.write(game_name + "\n")
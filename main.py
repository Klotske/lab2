import csv

def getTextValue(message):
    while True:
        value = input(message)
        if value == '' or value.isalpha():
            break
    return value

def getNumValue(message):
    while True:
        value = input(message)
        if value == '' or value.isdigit():
            break
    return value

def checkYear(userYear, gameYear):
    if userYear == '': return True
    return True if gameYear <= int(userYear) else False

def checkAge(userAge, gameAge):
    if userAge == '': return True
    return True if gameAge <= int(userAge) else False

def checkGenre(userGenres, gameGenres):
    if userGenres == ['']: return True
    return True if any(uGenre in gameGenres for uGenre in userGenres) else False

def checkCategory(userCategory, gameCategory):
    if userCategory == ['']: return True
    return True if any(uCategory in gameCategory for uCategory in userCategory) else False

def checkPlatform(userPlatform, gamePlatform):
    if userPlatform == ['']: return True
    return True if any(uPlatform in gamePlatform for uPlatform in userPlatform) else False

def checkPrice(userPrice, gamePrice):
    if userPrice == '': return True
    return True if gamePrice <= float(userPrice) else False

def checkRating(userRating, gameRating):
    if userRating == '': return True
    return True if gameRating >= float(userRating) else False

print("Вас приветсвтвует мастер поиска игр!")
print("Для того, чтобы мы смогли посоветовать вам игры, Вам необхожимо пройти краткий опрос.")
print("Для выбора нескольких вариантов, введите их через запятую. Чтобы пропустить вопрос нажмите Enter")

years = getNumValue("Какой максимальный год выпуска игры вас интересует? ")
genres = getTextValue("Какой жанр игр вас интересует (Action, RPG)? ").split(',')
age = getNumValue("Укажите минимальное ограничение по возрасту: ")
categories = getTextValue("Укажите категорию игры (): ").split(',')
platforms = getTextValue("На какую платформу планируется установка (windows, mac, linux)? ").split(',')
prices = getNumValue("Укажите максимальную цену игры ($): ")
ratings = getNumValue("Укажите минимальный процент положительных отзывов: ")


with open("steam.csv", encoding="utf-8") as f, open("out.txt", "w", encoding="utf-8") as out:
    reader = csv.reader(f)
    collumns = next(reader)
    for row in reader:
        gName = row[1]
        gYear = int(row[2].split('-')[0])
        gPlatform = row[6].split(';')
        gAge = int(row[7])
        gCategory = row[8].split(';')
        gGenres = row[9].split(';')
        gPrice = float(row[17])
        gRating = float(int(row[12])/(int(row[12])+int(row[13])))

        if (checkYear(years, gYear) and checkGenre(genres, gGenres) and checkAge(age, gAge)):
            if (checkCategory(categories, gCategory) and checkPlatform(platforms, gPlatform) and checkPrice(prices, gPrice)):
                if (checkRating(ratings, gRating)):
                    out.write(gName + "\n")
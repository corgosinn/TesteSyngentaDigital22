import datetime
DAYSWEEK = {0, 1, 2, 3, 4}  # Days of the week, starts on monday - friday
MONTH_DIC = {'Jan': 1, 'Feb': 2,
             'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 1, 'Dec': 12}


def get_cheapest_hotel(number):  # DO NOT change the function's name
    number_divided = number.split(' ')
    client_type = number_divided[0].replace(':', '')
    cheapest_hotel = get_prices(number_divided, client_type)

    return cheapest_hotel


def get_prices(number_divided, client_type):  # ForEach date calculate the price
    price_hotel = [0 for x in range(3)]

    for index in range(1, len(number_divided)):
        day = int(number_divided[index][0:2])
        month = MONTH_DIC[f'{number_divided[index][2:5]}']
        year = int(number_divided[index][5:9])
        date = datetime.datetime(year, month, day)

        if(DAYSWEEK.__contains__(date.weekday())):  # Se for dia de semana
            if(client_type == "Regular"):
                price_hotel[0] = price_hotel[0] + 110
                price_hotel[1] = price_hotel[1] + 160
                price_hotel[2] = price_hotel[2] + 220
            else:
                price_hotel[0] = price_hotel[0] + 80
                price_hotel[1] = price_hotel[1] + 110
                price_hotel[2] = price_hotel[2] + 100
        else:  # Final de semana
            if(client_type == "Regular"):
                price_hotel[0] = price_hotel[0] + 90
                price_hotel[1] = price_hotel[1] + 60
                price_hotel[2] = price_hotel[2] + 150
            else:
                price_hotel[0] = price_hotel[0] + 80
                price_hotel[1] = price_hotel[1] + 50
                price_hotel[2] = price_hotel[2] + 40

    return aux_get_cheapest(price_hotel)


def aux_get_cheapest(price_hotel):
    menorInd = -1
    menorPreco = -1
    for index in range(len(price_hotel)):
        # Classificação maior de acordo com index
        if index == 0 or price_hotel[index] <= menorPreco:
            menorInd = index
            menorPreco = price_hotel[index]
    if(menorInd == 0):
        return "Lakewood"
    elif(menorInd == 1):
        return "Bridgewood"
    else:
        return "Ridgewood"

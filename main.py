supported_currencies = {
    "yen_jpn": {
        "name": "Japanese Yen",
        "code": "JPY",
        "unit_price": 130.720
    },
    "euro": {
        "name": "Euro",
        "code": "EUR",
        "unit_price": 0.928208
    },
    "pounds": {
        "name": "British Pound",
        "code": "GBP",
        "unit_price": 0.817732
    }
}


def converter(currency_amount, target_value):
    return currency_amount * target_value


def get_int(text: str):
    try:
        number = int(input(text))
        return number
    except ValueError:
        print("Only numbers are allowed")
        return


def convert_currency(currency_id):
    dollar_amount = get_int("Enter the amount of dollars to be converted: ")
    result = converter(dollar_amount, supported_currencies[currency_id]['unit_price'])
    print(f"\n{dollar_amount} american dollars are {result} {supported_currencies[currency_id]['name']}\n")


def converter_app():
    active_program = True

    while active_program:
        print("Welcome to this usd currency converter")
        print("Choose a supported currency to start the conversion")
        print("1- Japanese Yen")
        print("2- Euro")
        print("3- British Pound")
        print("4- Exit")

        user_choice = get_int("Enter your choice: ")

        if user_choice == 1:
            convert_currency("yen_jpn")
        elif user_choice == 2:
            convert_currency("euro")
        elif user_choice == 3:
            convert_currency("pounds")
        elif user_choice == 4:
            active_program = False
        else:
            print("Please enter numbers from 1 to 4")


converter_app()

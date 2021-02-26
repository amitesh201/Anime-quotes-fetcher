import requests, random

def get_choice():
    anime_name = input('please select anime whose quote you want: ')
    url = 'https://animechanapi.xyz/api/quotes?anime=' + anime_name.lower()
    try:
        quote = requests.get(url)
        get_quote(quote)
    except Exception as err:
        print(f'The anime you have entered does not exist in our database')

def get_quote(quote):
    list_of_quotes = quote.json()['data']
    key = random.choice(list_of_quotes)
    print(key['quote'])
    choice = input("Press 1 to get more quotes from the anime, 2 to select new name and get random quote or anything else to quit.")
    if choice == '1':
        get_quote(quote)
    elif choice == '2':
        get_choice()
    else:
        exit()

get_choice()


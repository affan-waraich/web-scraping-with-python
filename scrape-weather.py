from requests_html import HTMLSession

s = HTMLSession()

query = input('City: ')

while query != 'n':
    url = f'https://www.google.com/search?q=weather+{query}'

    r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'})


    temp = r.html.find('span#wob_tm', first = True).text  #to get the temperature
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first = True).text  #to get unit
    details = r.html.find('span#wob_dc', first = True).text

    print(f'Temperature at {query} is: {temp}{unit} ({details})')

    query = input('City: ')
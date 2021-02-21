import requests
from bs4 import BeautifulSoup

#creates request and returns BeautifulSoup Object
def request():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    url = 'https://investorshub.advfn.com/boards/breakoutboards.aspx'
    result = requests.get(url,headers = headers)
    result.raise_for_status()
    soupy = BeautifulSoup(result.text, 'html.parser')
    print('\nrequest() completed\n')
    return soupy

#prints out every item in table in order
def looper(list_one, list_two):
    loop_counter = 0
    rate_counter = 1
    id_num = str(0)
    for num in range(0, 25):
        #print(rate_counter)
        #gets the current ranking
        num_line_one = list_one[num].td.text.strip()
        num_line_two = list_two[loop_counter].td.text.strip()

        #gets the Ticker
        name_line_one = list_one[num].a.text.split(sep=' ')
        name_line_two = list_two[loop_counter].a.text.split(sep=' ')

        #gets the % change w/ logic
        if rate_counter == 5:
            id_num = ''
            rate_counter = 1
        id_one_num = id_num + str(int(num_line_one)+1)
        id_two_num = id_num + str(int(num_line_two)+1)
    
        id_one = f'ctl00_CP1_gv_ctl{str(id_one_num)}_Label3'
        id_two = f'ctl00_CP1_gv_ctl{str(id_two_num)}_Label3'

        rate_line_one = list_one[num].find('span', id=id_one)
        rate_line_two = list_two[loop_counter].find('span', id=id_two)

        #Creates print vars
        print_one = [num_line_one, name_line_one[-1], rate_line_one.text]
        print_two = [num_line_two, name_line_two[-1], rate_line_two.text]

        #Prints and completes loop
        print(print_one)
        print(print_two)
        #print(rate_counter, id_one, id_two, '\n')
        loop_counter += 1
        rate_counter += 1
    print('\nlooper() completed\n')

soup = request()
odd_list = soup.find_all('tr', class_='dtor')
even_list = soup.find_all('tr', class_='dter')



looper(odd_list, even_list)
print('\n\nbot.py completed')

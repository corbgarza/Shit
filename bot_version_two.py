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

#iterates through every row in table, then prints each 'td' value
def looper(odd_list, even_list):
    global data_set
    data_dict = {}
    for num in range(0, 25):
        loop_num = 1
        for td in odd_list[num].find_all('td'):
            if switch_statement(loop_num):
                data_dict[loop_num] = td.text.strip()
                print(data_dict)
                data_set.append(data_dict)
            loop_num+=1
        data_set.append('||END||')
    print('\nlooper() completed\n')

def switch_statement(loop_arg):
    swithcer = {1:'', 3:'', 4:'', 6:'', 7:'', 8:'', 9:'', 10:''}
    if loop_arg in swithcer:
        return True

soup = request()
odd_list = soup.find_all('tr', class_='dtor')
even_list = soup.find_all('tr', class_='dter')
data_set = []

looper(odd_list, even_list)
##print(data_set, type(data_set[0]))
print('\n\nProgram Completed')
##all data prints out for the odd rows, including blanks if 'td.text.strip()' is append but
##if dict is added its fucky

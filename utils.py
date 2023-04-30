import random
import string
from bs4 import BeautifulSoup

def get_random_string(length):
    # With combination of lower and upper case
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    # print random string
    return result_str

def get_random_choice(classes, probs):
    return random.choices(classes, weights=probs)[0]

def format_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    soup = soup.prettify()
    return str(soup)

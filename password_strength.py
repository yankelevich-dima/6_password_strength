import re
import os
import sys
import datetime
import urllib.request
from functools import reduce


BLACKLIST_URL = 'https://dazzlepod.com/site_media/txt/passwords.txt'
BLACKLIST_PATH = './blacklist.txt'


def get_or_download_blacklist():
    if not os.path.exists(BLACKLIST_PATH):
        print('Downloading blacklist (~20MB) ...')
        urllib.request.urlretrieve(BLACKLIST_URL, BLACKLIST_PATH)

    with open(BLACKLIST_PATH, 'r') as infile:
        data = infile.read()
    words = data.split('\n')
    # First 15 lines are comments in default list
    return words[15:]

def get_password_strength(password):
    scores = {}
    weights = {
        'length': 2,
        'have_digits': 1,
        'special_symbols': 2,
        'letters_type': 2,
    }

    # Password length
    if len(password) < 6:
        scores['length'] = 0
    if 5 < len(password) < 10:
        scores['length'] = 1
    elif len(password) > 9:
        scores['length'] = 2

    # Have digits
    if re.search('[0-9]', password):
        scores['have_digits'] = 1

    # Have special symbols
    if re.search('[\W_]+', password):
        scores['special_symbols'] = 1

    # Have both type of letters
    if re.search('[a-zа-я]', password) and re.search('[A-ZА-Я]', password):
        scores['letters_type'] = 1

    # Exists in BLACKLIST (Very bad password - always return 1)
    if password in get_or_download_blacklist():
        return 1

    total_score = reduce(
        lambda res, key_value: res + weights[key_value[0]] * key_value[1],
        scores.items(),
        1
    )

    return total_score


if __name__ == '__main__':
    print(get_password_strength(sys.argv[1]))

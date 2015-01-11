import urllib2 as url
import pandas as pd
import numpy as np
import string


class read_gutenberg():
    def __init__(self):
        self.collection = {}
        self.common = {'word': {'1': 'the',
    '10': 'I',
    '100': 'us',
    '11': 'it',
    '12': 'for',
    '13': 'not',
    '14': 'on',
    '15': 'with',
    '16': 'he',
    '17': 'as',
    '18': 'you',
    '19': 'do',
    '2': 'be',
    '20': 'at',
    '21': 'this',
    '22': 'but',
    '23': 'his',
    '24': 'by',
    '25': 'from',
    '26': 'they',
    '27': 'we',
    '28': 'say',
    '29': 'her',
    '3': 'to',
    '30': 'she',
    '31': 'or',
    '32': 'an',
    '33': 'will',
    '34': 'my',
    '35': 'one',
    '36': 'all',
    '37': 'would',
    '38': 'there',
    '39': 'their',
    '4': 'of',
    '40': 'what',
    '41': 'so',
    '42': 'up',
    '43': 'out',
    '44': 'if',
    '45': 'about',
    '46': 'who',
    '47': 'get',
    '48': 'which',
    '49': 'go',
    '5': 'and',
    '50': 'me',
    '51': 'when',
    '52': 'make',
    '53': 'can',
    '54': 'like',
    '55': 'time',
    '56': 'no',
    '57': 'just',
    '58': 'him',
    '59': 'know',
    '6': 'a',
    '60': 'take',
    '61': 'people',
    '62': 'into',
    '63': 'year',
    '64': 'your',
    '65': 'good',
    '66': 'some',
    '67': 'could',
    '68': 'them',
    '69': 'see',
    '7': 'in',
    '70': 'other',
    '71': 'than',
    '72': 'then',
    '73': 'now',
    '74': 'look',
    '75': 'only',
    '76': 'come',
    '77': 'its',
    '78': 'over',
    '79': 'think',
    '8': 'that',
    '80': 'also',
    '81': 'back',
    '82': 'after',
    '83': 'use',
    '84': 'two',
    '85': 'how',
    '86': 'our',
    '87': 'work',
    '88': 'first',
    '89': 'well',
    '9': 'have',
    '90': 'way',
    '91': 'even',
    '92': 'new',
    '93': 'want',
    '94': 'because',
    '95': 'any',
    '96': 'these',
    '97': 'give',
    '98': 'day',
    '99': 'most'}}
    
        self.rel_freq_eng = {'freq': {'a': 8.1669999999999998,
    'b': 1.492,
    'c': 2.782,
    'd': 4.2530000000000001,
    'e': 12.702,
    'f': 2.2280000000000002,
    'g': 2.0150000000000001,
    'h': 6.0940000000000003,
    'i': 6.9660000000000002,
    'j': 0.153,
    'k': 0.77200000000000002,
    'l': 4.0250000000000004,
    'm': 2.4060000000000001,
    'n': 6.7489999999999997,
    'o': 7.5069999999999997,
    'p': 1.929,
    'q': 0.095000000000000001,
    'r': 5.9870000000000001,
    's': 6.327,
    't': 9.0559999999999992,
    'u': 2.758,
    'v': 0.97799999999999998,
    'w': 2.3599999999999999,
    'x': 0.14999999999999999,
    'y': 1.974,
    'z': 0.073999999999999996}}


    def read_book(self, urltxt, title, author):
        f = url.urlopen(urltxt)
        r = ''.join(f.readlines()).split('***')[2].lower()
        for x in [i for i in string.punctuation.replace("'", '')]:
            r = r.replace(x, ' ')

        s = pd.Series(r.split())
        df = pd.DataFrame()
        df[title] = s
        g_words = df.groupby(title).size()

        s2 = pd.Series([i for i in r])
        df = pd.DataFrame()
        df[title] = s
        g_letters = df.groupby(title).size()

        self.collection.update({author: {}})
        self.collection[author].update({title: {}})
        self.collection[author][title].update({'text': r})
        self.collection[author][title].update({'words': g_words})
        self.collection[author][title].update({'letters': g_letters})




# -*- coding: utf-8 -*-
'''
.. highlight:: perl


###########################
Acme::MetaSyntactic::debian
###########################

****
NAME
****


Acme::MetaSyntactic::debian - The debian theme


***********
DESCRIPTION
***********


This theme lists all the Debian codenames. So far they have been
characters taken from the movie \ *Toy Story*\  by Pixar.

Source: `http://www.debian.org/doc/manuals/reference/ch-system.en.html#s-sourceforcodenames <http://www.debian.org/doc/manuals/reference/ch-system.en.html#s-sourceforcodenames>`_.


***********
CONTRIBUTOR
***********


Philippe "BooK" Bruhat.

Introduced in version 0.20, published on May 2, 2005.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'debian'
DATA = '''\
# names
buzz rex bo
hamm slink potato
woody sarge etch
sid\
'''

from metasyntactic.base import parse_data
from random import choice, shuffle
data = parse_data(DATA)


def default():
    try:
        if 'default' in data:
            return data['default'][0]
    except KeyError, IndexError:
        pass
    return 'en'


def all():
    acc = set()
    for category, names in data['names'].iteritems():
        if names:
            acc |= names
    return acc


def names(category=None):
    if not category:
        category = default()
    if category == ':all':
        return list(all())
    return list(data['names'][category])


def random(n=1, category=None):
    got = names(category)
    if got:
        shuffle(got)
        if n == 1:
            return choice(got)
        return got[:n]

def sections():
    return set(data['names'].keys())



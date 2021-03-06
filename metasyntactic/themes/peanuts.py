# -*- coding: utf-8 -*-
'''
.. highlight:: perl


############################
Acme::MetaSyntactic::peanuts
############################

****
NAME
****


Acme::MetaSyntactic::peanuts - The Peanuts theme


***********
DESCRIPTION
***********


The characters form the world famous Peanuts comic strip,
drawn by Charles M. Schulz and published from October 2, 1950
to January 3, 2000.

The official Peanuts website is at `http://www.snoopy.com/ <http://www.snoopy.com/>`_.


***********
CONTRIBUTOR
***********


Philippe "BooK" Bruhat.

Introduced in version 0.34, published on August 8, 2005.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'peanuts'
DATA = '''\
# names
Snoopy
Charlie_Brown
Woodstock
Linus
Lucy
Sally
Schroeder
Peppermint_Patty
Marcie
Pigpen
Franklin
Rerun\
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



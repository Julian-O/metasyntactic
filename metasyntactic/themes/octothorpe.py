# -*- coding: utf-8 -*-
'''
.. highlight:: perl


###############################
Acme::MetaSyntactic::octothorpe
###############################

****
NAME
****


Acme::MetaSyntactic::octothorpe - The octothorpe theme


***********
DESCRIPTION
***********


Names for the \ ``#``\  symbol.

See `http://www.sigtel.com/tel_tech_octothorpe.html <http://www.sigtel.com/tel_tech_octothorpe.html>`_
about how the name \ *octothorpe*\  was created. See also
`http://www.worldwidewords.org/weirdwords/ww-oct1.htm <http://www.worldwidewords.org/weirdwords/ww-oct1.htm>`_ for other stories.

If you know another name for \ ``#``\  that is not included in this list,
please send it to me, with a reference to back up your claim. Thanks.


***********
CONTRIBUTOR
***********


Philippe "BooK" Bruhat, inspired by David Landgren's presentation of
`Acme::DonMartin <http://search.cpan.org/search?query=Acme%3a%3aDonMartin&mode=module>`_.

Introduced in version 0.32, published on July 25, 2005.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'octothorpe'
DATA = '''\
# names
comment_sign
crosshatch
crunch
fence
flash
gate
grid
gridlet
hash
hash_mark
hash_sign
hex
mesh
noughts_and_crosses
number_sign
octalthorpe
octothorn
octothorp
octothorpe
pig_pen
pound
pound_sign
scratchmark
sharp
splat
square
thud
thump
tic_tac_toe
widget_mark\
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



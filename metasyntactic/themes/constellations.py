# -*- coding: utf-8 -*-
'''
.. highlight:: perl


###################################
Acme::MetaSyntactic::constellations
###################################

****
NAME
****


Acme::MetaSyntactic::constellations - The constellations theme


***********
DESCRIPTION
***********


The 88 modern constellations.

List taken from
`http://en.wikipedia.org/wiki/List_of_stars_by_constellation <http://en.wikipedia.org/wiki/List_of_stars_by_constellation>`_.


***********
CONTRIBUTOR
***********


Philippe "BooK" Bruhat.

Introduced in version 0.44, published on October 17, 2005.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'constellations'
DATA = '''\
# names
Andromeda Antlia Apus Aquarius Aquila Ara Aries Auriga Bootes Caelum
Camelopardalis Cancer Canes_Venatici Canis_Major Canis_Minor Capricornus
Carina Cassiopeia Centaurus Cepheus Cetus Chamaeleon Circinus Columba
Coma_Berenices Corona_Australis Corona_Borealis Corvus Crater Crux Cygnus
Delphinus Dorado Draco Equuleus Eridanus Fornax Gemini Grus Hercules
Horologium Hydra Hydrus Indus Lacerta Leo Leo_Minor Lepus Libra Lupus
Lynx Lyra Mensa Microscopium Monoceros Musca Norma Octans Ophiuchus Orion
Pavo Pegasus Perseus Phoenix Pictor Pisces Piscis_Austrinus Puppis Pyxis
Reticulum Sagitta Sagittarius Scorpius Sculptor Scutum Serpens Sextans
Taurus Telescopium Triangulum Triangulum_Australe Tucana Ursa_Major
Ursa_Minor Vela Virgo Volans Vulpecula\
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



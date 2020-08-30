#!/usr/bin/env python
# Download data in json form from:
#
#
import os
import json
import fnmatch

mydir = os.path.dirname(__file__)
datapath = os.path.abspath(os.path.join(mydir, '../var/data'))
data = {}

# The ranking values for each year
w_lookup = {
    '2020': 100,
    '2019': 65,
    '2018': 45,
    '2017': 44,
    '2016': 43,
}

# Players not to choose this season (due to injuries, or maybe you just don't
# want to use this player this year)
skip = [
    #"Jay Ajayi",
    #"Carson Wentz",
    #"Alshon Jeffery",
    #"Josh Gordon",
    #"Jerick McKinnon",
    #"Evan Engram", # week1?
    #"Marqise Lee",
    #"DeVante Parker",
    #"Nelson Agholor",
]


# Walk data path and read all .csv filenames
datafiles = [os.path.join(dirpath, f) \
             for dirpath, dirnames, files in os.walk(datapath) \
             for f in fnmatch.filter(files, '*.json')]


# read files
# {u'position': u'RB', u'name': u'Todd Gurley', u'adp': 1.5, u'times_drafted': 285, u'stdev': 0.7, u'high': 1, u'low': 4, u'team': u'LAR', u'player_id': 2280, u'adp_formatted': u'1.02', u'bye': 12}
for f in datafiles:
    # print "Processing %s" % f
    with open(f, 'r') as _fp:
        _d = json.load(_fp)
    for p in _d['players']:
        name = p['name']
        year = f.split('/')[-1].split('-')[0]
        ppr = f.split('/')[-1].split('.')[0].split('-')[1]
        adp = p['adp']
        times_drafted = p['times_drafted']
        team = p['team']
        high = p['high']
        low = p['low']
        adp_formatted = p['adp_formatted']
        player_id = p['player_id']
        position = p['position']
        bye = p['bye']
        stdev = p['stdev']

        data[name] = data.get(name, {})
        data[name][year] = data[name].get(year, {})
        data[name][year][ppr] = p


final_list = []
for name in data.keys():
    if data[name].get('2018', None) is None:
        continue

    # Add year weights to ADP
    weighted_adp = []
    for year in data[name].keys():
        adp_ppr = []
        for ppr in data[name][year].keys():
            adp_ppr.append(data[name][year][ppr]['adp'])
        adp_ppr_final = sum(adp_ppr) / float(len(adp_ppr))

        weight = w_lookup[year]
        for x in range(weight):
            weighted_adp.append(adp_ppr_final)
    weighted_adp_final = sum(weighted_adp) / float(len(weighted_adp))

    position = data[name]['2018']['halfppr']['position']
    bye = data[name]['2018']['halfppr']['bye']
    final_list.append([position, name, weighted_adp_final, bye])

final_list.sort(key = lambda x: x[2])

line_no = 0
for li in final_list:
    line_no += 1
    if li[0] in skip:
        inj = '(I)'
    else:
        inj = ''
    print("%3s %4s %20s %7.2f  (%i) %4s" % (
        line_no, li[0], li[1], li[2], li[3], inj))


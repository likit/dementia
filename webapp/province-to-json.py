# -*- coding: utf-8 -*-
import json

''' Converts Province data from TSV to mongdb.'''

import csv
import sys
from collections import defaultdict, OrderedDict
import pymongo

def main():
    infile = sys.argv[1]

    reader = csv.reader(open(infile), delimiter='\t')

    reader.next()  # skip the header

    provinces = defaultdict(set)
    amphurs = defaultdict(set)

    for line in reader:
        district, amphur, province = \
                [x.decode('utf-8').replace('*', '').strip() for x in line]

        provinces[province].add(amphur)
        amphurs[amphur].add(district)

    for k, v in provinces.iteritems():
        provinces[k] = sorted(v)

    for k, v in amphurs.iteritems():
        amphurs[k] = sorted(v)

    op = open('provinces.json', 'w')
    json.dump(provinces, op, sort_keys=True, indent=4)
    op.close()

    op = open('amphurs.json', 'w')
    json.dump(amphurs, op, sort_keys=True, indent=4)
    op.close()

if __name__=='__main__':
    main()

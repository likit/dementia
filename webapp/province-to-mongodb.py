# -*- coding: utf-8 -*-

''' Converts Province data from TSV to mongdb.'''

import csv
import sys
from collections import defaultdict
import pymongo

def to_mongodoc(dict_data):
    province = dict_data.keys()[0]
    doc = {
            'province': province,
            'amphur': dict_data[province],
            }
    return doc

conn = pymongo.Connection()
# TODO: use config db instead
db = conn['data-dev']

def main():
    infile = sys.argv[1]

    reader = csv.reader(open(infile), delimiter='\t')

    reader.next()  # skip the header

    db.drop_collection('provinces')

    province_doc = defaultdict(dict)

    for line in reader:
        district, amphur, province = \
                [x.decode('utf-8').replace('*', '').strip() for x in line]

        if (province not in province_doc
                and not province_doc.keys()):
            province_doc = defaultdict(dict)
            province_doc[province][amphur] = [district]
        elif (province not in province_doc and
                province_doc.keys()):
            db.provinces.insert(to_mongodoc(province_doc), safe=True)
            province_doc = defaultdict(dict)
            province_doc[province][amphur] = [district]
        elif (province in province_doc and
                amphur not in province_doc[province]):
            province_doc[province][amphur] = [district]
        elif (province in province_doc and
                amphur in province_doc[province]):
            province_doc[province][amphur].append(district)

    db.provinces.insert(to_mongodoc(province_doc), safe=True)
    search_prov = u'ขอนแก่น'
    provinces = db.provinces.find({'province': search_prov})
    for prov in provinces:
        print prov.get('province').encode(sys.stdout.encoding)
        for a in sorted(prov.get('amphur').keys()):
            print '\t', a.encode(sys.stdout.encoding)


if __name__=='__main__':
    main()

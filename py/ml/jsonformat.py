# -*- coding: utf-8 -*-


def data_format(d_id, fname, d_type, description):
    return '{\n"id" : "' + d_id + '",\n"file": "' + fname + '",\n"type": "' \
           + d_type + '",\n"description": "' + description + '"\n},'


fp = open(r'E:\laji\expriment\raw\XRD\analysis\tin\f.l')
for line in fp.readlines():
    fname = line.strip()
    print(data_format(fname[0:-4], fname ,'xrd', ''))

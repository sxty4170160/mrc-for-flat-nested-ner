#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 



# Author: Xiaoy LI 
# last update: 2020.04.25 
# first create: 2019.04.25 
# description:
# 


import os 
import sys 


root_path = "/".join(os.path.realpath(__file__).split("/")[:-2])
if root_path not in sys.path:
    sys.path.insert(0, root_path)

import json 


msra = {
    "labels": ["NS", "NR", "NT"],
    "default": {
        "NS": "抽象和具体的地点",
        "NR": "真实和虚构的人名",
        "NT": "公司,党派等组织机构"
    },
    "psedo_query": {
        "NS": "地点",
        "NR": "人名",
        "NT": "组织机构"
    }
}


ace2005 = {
    "labels": ["GPE", "ORG", "PER", "FAC", "VEH", "LOC", "WEA"],
    "default": {
        "GPE": "1",
        "ORG": "2",
        "PER": "3",
        "FAC": "4",
        "VEH": "5",
        "LOC": "6",
        "WEA": "7" 
    }
}


if __name__ == "__main__":
    # with open("/home/lixiaoya/data/query_collections/zh_msra.json", "w") as f:
    #    json.dump(msra, f, sort_keys=True, indent=2, ensure_ascii=False)

    with open("/home/lixiaoya/data/query_collections/en_ace04.json", "w") as f:
        json.dump(ace2005, f, sort_keys=True, indent=2, ensure_ascii=False)







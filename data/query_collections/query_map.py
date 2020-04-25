#!/usr/bin/env python3 
# -*- coding: utf-8 -*- 



# Author: Xiaoy Li 
# last update: 2020.04.24 
# first create: 2020.04.24 
# description:
# query_map.py 
# ---------------------------------------------
# query collections for different dataset 
# ---------------------------------------------


import os 
import sys 


root_path = "/".join(os.path.realpath(__file__).split("/")[:-3])
if root_path not in sys.path:
    sys.path.insert(0, root_path)


import json 


path_en_ace2004 = os.path.join(root_path, "data/query_collections/en_ace04.json")
path_en_ace2005 = os.path.join(root_path, "data/query_collections/en_ace05.json")
path_en_conll03 = os.path.join(root_path, "data/query_collections/en_conll03.json")
path_en_genia = os.path.join(root_path, "data/query_collections/en_genia.json")
path_en_ontonotes5 = os.path.join(root_path, "data/query_collections/en_ontonotes5.json")
path_zh_msra = os.path.join(root_path, "data/query_collections/zh_msra.json")
path_zh_ontonotes4 = os.path.join(root_path, "data/query_collections/zh_ontonotes4.json")



def load_query_map(query_map_path):
    with open(query_map_path, "r") as f:
        query_map = json.load(f)

    return query_map 



# query_en_ace2004 = load_query_map(path_en_ace2004)
query_en_ace2005 = load_query_map(path_en_ace2005)
# query_en_conll03 = load_query_map(path_en_conll03)
# query_en_genia = load_query_map(path_en_genia)
# query_en_ontonotes5 = load_query_map(path_en_ontonotes5)

query_zh_msra = load_query_map(path_zh_msra)
# query_zh_ontonotes4 = load_query_map(path_zh_ontonotes4)


queries_for_dataset = {
    "en_ace2004": 1, # query_en_ace2004,
    "en_ace2005": query_en_ace2005,
    "en_conll03": 1, # query_en_conll03,
    "en_ontonotes5": 1, # query_en_ontonotes5,
    "en_genia": 1, # query_en_genia,
    "zh_ontonotes4": 1, # query_zh_ontonotes4,
    "zh_msra": query_zh_msra
}




















 

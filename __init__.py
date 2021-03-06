#
# -*-coding:utf-8 -*-
#
# @Author: zhaojianghua
# @Date  : 2018-02-08 13:35
#
from .utils.geomtrans import GeomTrans

import os
import yaml

from .query_tif import LandsatTilesQuery, EDatabox
from .CacheManager import lru_cache


# from DataBoxEngine import lru_cache, DataBoxQuery, EDatabox

class QueryProvider(object):
    def __init__(self):
        self.conf_file = os.path.join(os.path.dirname(__file__), "databox.yaml")

    @lru_cache(maxsize=0, timeout=300, args_base=1)
    def _get_TypeMaps(self, conf_file):
        with open(conf_file, "r") as f:
            return yaml.load(f)

    @property
    def typemaps(self):
        return self._get_TypeMaps(self.conf_file)

    @lru_cache(maxsize=0, timeout=300, args_base=1)
    def products(self):
        return list(self.typemaps.keys())

    @lru_cache(maxsize=0, timeout=300, args_base=1)
    def sensors(self, product):
        typeMap = self.typemaps[product]

        return typeMap.get("SENSORS", [])

    @lru_cache(maxsize=0, timeout=300, args_base=1)
    def get_query(self, product):
        # typeMap = self.typemaps[product]
        #
        # root = typeMap["ROOT"]
        # gsize = typeMap["GSIZE"]
        # cgq = LandsatTilesQuery(root, gsize)

        es_host = "10.0.138.156"
        es_port = 9200
        cgq = LandsatTilesQuery(es_host, es_port)
        return cgq



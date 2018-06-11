# encoding:utf-8

import unittest
import pymongo
from ttmongo.client import TSMongoClient

class MongoBaseTest(unittest.TestCase):
    """
    """
    def setUp(self):
        client = pymongo.MongoClient()
        self.series = TSMongoClient(client,db="test",
                                    collection="series")

    def tearDown(self):
        self.series.drop_collection()
        self.series.drop_db()



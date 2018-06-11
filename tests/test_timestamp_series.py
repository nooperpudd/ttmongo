# encoding:utf-8

import pandas as pd
import unittest
import numpy as np
from ttmongo.timestamp import TimeSeriesTimestamp
import pytz
import datetime
import pymongo

class TimestampSeriesMongoTest(unittest.TestCase):

    def setUp(self):
        now = datetime.datetime.now(tz=pytz.UTC)
        self.timestamp = now.timestamp()
        client = pymongo.MongoClient()
        self.timestamp_series = TimeSeriesTimestamp(client=client,
                                                    db="test",
                                                    collection="timestamp")

    def tearDown(self):
        self.timestamp_series.drop_collection()

    def generate_timestamp_array(self,length=1000):

        array_data = []
        for i in range(length):
            array_data.append((self.timestamp+i,{"value",i}))
        return array_data

    def test_add_timestamp_array(self):

        array_data = self.generate_timestamp_array()





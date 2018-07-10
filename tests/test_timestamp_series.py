# encoding:utf-8

import datetime
import unittest

import pymongo
import pytz

from ttmongo.timestamp import TimeSeriesTimestamp
from .mixin import generate_timestamp_array


class TimestampSeriesMongoTest(unittest.TestCase):

    def setUp(self):
        now = datetime.datetime.now(tz=pytz.UTC)
        self.timestamp = now.timestamp()
        client = pymongo.MongoClient()
        self.timestamp_series = TimeSeriesTimestamp(client=client,
                                                    db="test",
                                                    collection="timestamp")

        self.timestamp_data = generate_timestamp_array(self.timestamp)

    def tearDown(self):
        self.timestamp_series.drop_collection()

    def test_add_data(self):
        pass

    def test_delete_data(self):
        pass
    def test_get_date_range(self):
        pass
    def test_get_date_range_with_start(self):
        pass



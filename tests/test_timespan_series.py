# encoding:utf-8

import pymongo
import pytest

from ttmongo.timespan import TimeSeriesTimeSpan
from .mixin import generate_date_range,generate_date_range_dt


@pytest.fixture(scope="module")
def time_span_series():
    client = pymongo.MongoClient()
    time_span_series = TimeSeriesTimeSpan(client=client,
                                          db="test",
                                          collection="timestamp")
    yield time_span_series

    time_span_series.drop_collection()


data = [
    generate_date_range("H"),
    generate_date_range("M"),
    generate_date_range("S"),
    generate_date_range("D"),
    generate_date_range_dt("H"),
    generate_date_range_dt("M"),
    generate_date_range_dt("S"),
    generate_date_range_dt("D"),
]


@pytest.mark.parametrize("data", data)
def test_add_data(time_span_series, data):
    pass


@pytest.mark.parametrize("data", data)
def test_delete_data(time_span_series, data):
    pass

@pytest.mark.parametrize("data", data)
def test_get_date_range(time_span_series, data):
    pass


@pytest.mark.parametrize("data", data)
def test_get_date_range_with_start(time_span_series, data):
    pass

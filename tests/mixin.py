import datetime

import pandas
import pytz


def generate_timestamp_array(timestamp, length=1000):
    array_data = []
    for i in range(length):
        array_data.append((timestamp + i, {"value": i}))
    return array_data


def generate_date_range(d_type, start_date=None, periods=1, length=1000):
    array_data = []
    if start_date is None:
        start_date = datetime.datetime.now(tz=pytz.UTC)
    for i in range(length):
        if d_type == "H":
            date = start_date + datetime.timedelta(hours=periods + i)
        elif d_type == "M":
            date = start_date + datetime.timedelta(minutes=periods + i)
        elif d_type == "S":
            date = start_date + datetime.timedelta(seconds=periods + i)
        elif d_type == "D":
            date = start_date + datetime.timedelta(days=periods + i)
        else:
            raise Exception("not")
        array_data.append((date, {"value": i}))
    return array_data


def generate_date_range_dt(d_type, start_date=None, columns=None, length=1000):
    """
    :param start_date:
    :param d_type:
    :param columns:
    :param length:
    :return:
    """
    if start_date is None:
        start_date = datetime.datetime.now(tz=pytz.UTC)
    if d_type == "H":
        index = pandas.date_range(start_date, periods=length, freq="H")

    elif d_type == "M":
        index = pandas.date_range(start_date, periods=length, freq="M")

    elif d_type == "S":
        index = pandas.date_range(start_date, periods=length, freq="S")

    elif d_type == "D":
        index = pandas.date_range(start_date, periods=length, freq="D")
    else:
        raise Exception("not")

    data = list(range(length))

    data_frame = pandas.DataFrame(index=index, data=data, columns=columns)
    return data_frame

import datetime

import pandas


def generate_timestamp_array(timestamp, length=1000):
    array_data = []
    for i in range(length):
        array_data.append((timestamp + i, {"value": i}))
    return array_data


def generate_date_range(start_date, d_type, periods=1, length=1000):
    array_data = []
    for i in range(length):
        if d_type == "h":
            date = start_date + datetime.timedelta(hours=periods + i)
        elif d_type == "m":
            date = start_date + datetime.timedelta(minutes=periods + i)
        elif d_type == "s":
            date = start_date + datetime.timedelta(seconds=periods + i)
        elif d_type == "d":
            date = start_date + datetime.timedelta(days=periods + i)
        else:
            raise Exception("not")
        array_data.append((date, {"value": i}))
    return array_data


def generate_date_range_dt(start_date, d_type, columns=None, length=1000):
    if d_type == "h":
        index = pandas.date_range(start_date, periods=length, freq="H")

    elif d_type == "m":
        index = pandas.date_range(start_date, periods=length, freq="M")

    elif d_type == "s":
        index = pandas.date_range(start_date, periods=length, freq="S")

    elif d_type == "d":
        index = pandas.date_range(start_date, periods=length, freq="D")
    else:
        raise Exception("not")

    data = list(range(length))

    data_frame = pandas.DataFrame(index=index, data=data, columns=columns)
    return data_frame

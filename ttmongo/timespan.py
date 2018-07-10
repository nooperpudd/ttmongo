from .client import TSMongoClient


class TimeSeriesTimeSpan(TSMongoClient):
    """
    test to use the engine
    """

    def __init__(self, client, db="", collection="",
                 index="", *args, **kwargs):
        super().__init__(client, db, collection, *args, **kwargs)

    def write(self,name,data):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def stats(self):
        pass

    def write(self, ):
        pass

    def write_many(self):
        pass

    def delete(self, name, start_timestamp=None, end_timestamp=None):
        pass

    def get_slice(self):
        pass

    def list_names(self):
        pass

    def max_timestamp(self, name):
        pass

    def min_timestamp(self, name):
        pass

    def iter(self, name, start_timestamp=None,
             end_timestamp=None):
        pass

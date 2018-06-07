# encoding:utf-8

import pymongo
import functools
import contextlib
import pytz

from bson.codec_options import CodecOptions


class MongoClient(object):
    """
    todo storage engine

    https://docs.mongodb.com/manual/reference/command/
    collMod/#dbcmd.collMod

    https://docs.mongodb.com/manual/core/schema-validation/

    # collection options

    The maximum BSON document size is 16 megabytes.
    Maximum Index Key Length for details

    Within a single mongod instance,
    timestamp values are always unique.

    insertOne
    updateOne
    updateMany
    replaceOne
    deleteOne
    deleteMany
    # Read Concern
    https://docs.mongodb.com/manual/reference/read-concern/
    https://docs.mongodb.com/manual/reference/write-concern/


    Capped Collections for recently data

    update unique index


    When using MMAPv1, if your applications require updates
    that will frequently cause document growth to exceeds the current
    power of 2 allocation, you may want to refactor your data model to
    use references between data in distinct documents rather than a
    denormalized data model.

    You may also use a pre-allocation strategy to explicitly avoid
     document growth. Refer to the Pre-Aggregated Reports
     Use Case for an example of the pre-allocation approach to
     handling document growth.

    support The Time to Live or TTL feature of collections
    expires documents after a period of time


    However, embedding related data in documents may lead to
    situations where documents grow after creation.
     With the MMAPv1 storage engine, document growth can
     impact write performance
      and lead to data fragmentation.

    Furthermore, documents in MongoDB must be smaller
     than the maximum BSON document size.

    """
    def __init__(self,client,db,tzone=pytz.UTC,**options):
        self.client =  client
        self._db = db
        self.tzone = tzone
        self.option = CodecOptions(tz_aware=True,tzinfo=tzone)

    @property
    @functools.lru_cache
    def db(self):
        return self.client[self._db]

    def get_collection(self):
        pass

    @property
    def query(self):
        """
        :return:
        """
        pass
    def ensure_index(self):
        """
        :return:
        """
        pass

    def stats(self):
        """
        :return:
        """
        pass
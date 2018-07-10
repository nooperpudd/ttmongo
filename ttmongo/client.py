# encoding:utf-8

import functools
import atexit
import pymongo
import pytz
from bson.codec_options import CodecOptions


class TSMongoClient(object):
    """
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

    retryable

    retryWrites=true

     MMAPv1 Storage Engine does not support retryable writes.

     # TEST different engine

     WiredTiger Storage Engine
     In-Memory Storage Engine
     MMAPv1 Storage Engine
    """

    def __init__(self, client: pymongo.MongoClient, db,
                 collection, tz=pytz.UTC, **options):
        """
        # todo add write corn read coren
        :param client:
        :param db:
        :param tz:
        :param options:
        """
        self.client = client
        self._db = db
        self.tz = tz
        self._collection = collection
        self.code_options = CodecOptions(tz_aware=True, tzinfo=tz)

        if not self.db.get_collection(collection):
            self.db.create_collection(collection)

    @property
    @functools.lru_cache
    def db(self):
        """
        :return:
        """
        return self.client.get_database(self._db,
                                        codec_options=self.code_options)

    def create_index(self, name, unique=True):
        """
        :return:
        """
        index = [(name, pymongo.ASCENDING)]
        self.collection.create_index(index, unique=unique)

    def count(self, column_name, value):
        """
        :param column_name:
        :param value:
        :return:
        """
        return self.collection.find({column_name: value}).count()

    @property
    @functools.lru_cache
    def collection(self):
        """
        :return:
        """
        return self.db.get_collection(self._collection)

    def __del__(self):
        self.client.close()

    def drop_db(self):
        """
        :return:
        """
        return self.client.drop_database(self.db)

    def drop_collection(self):
        """
        :return:
        """
        return self.db.drop_collection(self.collection)

    def get_engine(self):
        pass

    def read_concern(self):
        """
        Read Your Own Writes¶
Changed in version 3.6.

Starting in MongoDB 3.6, you can use causally consistent sessions to read your own writes, if the writes request acknowledgement.

Prior to MongoDB 3.6, you must have issued your write operation with { w: "majority" } write concern and then use either "majority" or "linearizable" read concern for the read operations to ensure that a single thread can read its own writes.

Real Time Order
Combined with "majority" write concern, "linearizable" read concern enables multiple threads to perform reads and writes on a single document as if a single thread performed these operations in real time; that is, the corresponding schedule for these reads and writes is considered linearizable.

Performance Comparisons
Unlike "majority", "linearizable" read concern confirms with secondary members that the read operation is reading from a primary that is capable of confirming writes with { w: "majority" } write concern. [2] As such, reads with linearizable read concern may be significantly slower than reads with "majority" or "local" read concerns.


        Always use maxTimeMS with linearizable read concern in case a majority of data bearing members are unavailable. maxTimeMS ensures that the operation does not block indefinitely and instead ensures that the operation returns an error if the read concern cannot be fulfilled.


        :return:
        """

    @property
    def write_concern(self):
        """
        https://docs.mongodb.com/manual/reference/write-concern/
        :return:
        """

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



    def bunks_wirte(self):
        """
        With an ordered list of operations, MongoDB executes the operations serially. If an error occurs during the processing of one of the write operations, MongoDB will return without processing any remaining write operations
        in the list. See ordered Bulk Write

        use order bulk write

        By default, bulkWrite() performs ordered operations.
         To specify unordered write operations, set ordered :
         false in the options document.


         Pre-Split the Collection

         If the sharded collection is empty, then the collection has only one initial chunk, which resides on a single shard. MongoDB must then take time to receive data, create splits, and distribute the split chunks to the available shards. To avoid this performance cost, you can pre-split the collection, as described in Split Chunks in a Sharded Cluster.

        To improve write performance to sharded clusters, use bulkWrite() with the optional parameter ordered set to false. mongos can attempt to send the writes to multiple shards simultaneously. For empty collections, first pre-split the collection as described in Split Chunks in a Sharded Cluster.

        Avoid Monotonic Throttling¶
If your shard key increases monotonically during an insert, then all inserted data goes to the last chunk in the collection, which will always end up on a single shard. Therefore, the insert capacity of the cluster will never exceed the insert capacity of that single shard.

If your insert volume is larger than what a single shard can process, and if you cannot avoid a monotonically increasing shard key, then consider the following modifications to your application:

        :return:
        """
        pass

    def iter(self):
        """
        https://docs.mongodb.com/manual/tutorial/iterate-a-cursor/
        cursor.close()

        For the MMAPv1 storage engine, intervening write operations on a document may result in a cursor that returns a
        document more than once if that document has changed. To handle this situation,
         see the information on Cursor Snapshot.

        MongoDB cursors can return the same document more than once in some situations.
        As a cursor returns documents other operations may interleave with the query.
        If some of these operations are updates that cause the document to move (in the case of MMAPv1,
        caused by document growth) or that change the indexed field on the index used by the query;
        then the cursor will return the same document more than once.

        If your collection has a field or fields that are never modified, you can use a unique index on
        this field or these fields so that the query will return each document no more than once.
        Query with hint() to explicitly force the query to use that index.

        As you iterate through the cursor and reach the end of the returned batch, if there are more results,
        cursor.next() will perform a getMore operation to retrieve the next batch. To see how many documents remain
         in the batch as you iterate the cursor, you can use the objsLeftInBatch() method, as in the following example:
        :return:
        """

import time
import os
from random import random, randint

from gevent import sleep
from asyncinflux import AsyncWriter
from influxdb import client as influxdb

db = influxdb.InfluxDBClient(database="test")
writer = AsyncWriter(db)
writer.start()
while True:
    cpu = os.times()
    point = [{
        "points": [[time.time(), random(), randint(1, 100)]],
        "name": u"cpu_memory",
        "columns":[u"time", u"load", u"memory_percent"]

    }]
    #print(point)
    writer.write_points(point)
    sleep(0.1)
writer.stop()

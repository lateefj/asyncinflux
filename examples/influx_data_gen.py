import time
import os
from random import random, randint
from asyncinflux import AsyncWriter
from influxdb import client as influxdb
db = influxdb.InfluxDBClient(database="test")
writer = AsyncWriter(db)
writer.start()
while True:
    cpu = os.times()
    point = [{
        "time":  time.time(),
        "points": [[random(), randint(1, 100)]],
        "name": u"cpu_memory",
        "columns":[u"load", u"memory_percent"]

    }]
    #print(point)
    writer.write_points(point)
    time.sleep(0.1)

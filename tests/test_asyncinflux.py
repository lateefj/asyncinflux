import unittest


import asyncinflux


class MockInfluxClient:

    def __init__(self):
        self.data = None

    def write_points(self, points):
        if self.data is not None:
            self.data.extend(points)
        else:
            self.data = points

class TestAsycWriteClient(unittest.TestCase):

    def test_single(self):
        mic = MockInfluxClient()
        awc = asyncinflux.AsyncWriter(mic)
        awc.start()
        awc.write_points([{"foo": "bar"}])
        awc.stop()
        assert mic.data is not None, 'Expected mic.data not to be None'
        assert mic.data[0].has_key('foo'), 'Expected mic.data to have key "foo" however it is {0}'.format(mic.data)
        assert mic.data[0]["foo"] == "bar", 'Expected data["foo"] to be "bar" but was {0}'.format(mic.data['foo'])

    def test_multiple(self):
        mic = MockInfluxClient()
        awc = asyncinflux.AsyncWriter(mic)
        awc.write_points([{"foo": "bar1"}])
        awc.write_points([{"foo": "bar2"}])
        awc.start()
        awc.stop()

        assert mic.data is not None, 'Expected mic.data not to be None'
        assert mic.data[0].has_key('foo'), 'Expected mic.data[0] to have key "foo" however it is {0}'.format(mic.data[0])
        assert mic.data[0]['foo'] == "bar1", 'Expected data[0]["foo"] to be "bar1" but was {0}'.format(mic.data['foo'])
        assert mic.data[1]['foo'] == "bar2", 'Expected data[1]["foo"] to be "bar2" but was {0}'.format(mic.data['foo'])

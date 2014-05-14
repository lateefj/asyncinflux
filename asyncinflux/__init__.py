from codap import spawn, Queue

class AsyncWriter:

    def __init__(self, client):
        """Wraps the client connection with an async call"""
        self.q = Queue()
        self.client = client

    def _run(self):
        """The actual code to write the points"""
        try:
            for data in self.q:
                self.client.write_points(data)
        except KeyboardInterrupt:
            raise

    def start(self):
        """Backgrounds the writing of data points"""
        self.background = spawn(self._run)

    def stop(self):
        """Stop the writting of data points"""
        self.q.put_nowait(StopIteration)
        self.background.join()

    def write_points(self, body):
        """ Basically wraps the influxdb call """
        self.q.put_nowait(body)

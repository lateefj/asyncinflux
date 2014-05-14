from codap import spawn, Queue


class AsyncWriter:
    RUN = False
    def __init__(self, client):
        """Wraps the client connection with an async call"""
        self.q = Queue()
        self.client = client
        self.stop_q = Queue()

    def start(self):
        """Backgrounds the writing of data points"""
        self.RUN = True
        spawn(self._run)

    def stop(self):
        """Stop the writting of data points"""
        self.RUN = False
        self.q.put(None)
        self.stop_q.get()


    def write_points(self, body):
        """ Basically wraps the influxdb call """
        self.q.put_nowait(body)

    def _run(self):
        while self.RUN or not self.q.empty():
            data = self.q.get()
            if data is not None:
                self.client.write_points(data)

        self.stop_q.put(None)

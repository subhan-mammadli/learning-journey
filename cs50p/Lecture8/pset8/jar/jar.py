class Jar:
    def __init__(self, capacity=12):
        self._cookie = 0
        self.capacity = capacity

    def __str__(self):
        return self._cookie * "🍪"

    def deposit(self, n):
        self._cookie += n
        if self._cookie > self.capacity:
            raise ValueError

    def withdraw(self, n):
        if n > self._cookie:
            raise ValueError
        self._cookie -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        if self._cookie > capacity:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._cookie

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError
        if size > self.capacity:
            raise ValueError
        self._cookie = size

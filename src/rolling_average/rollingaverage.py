from collections import deque

class RollingAverage:

    def __init__(self, size:int):
        self._size =  max (size, 2)
        self._sum = 0
        self._sample = deque()

    def average(self):
        if not len(self._sample):
            raise EmptySampleError("RollingAverage object has no samples. Division by zero.")
        
        return self._sum/len(self._sample)
    
    def sum(self):
        return self._sum
    
    def add(self, value):
        self._sample.append(value)
        self._sum += value

        if len(self._sample) > self._size:
            if (len(self._sample) - self._size) > 1:
                self._sum -= self._sample.popleft()    

            self._sum -= self._sample.popleft()

    def resize(self, new_size:int, discardExcess:bool=False):
        if new_size < 0:
            raise ResizingError(f"Cannot resize to a negative number (provided value: {new_size})")

        if new_size == 0:
            raise ResizingError("Cannot resize to zero")

        self._size = new_size

        if discardExcess and (len(self._sample) > self._size):
            self._sample = self._sample[(self._size * -1):]
            self._recalculate()

    def clearSamples(self):
        self._sum = 0
        self._sample.clear()


    def _recalculate(self):
        self._sum = 0

        for s in self._sample:
            self._sum += s

class ResizingError(Exception):
    pass

class EmptySampleError(Exception):
    pass
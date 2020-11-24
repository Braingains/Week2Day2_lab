from src.bus import Bus
from src.person import Person
class BusStop:

    def __init__(self, name):
        self.name = name
        self.queue = []

    def add_to_queue(self, person):
        self.queue.append(person)


bus_stop = BusStop("Waverly Station")
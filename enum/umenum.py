from enum import Enum, auto

class Weekday(Enum):
    Sunday = auto()
    Monday = auto()
    Tuesday = auto()
    Wednesday = auto()
    Thursday = auto()
    Friday = auto()
    Saturday = auto()

# Enumeration 

class OrderStatus(Enum):
    PENDING = auto()
    PROCESSING = auto()
    PROCESSED = auto()

class Order:
    def __init__(self):
        self.status = OrderStatus.PENDING

    def process(self):
        if self.status == OrderStatus.PROCESSED:
            raise RunTimeError(
                "Can't process order that has "
                "already been processed"
            )
        self.status = OrderStatus.PROCESSING
        self.status = OrderStatus.PROCESSED

ifa_books = Order()
print(ifa_books.process())

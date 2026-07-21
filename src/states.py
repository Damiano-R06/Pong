from enum import Enum

class State(Enum):
    START = 1
    RUNNING = 2
    PAUSE = 3
    P1WIN = 4
    P2WIN = 5
    END = 6
import sys
import time
from random import randint


class BaseFunction:
    def __init__(self):
        pass

    def create_percentage(self) -> int:
        return randint(0,100)

    def exponential_contamination(self, transmitters: int,
                                        contagion_level: int) -> int:
        max_percentage = 100
        return int(transmitters ** (contagion_level / max_percentage))

    def waiting_time_to_proceed(self, millisecond: float) -> str:
        print("\n-------------------------------------------------------")
        loading = f"{'*' * 55}"
        for char in loading:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(millisecond)
        return ''
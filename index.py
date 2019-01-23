import random
from time import sleep

from dictionary import MAJOR_CHORDS, MINOR_CHORDS

TARGET_CHORDS = MAJOR_CHORDS + MINOR_CHORDS

while True:
    print(f'\r          {random.choice(TARGET_CHORDS):10s}', end='')
    sleep(2)

import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("Limutin na ang mundo", 0.12),
        ("Nang magkasama tayo", 0.12),
        ("Sunod sa bawat galaw", 0.14),
        ("Hindi na maliligaw", 0.14),
        ("Hindi na maliligaw", 0.13),
        ("Hindi na maliligaw", 0.13),
        ("Hindi na maliligaw", 0.13),
        ("Hindi na maliligaw", 0.13),
        ("Hindi na maliligaw", 0.13),
        (" ", 150),
    ]

    delays = [4.2, 4.2, 4.2, 11.3, 4.2, 4.2, 4.2, 4.2, 4.2, 4.2]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')

print_lyrics()
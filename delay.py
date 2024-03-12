import time
import sys

def print_d(words, delay=""):
    d2 = float(delay)
    for char in words:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(d2)
    sys.stdout.write("""
""")
    sys.stdout.flush()


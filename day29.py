import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")
        time.sleep(3)

def print_letters():
    for letter in "ABCDE":
        print(f"Letter : {letter}")
        time.sleep(3)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t1.join()
t2.start()
t2.join()

#  wait threads


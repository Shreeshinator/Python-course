# multithreading is the concurrent execution of multiple threads within a single process. It allows for tasks to be performed simultaneously, improving the efficiency and responsiveness of applications. In Python, the `threading` module provides a way to create and manage threads.

import threading
import time

def walk_dog():
    time.sleep(8)  # Simulate time taken to walk the dog
    print("Finished walking the dog!")

def take_out_trash():
    time.sleep(2)  # Simulate time taken to take out the trash
    print("Finished taking out the trash...")

def get_mail():
    time.sleep(3)  # Simulate time taken to get the mail
    print("Finished getting the mail...")

# with time sleep they would have been executed sequentially, but with threading they can run concurrently, allowing for more efficient use of time. The main thread can continue executing while the other threads are performing their tasks.

chore1 = threading.Thread(target=walk_dog)
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

# In this example, they are done concurrently, so take out trash is done first, then get mail, and then finally walk the dog. If they were done sequentially, it would have taken 13 seconds (8 + 2 + 3) instead of just 8 seconds, which is the time taken for the longest task (walking the dog).

# chore1.join()  # Wait for walk_dog to finish
chore2.join()  # Wait for take_out_trash to finish
chore3.join()  # Wait for get_mail to finish

print("All chores are done!")
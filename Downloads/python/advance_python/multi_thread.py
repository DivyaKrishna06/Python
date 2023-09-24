import threading
import time

# Function to simulate a time-consuming task
def task(thread_num):
    print(f"Thread {thread_num} started.")
    time.sleep(2)  # Simulate some work
    print(f"Thread {thread_num} finished.")

# Create and start multiple threads
threads = []
for i in range(5):
    thread = threading.Thread(target=task, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All threads have finished.")
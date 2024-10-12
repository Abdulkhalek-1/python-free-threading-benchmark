import sys
import time
import threading


# CPU-bound task: Fibonacci sequence calculation
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# I/O-bound task: Simulate I/O task using sleep
def io_task(seconds):
    time.sleep(seconds)


# Benchmark function
def benchmark(task, args, num_threads):
    threads = []

    # Start time
    start_time = time.time()

    # Create threads
    for _ in range(num_threads):
        thread = threading.Thread(target=task, args=args)
        threads.append(thread)
        thread.start()

    # Join threads
    for thread in threads:
        thread.join()

    # End time
    end_time = time.time()

    # Return elapsed time
    return end_time - start_time


if __name__ == "__main__":
    NUM_THREADS = 4
    FIB_N = 30  # Adjust this for more intensive CPU-bound task
    IO_SLEEP_TIME = 1  # Simulate I/O task with 1 second sleep

    print("GIL state:", "Enabled" if sys._is_gil_enabled() else "Disabled")
    print("Benchmarking with", NUM_THREADS, "threads...")

    # CPU-bound benchmark
    cpu_time = benchmark(fibonacci, (FIB_N,), NUM_THREADS)
    print(f"CPU-bound task took {cpu_time:.2f} seconds.")

    # I/O-bound benchmark
    io_time = benchmark(io_task, (IO_SLEEP_TIME,), NUM_THREADS)
    print(f"I/O-bound task took {io_time:.2f} seconds.")

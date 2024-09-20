import time
import os
import sys
import resource  # Fallback for UNIX-based systems

# CPU Benchmark (Simple loop)
def cpu_benchmark():
    print("Starting CPU benchmark...")
    start_time = time.time()
    count = 0
    for i in range(10000000):  # Simple large loop
        count += 1
    end_time = time.time()
    cpu_time = end_time - start_time
    print("CPU benchmark finished.")
    print("Time taken for CPU benchmark: %.2f seconds" % cpu_time)

# Memory Benchmark (Allocate and hold large memory)
def memory_benchmark():
    print("Starting memory benchmark...")
    try:
        large_list = []
        for i in range(10000000):  # Create a large list to stress memory
            large_list.append(i)
        memory_size = sys.getsizeof(large_list) / (1024 * 1024)  # Convert bytes to MB
        print("Memory benchmark finished.")
        print("Memory used: %.2f MB" % memory_size)
    except MemoryError:
        print("MemoryError: Ran out of memory during benchmark!")

# Fallback Memory Usage with 'resource' (UNIX-based systems)
def get_memory_usage_fallback():
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        return mem_usage / 1024  # Convert to MB
    return None

# Run the benchmarks
cpu_benchmark()

# Fallback to resource library for memory measurement
initial_memory_usage = get_memory_usage_fallback()

if initial_memory_usage is not None:
    print("Initial memory usage (fallback): %.2f MB" % initial_memory_usage)
else:
    print("Unable to retrieve initial memory usage.")

memory_benchmark()

final_memory_usage = get_memory_usage_fallback()
if final_memory_usage is not None:
    print("Final memory usage (fallback): %.2f MB" % final_memory_usage)
else:
    print("Unable to retrieve final memory usage.")

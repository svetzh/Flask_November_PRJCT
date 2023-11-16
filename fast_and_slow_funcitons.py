import time

current_time = time.time()
print(current_time)

def speed_calulated_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"{(func.__name__).title()} run speed: {end_time - start_time}s")
    return wrapper

@speed_calulated_decorator
def fast_func():
    for i in range(20_000_000):
        i * i

@speed_calulated_decorator
def slow_func():
    for i in range(40_000_000):
        i * i


fast_func()
slow_func()
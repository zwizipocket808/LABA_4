import tracemalloc

def track_memory(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        mem_before = tracemalloc.get_traced_memory()[0]
        
        result = func(*args, **kwargs)
        
        mem_after = tracemalloc.get_traced_memory()[0]
        tracemalloc.stop()
        
        print(f"{func.__name__} использовала {mem_after - mem_before:,} байт")
        return result
    return wrapper

# Как использовать:
@track_memory
def create_list(n):
    return list(range(n))

@track_memory
def create_string(n):
    return "x" * n

# Проверка:
create_list(100000)
create_string(100000)

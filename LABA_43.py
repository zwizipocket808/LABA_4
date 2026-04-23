import tracemalloc

# Замыкание
def reader(source, n):
    if isinstance(source, bytes):
        pos = 0
        def get():
            nonlocal pos
            if pos >= len(source):
                return None
            start = pos
            pos = min(pos + n, len(source))
            return source[start:pos]
        return get
    else:
        def get():
            return source.read(n) or None
        return get

# Декоратор
def track_memory(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        before = tracemalloc.get_traced_memory()[0]
        result = func(*args, **kwargs)
        after = tracemalloc.get_traced_memory()[0]
        tracemalloc.stop()
        print(f"{func.__name__} использовала {after - before} байт")
        return result
    return wrapper

# Применяем декоратор к замыканию
data = b"Python is awesome"          # любые байты
raw_reader = reader(data, 3)         # замыкание
tracked_reader = track_memory(raw_reader)  # оборачиваем декоратором

# Тестируем
print(tracked_reader())  # b'Pyt'
print(tracked_reader())  # b'hon'
print(tracked_reader())  # b' is'
print(tracked_reader())  # b' aw'
print(tracked_reader())  # b'eso'
print(tracked_reader())  # b'me'
print(tracked_reader())  # None
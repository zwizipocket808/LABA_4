def make_reader(data, n):
    pos = 0
    def reader():
        nonlocal pos
        if pos >= len(data):
            return None
        result = data[pos:pos+n]
        pos += n
        return result
    return reader

# Данные (обратите внимание: 'World' а не 'WorLd')
data = b"Hello World! This is test bytes"
read_5_bytes = make_reader(data, 5)

print(read_5_bytes())  # b'Hello'
print(read_5_bytes())  # b' Worl'
print(read_5_bytes())  # b'd! Th'

# Для продолжения (чтобы консоль не закрывалась)
input("\nДля продолжения нажмите любую клавишу . . .")

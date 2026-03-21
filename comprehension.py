def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Викликаю функцію: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Функція завершена: {func.__name__}")
        return result
    return wrapper

@logger    
def calculate(a, b):
    return print(a + b)

calculate(2, 3)
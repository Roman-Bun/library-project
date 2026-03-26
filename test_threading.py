import threading
import time

def count_sum(data):
    # Додамо затримку, щоб імітувати "важку" роботу
    time.sleep(1) 
    result = sum(data)
    print(f"Сума списку {data}: {result}")

start = time.time()

threads = []
lists = [
    [1, 2, 3, 4, 5],
    [10, 20, 30, 40, 50],
    [100, 200, 300, 400, 500],
]

for num in lists:
    t = threading.Thread(target=count_sum, args=(num,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Загальний час: {time.time() - start:.1f} сек")
import time

print("Запущен процесс взлома...")
time.sleep(2)
for i in range(1, 10):
    print("Взлом. Прогресс - {}%".format(i*10))
    time.sleep(2)
print("Взлом успешно завершен!")

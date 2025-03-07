from collections import Counter

#открываем файл и читаем строки
with open("mbox.txt", "r", encoding="utf-8") as file: lines = file.readlines()

#извлекаем почтовые адреса
pochta = [line.split()[1] for line in lines if line.startswith("From ")]

#считаем количество писем каждого автора
kol_vo_pochty = Counter(pochta)

#ищем автора с МАХ числом писем
most_frequent_author = kol_vo_pochty.most_common(1)[0]

#чепятаем
print("Все авторы писем:")
for email, count in kol_vo_pochty.items():
    print(f"{email}: {count} писем")

print("\nАвтор, написавший больше всего писем:")
print(f"{most_frequent_author[0]} ({most_frequent_author[1]} писем)")
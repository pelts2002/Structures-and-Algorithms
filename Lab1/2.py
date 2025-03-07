#хэш-таблица через массив
hash_table = [[] for i in range(100)]  #100 списков внутри

def my_hash(word):
    h = 0
    for c in word:
        h += ord(c)
    return h % 100  #размер таблицы 100

def add(word):
    index = my_hash(word)
    if word not in hash_table[index]:  #проверяем, нет ли уже слова
        hash_table[index].append(word)

def check(word):
    index = my_hash(word)
    if word in hash_table[index]:
        print("yes")
    else:
        print("no")

#читаем команды с консоли
while True:
    s = input()
    if s == "exit":
        break
    cmd = s.split()
    if len(cmd) == 2:
        if cmd[0] == "add":
            add(cmd[1])
        elif cmd[0] == "check":
            check(cmd[1])
        else:
            print("неправильная команда")
    else:
        print("неправильный ввод")
# Задача 34:  Винни-Пух попросил Вас посмотреть,
# есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках
# не настолько просто, насколько легко 
# он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, 
# если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”,
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  



stroka = "парам-пам-пам  парам-пам пам-па-рам па-ра-ра-па-дам"
vowels = ['а','я','ы','и','й','у','е','о','э','ю']
list_phrases = stroka.split()
count_vow =[]
for phrases in list_phrases:
    count = 0
    for letter in phrases:
        if letter in vowels:
            count += 1
    count_vow.append(count)
print(count_vow)
if count_vow.count(count_vow[0]) == len(count_vow):
    print ("Парам пам - пам")
else:
    print ("Пам парам")
    

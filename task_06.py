# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

# quantity
total= int(input("Сколько журавликов сделали дети?: "))
if total%4==0:
    a = total//4
    b=a*2
    print(f"Петя сделал {a} журавликов")
    print(f"Коля сделал {a} журавликов")
    print(f"Катя сделалa {b} журавликов")
else:print("Такого количества журавликов при данном условии задачи дети сделать не могли")


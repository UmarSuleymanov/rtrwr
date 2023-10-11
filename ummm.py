# 1)Задача «р-1 »
#
# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
#     print(i)
#
# 2)Задача «р-2»
#
# a = int(input())
# b = int(input())
# if a < b:
#     for i in range(a, b + 1):
#         print(i)
# else:
#     for i in range(a, b - 1, -1):
#         print(i)
#
#
# Задача N3 (Сумма N чисел)
#
# n = int(input())
# sum = 0
# for i in range(n):
#     sum += int(input())
# print(sum)
#
#
# Задача N4 (Факториал)
#
# res = 1
# n = int(input())
# for i in range(1, n + 1):
#     res *= i
# print(res)
#
#
# Задача N5 (Лесенка)
#
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, sep='', end='')
#     print()
#
#
# Задача N6 (Список квадратов)
#
# n = int(input())
# i = 1
# while i ** 2 <= n:
#     print(i ** 2)
#     i += 1
#
#
# Задача N7 (Степень двойки)
#
# n = int(input())
# two_in_power = 2
# power = 1
# while two_in_power <= n:
#     two_in_power *= 2
#     power += 1
# print(power - 1, two_in_power // 2)
#
# Задача N8 (Утренняя пробежка)
#
# x = int(input())
# y = int(input())
# i = 1
# while x < y:
#     x *= 1.1
#     i += 1
# print(i)
#
#
# Задача N9 (Длина последовательности)
#
# len = 0
# while int(input()) != 0:
#     len += 1
# print(len)
#
#
# Задача N10 (Количество элементов, которые больше предыдущего)
#
# prev = int(input())
# answer = 0
# while prev != 0:
#     next = int(input())
#     if next != 0 and prev < next:
#         answer += 1
#     prev = next
# print(answer)
#
# Задача N11 (Второй максимум)
#
# old = int(input())
# k=1
# i = int(input())
# while(i != 0):
#     if(i>old):
#         print(i)
#         k+=1
#         break
#     else:
#         old = i
#         i = int(input())
# if(k!=2):
#     print(old)
#
#
# Задача N12 (Числа Фибоначчи)
#
# n1=0
# n2=1
# k=1
# a=int(input())
# while n2<a:
#     n1,n2=n2,n2+n1
#     k+=1
# if n2!=a:
#     print("-1")
# else:
#     print(k)
#
#
# Задача N14 (Четные индексы)
#
# a = input().split()
# for i in range(0, len(a), 2):
#     print(a[i])
#
# Задача N15 (Больше предыдущего)
#
# a = [int(i) for i in input(':').split()]
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i])
#
# Задача N16 (Наибольший элемент)
#
# max = 0
# index_of_max = -1
# s = input().split(' ')
# len = 0
# for i in s:
#     i = int(i)
#     if i > max:
#         max = i
#         index_of_max = len
#     len += 1
# print(max, index_of_max)

# Задача N17 (Шеренга)
#
# a = [int(i) for i in input().split()]
# x = int(input())
# pos = 0
# while pos < len(a) and a[pos] >= x:
#     pos += 1
# print(pos + 1)
#
# Задача N18 (Переставить соседние)
#
# a = [int(i) for i in input().split()]
# for i in range(1, len(a), 2):
#     a[i - 1], a[i] = a[i], a[i - 1]
# print(' '.join([str(i) for i in a]))
#
# Задача N19 (Переставить min и max)
#
# a = [int(s) for s in input().split()]
# a[a.index(max(a))], a[a.index(min(a))] = a[a.index(min(a))], a[a.index(max(a))]
#
#
# Задача N20 (Удалить элемент)
#
# a = [int(s) for s in input().split()]
# k = int(input())
# for i in range(k + 1, len(a)):
#     a[i - 1] = a[i]
# a.pop()
# print(' '.join([str(i) for i in a]))















































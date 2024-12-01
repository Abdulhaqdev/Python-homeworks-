# str = input("inter text ")
# print(str.upper(
# ))

# n = int(input("sonni kiritong :"))

 
# b = n % 10 
# o = n // 10 % 10
# y = n // 100
# m = n //  1000

# print(n , b )
# print( o )
# print( y)
# print(m)

# i = n
# b = n % 10 
# o = n // 10 % 10
# y = n % 1000 // 100
# m = i //  1000

# print("       ")
# print( b )
# print( o )
# print( y)
# print(m)

# g = 15000
# c = 14000
# m = 25000
# n = int(input("Pulingizni kiriting :"))

# i1 = g <= n
# i2 = c <= n
# i3 = m <= n

# print("gentra: ", i1 )
# print("coblit: ", i2 )
# print("mablibu: ", i3 )

 
# n = int(input("Pulingizni sumda kiriting :"))
# km = int(input("Oqishgasha nechi km: "))
# mr = int(input("nechta avtobus bilan borasiz: "))
# sum= int(input("taxi narxi: "))

# print(f"taxi: {sum * km <= n} ")
# print(f"Avtobus: {2000 * mr <= n}")

# -----------------1masala--------------

# m = int(input("kgni kiriting "))
# print(f"{m}kg = {m / 1000} tonna" )


# -----------------2masala-----------------

# bayt = int(input("baytni kiriting "))
# print(f"{bayt}kg = {bayt / 1024} tonna" )


# ----------------3masla------------------

# a = int(input("A sonni kiriting "))
# b = int(input("B sonni kiriting "))

# print(f"{a} soni ichida {b} soni {a/b} marta bor " )


# -----------------4 masala----------------

# a = int(input("A sonni kiriting "))
# b = int(input("B sonni kiriting "))

# print(f"{a} soni ichida {b} soni {a//b} marta yoq" )
# 

# -------------6 masala-----------------------

# s = int(input("sonni kiriting "))

# print(f"birlar xonasi  {s % 10}" )
# print(f"onlar xonasi  {s // 10 % 10}" )


# -------------7 masala ------------------------

# s = int(input("sonni kiriting "))

# print(f"raqamlar yigindisi  {(s % 10 ) + (s // 10 % 10)} " )


# ---------------8 masala-----------------------
# s = int(input("sonni kiriting "))

# b = str(s % 10) 
# o =str(s // 10 % 10)

# print(o+b)

# --------------9 masala -----------------------
# s = int(input("sonni kiriting "))

# print(s% 1000 // 100)

# -----------------------10 masala -------------------
# s = int(input("sonni kiriting "))

# print(s% 10 )
# print(s% 1000 // 100)

# -------------------- 11 masala -----------------------
# s = int(input("sonni kiriting "))

# print(s% 10 + s // 10 % 10+s% 1000 // 100 )

# -----------------------12 masala--------------------

# s = int(input("sonni kiriting "))

# b = str(s % 10) 
# o =str(s // 10 % 10)
# y= str(s % 1000 // 100)

# print(y+o+b)

# ------------------- 13 masala ----------------------
# s = int(input("sonni kiriting "))

# b = str(s % 10) 
# o =str(s // 10 % 10)
# y= str(s % 1000 // 100)

# print(o+y+b)

# ---------------------- 15 ---------------------------
# s = int(input("sonni kiriting "))

# b = str(s % 10) 
# o =str(s // 10 % 10)
# y= str(s % 1000 // 100)

# print(y+b+o)

# --------------------16 ------------------------------
# s = int(input("sonni kiriting "))

# b = str(s % 10) 
# o =str(s // 10 % 10)
# y= str(s % 1000 // 100)

# print(o+b+y)

# ----------------------uyga-1-----------------------------

# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# fruits.remove("banana")
# print(fruits)

# ---------------------------2------------------------------

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# numbers = [x for x in numbers if x % 2 != 0]

# print(numbers)

# ----------------------3-----------------------------------

# my_list = [10, 20, 30, 40, 50, 60, 70, 80]

# print(my_list[0:3] + my_list[6:8])

# ---------------------4---------------------------------

# cities = ["New York", "London", "Tokyo", "Moscow", "Paris"]

# del cities[2]

# print(cities)

# ---------------------5-----------------------------

# numbers = [5, 10, 15, 20, 25]

# del numbers[0]
# size = len(numbers)
# del numbers[size-1]

# print(numbers)

# ---------------6------------------------

# fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# print(fruits.remove("banana"))

# -------------------7---------------------

# items = [1, 2, 3, 4, 5]
# del items

# print(items)


# -------------------8-----------------

# cars = ["Toyota", "Ford", "BMW", "Audi"]

# cars.append(cars.pop(1))

# print(cars)

# ---------------9------------
# numbers = [1, 2, 3, 4, 5]

# numbers = numbers[::-1]

# print(numbers)


# Task 1: Tuple yaratish va elementlarga murojaat qilish

# fruits = ('apple', 'banana', 'cherry', 'orange', 'kiwi')

# print("Task 1: Birinchi element:", fruits[0])

# print("Task 1: Oxirgi element:", fruits[-1])

# print("Task 1: Uchinchi element:", fruits[2])


# Task 2: Tuple elementlarini hisoblash

# numbers = (1, 2, 3, 4, 2, 5, 6, 2)

# count_of_twos = numbers.count(2)
# print("Task 2: Tuple'da 2 soni", count_of_twos, "marta bor")

# index_of_five = numbers.index(5)
# print("Task 2: 5 soni", index_of_five, "indeksda joylashgan")


# Task 3: Tuple'dan ro'yxatga aylantirish
# colors = ('red', 'green', 'blue')

# Tuple'ni ro'yxatga aylantirish
# colors_list = list(colors)

# colors_list.append('yellow')

# colors_tuple = tuple(colors_list)
# print("Task 3: Yangi tuple:", colors_tuple)


# Task 4: Tuple'ni teskari qilish

# letters = ('a', 'b', 'c', 'd', 'e')

# reversed_letters = letters[::-1]
# print("Task 4: Teskari qilingan tuple:", reversed_letters)


# Task 5: Tuple ichidagi tuple


# nested_tuple = (1, 2, (3, 4, 5), 6, 7)

# print("Task 5: Ichkaridagi tuple'dagi ikkinchi element:", nested_tuple[2][1])

# for element in nested_tuple:
#     print("Task 5: Element:", element)


# ---------------------------------1------------------------------

# n = int(input("sonni kiritng :"))

# if(n > 0 ):
# 	print(n+1)
# else:
# 		print(n)

# ----------------------------------------2-------------------------

# n = int(input("sonni kiritng :"))
                 
# if(n > 0 ):
# 	print(n+1)
# else:
# 		print(n-2)


# ----------------------------------3---------------------------

# n = int(input("sonni kiritng :"))

# if(n > 0 ):
# 	print(n+1)
# else:
# 		print(n-2)
# if(n == 0):
# 	  print(10)


# ---------------------------------------------4-------------

# a = int(input("1-sonni kiriting :"))
# b = int(input("2-sonni kiriting :"))
# c = int(input("3-sonni kiriting :"))

# count = 0

# if(a > 0):
# 	count =+ 1
# if(b > 0):
# 	count =+ 1
# if(c > 0):
# 	count =+ 1

# print(count)


# -------------------------------------5---------------------

# a = int(input("1-sonni kiriting :"))
# b = int(input("2-sonni kiriting :"))
# c = int(input("3-sonni kiriting :"))

# count = 0
# count1 = 0


# if(a > 0):
# 	count =+ 1
# if(b > 0):
# 	count =+ 1
# if(c > 0):
# 	count =+ 1
# if(a < 0):
# 	count1 =+ 1
# if(b < 0):
# 	count1 =+ 1
# if(c < 0):
# 	count1 =+ 1
# print(count1)

# ---------------------------6--------------------------------------------

# a = int(input("1-sonni kiriting :"))
# b = int(input("2-sonni kiriting :"))

# c =0

# if(a>b):
# 	c = a
# if(a<b):
# 	c=b

# print(c)

# --------------------------------7--------------------------------

# a = int(input("1-sonni kiriting :"))
# b = int(input("2-sonni kiriting :"))

# c = 0
# i = 0
# if(a>b):
 	# i = 1
	# c = a
# if(a>b):
# 	c = b
#   i = 2
# print(c , i)


# -----------------------------------8------------------------

# a = int(input("1-sonni kiriting :"))
# b = int(input("2-sonni kiriting :"))

# c = 0
# u = 0
# if(a>b): 
# 	c = a
# if(a<b):
# 	u=b

# print(c,u)


# ----------------------------9-------------------------------

# a = float(input("A: "))
# b = float(input("B: "))

# if a > b:
#     a, b = b, a

# print(f"A = {a}, B = {b}")


# --------------------------10----------------------------
# a = int(input("A: "))
# b = int(input("B: "))

# if a != b:
#     a = a + b
# else:
#     a = 0
#     b = 0

# print(f"A = {a}, B = {b}")


# -------------------------------11------------------------------------
# a = int(input("A: "))
# b = int(input("B: "))

# if a != b:
#     if a > b:
#         b = a
#     else:
#         a = b
# else:
#     a = 0
#     b = 0

# print(f"A = {a}, B = {b}")

# ------------------------------------12------------------------------------
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# min_num = a

# if b < min_num:
#     min_num = b
# if c < min_num:
#     min_num = c

# print(f"Kichik son: {min_num}")


# ---------------------------------13-------------------------

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# if (a > b and a < c) or (a < b and a > c):
#     print(f"O'rta son: {a}")
# elif (b > a and b < c) or (b < a and b > c):
#     print(f"O'rta son: {b}")
# else:
#     print(f"O'rta son: {c}")


# ----------------------------------13-------------------------------

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# if a < b:
#     if a < c:
#         if b < c:
#             print(a, b, c)
#         else:
#             print(a, c, b)
#     else:
#         print(c, a, b)
# else:
#     if b < c:
#         if a < c:
#             print(b, a, c)
#         else:
#             print(b, c, a)


# ------------------------------14--------------------------

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# if a + b >= a + c and a + b >= b + c:
#     print(a, b)
# elif a + c >= a + b and a + c >= b + c:
#     print(a, c)
# else:
#     print(b, c)

# ---------------------15---------------------------------------
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# if a + b >= a + c and a + b >= b + c:
#     print(a, b)
# elif a + c >= a + b and a + c >= b + c:
#     print(a, c)
# else:
#     print(b, c)


# ---------------------------16-------------------------
# a = float(input("A: "))
# b = float(input("B: "))
# c = float(input("C: "))

# if a <= b <= c:
#     a *= 2
#     b *= 2
#     c *= 2
# else:
#     a = -a
#     b = -b
#     c = -c

# print(f"A = {a}, B = {b}, C = {c}")


# --------------------------------------17----------------------------------

# a = float(input("A: "))
# b = float(input("B: "))
# c = float(input("C: "))

# if a >= b >= c:
#     a *= 2
#     b *= 2
#     c *= 2
# else:
#     a = -a
#     b = -b
#     c = -c

# print(f"A = {a}, B = {b}, C = {c}")

# -----------------------------------18------------------------------
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# if a == b:
#     print("C soni boshqa:", 3)
# elif a == c:
#     print("B soni boshqa:", 2)
# else:
#     print("A soni boshqa:", 1)


# -------------------------------------------19------------------
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# d = int(input("d: "))

# if a == b == c:
#     print("D soni boshqa:", 4)
# elif a == b == d:
#     print("C soni boshqa:", 3)
# elif a == c == d:
#     print("B soni boshqa:", 2)
# else:
#     print("A soni boshqa:", 1)


# -----------------------------------20-----------

# a = float(input("A nuqtasi: "))
# b = float(input("B nuqtasi: "))
# c = float(input("C nuqtasi: "))

# if abs(a) <= abs(b) and abs(a) <= abs(c):
#     print("Eng yaqin nuqta: A va masofa:", abs(a))
# elif abs(b) <= abs(a) and abs(b) <= abs(c):
#     print("Eng yaqin nuqta: B va masofa:", abs(b))
# else:
#     print("Eng yaqin nuqta: C va masofa:", abs(c))


# -------------------------21-------------------
# x = int(input("X koordinatasi: "))
# y = int(input("Y koordinatasi: "))

# if x == 0 and y == 0:
#     print(0)
# elif x == 0 or y == 0:
#     print(1)
# else:
#     print(2)


# ----------------------------------22---------------------
# x = int(input("X koordinatasi: "))
# y = int(input("Y koordinatasi: "))

# if x > 0 and y > 0:
#     print("1-chorak")
# elif x < 0 and y > 0:
#     print("2-chorak")
# elif x < 0 and y < 0:
#     print("3-chorak")
# else:
#     print("4-chorak")

# ----------------------------------23------------------------------------

# x1 = int(input("1-uchning X koordinatasi: "))
# y1 = int(input("1-uchning Y koordinatasi: "))
# x2 = int(input("2-uchning X koordinatasi: "))
# y2 = int(input("2-uchning Y koordinatasi: "))
# x3 = int(input("3-uchning X koordinatasi: "))
# y3 = int(input("3-uchning Y koordinatasi: "))

# if x1 == x2:
#     print(f"To‘rtinchi uch koordinatasi: ({x3}, {y1})")
# elif x1 == x3:
#     print(f"To‘rtinchi uch koordinatasi: ({x2}, {y1})")
# else:
#     print(f"To‘rtinchi uch koordinatasi: ({x1}, {y2})")


# -----------------------------------------------------------------------------------------------------------

# ats = int(input("Avtomobil summasini kiritng: "))
# foiz = int(input("Foizni kiriting (30, 40, 50): "))
# oy = int(input("Nechi oy: "))

# if foiz >= 50:
#     pay = ((ats / 2) + (ats / 2 * 0.10)) / oy
# elif foiz == 40:
#     pay = ((ats * 0.40) + (ats / 2  * 0.175)) / oy
# elif foiz == 30:
#     pay = ((ats * 0.30) + (ats / 2  * 0.25)) / oy
# else:
#     print("Noto'g'ri foiz kiritildi.")
#     pay = None
    
# print(f"Oylik to'lov: {pay:.2f}")


# ----------------------------------------------------------


# x1 = int(input("1 sonni kiriting : "))
# x2 = int(input("2 sonni kiriting : "))

# if x1 < x2 :
#  while x1 <= x2:
#     print(x1)
#     x1+=1
# elif x1 > x2 :
#     while x1 >= x2:
#      print(x1)
#      x1+=1


# ----------------------------------------------------------------------------------------------------

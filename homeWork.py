# ------------------------1---------------------------
# i = 1
# s = 0 

# while i :
# 	n = int(input(" sonni kiriting :"))
# 	if n != 0:
# 			s+=n
# 	elif n == 0:
# 		i = 0

# print(s)

# -------------------------2---------------------------


# a = int(input("birinshi sonni kiriting :"))
# b = int(input("ekiinchi sonni kiriting :"))

# s = 0

# while a < b :
# 	s += a 
# 	a += 1

# print(s)


# ---------------------------3-------------------------

# arr = []

# i = 1

# while i < 6 :
# 		n = int(input("sonni kiriting :"))
# 		arr.append(n)
# 		print(len(arr))
# 		i += 1
# print(arr)		

# -------------------------------4-----------------------


# x = [1, 2, 3, 14, 5, 6, 6, 7]

# i = 0
# s = x[0] 

# while i < len(x):
#     if s < x[i]:
#         s = x[i]
#     i += 1

# print(s)


# ----------------------------------------5--------------------

# x = [1, 2, 3, 14, 5, 6, 6, 7]

# i = 0
# s = 0

# while i < len(x):
# 		if x[s] < x[i]:
# 			s = i 
# 		i+=1

# print(s)

# -----------------------6---------------------------------------

# n = input('sonni kiriting :')
# print(len(n))


# -------------------------7--------------------------------------

# 7-masala
#
# x = [1, 2, 0, 14, 5, -6]
#
# maximum = x[0]
# minimum = x[1]
# i = 0
# while i <len(x):
#     if x[i] > maximum:
#         maximum = x[i]
#     if x[i] < minimum:
#         minimum = x[i]
#     i += 1
# print(maximum)
# print(minimum)

# -----------------------------------8-----------------------

# x = [-2, 31, 104, 51, 19, 7]
# i = 0
#
# maximum = x[0]
# minimum = x[1]
# while i <len(x):
#     if x[i] > maximum:
#         maximum = x[i]
#     if x[i] < minimum:
#         minimum = x[i]
#     i += 1
# k = x.index(maximum)
# d = x.index(minimum)
# x[k] = minimum
# x[d] = maximum
# print(x)

# -------------------------9-------------------------------

# k = int(input("Son kiritng:"))
# x = [-2, 31, 104, 51, 19, 7]
# i = 0
# str = 'element yoq'
# while i < len(x):
#     if x[i] == k:
#         str = 'Ellement bor'
#         break
#     i += 1
# print(str)

# ----------------------1----------------------

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target = int(input(f"What's the target? "))
# i = 0

# while i < len(arr):
# 	if arr[i] == target: 
# 		print(True)
# 		break 
# 	if i == len(arr)-1: print(False)
# 	i += 1

# b = False

# while i < len(arr) :
# 	if arr[i] == target :
# 		b = True
# 	i+=1

# print(b)

# ----------------------------------2------------------------------------


# i = 100

# while i <= 999 :
# 	b = i % 10
# 	o = i // 10 % 10
# 	y = i // 100 % 10
# 	s = b + o + y  
# 	if 5 < s < 8 :
# 		print(i) 
# 	i += 1


# ----------------------------------3-------------------------------------
# Ekrandan son kiritilsa shu son kecha xonali ekangini aniqlang

# n = int(input("sonni kiriting :"))
# s = 0

# while n:
# 	n //= 10
# 	s += 1

# print(s)


# 4 - masala Ekrandan sonlar kiritiladi masalalan 5 yoki 10 ta shun sonlarni yig'indisini chiqaring

# i = 0
# s = 0

# while i < 4:
# 	n = int(input("sonni kiriting :"))
# 	s += n
# 	i += 1

# print(s)



# 5 - masala Ekrandan sonlar kiritiladi masalalan 5 yoki 10 ta shun sonlarni kattasini chiqaring

# i = 0
# s = 1

# while i < 4:
# 	n = int(input("sonni kiriting :"))
# 	if s < n :
# 		s = n
# 	i += 1

# print(s)



# 6 - masala Ekrandan sonlar kiritiladi masalalan 5 yoki 10 ta shun sonlarni  kichigini chiqaring

# i = 0
# s = 1

# while i < 4:
# 	n = int(input("sonni kiriting :"))
# 	if s >  n :
# 		s = n
# 	i += 1

# print(s)


# 7-masala List yarating hosil bolgan listning har bir elementiga 2 ni ko'paytirib ekranga chiqaring
  
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# i = 0

# while i < len(arr) :
# 	arr[i] = arr[i] * 2
# 	i += 1

# print(arr)


# 8- masala Mukammal son yoki Mukammal son elasligini tekshiring mukammal sonlar o'zidan tashqari bo'luvchilarini yig'indisi o'ziga teng Masalan : 28 -> 1,2,4,7,14 shu sonlarning yigindisi 28 ga teng

# n = int(input("sonni kiriting :"))
# i = 1
# s = 0

# while  i < n :
# 	if n % i == 0 :
# 		s += i
# 	i += 1
# if s == n: 
# 	print(True)
# else:
# 	print(False)


# 9-masala Ekrandan son kiritilsa shu son 2 ning darajasi bo'lsa darajasi aks holda darajasi emas kabi so'zlarni chiqaring


# n = int(input("sonni kiriting :"))

# i = 1
# b = False
# while i <= n:
# 	if n == i:
# 		b = True
# 	i *= 2



# while n >= 2:
# 	if n == 2:
# 		b = True
# 	n /= 2
# print(b)


#10-masala Ekrandan son kiritilsa shu son 2 ning darajasi bo'lsa nechanchi darajasi ekanligini aks holda darajas emas kabi so'zlarni chiqaring

# n = int(input("sonni kiriting :"))

# i = 1
# a = 0

# while i <= n:
# 	if n == i:
# 		a = i
# 	i *= 2

# print(a)

# 11-masala Ekrandan son kiritiladi shu sonning faktorialini chiqaring


# 12-masala List berilgan x = [1,23,10,45,-41,56,78,13] shu listning juft va toq elementlarini 2 ta  alohida listga yuklang

# x  = [1,23,10,45,-41,56,78,13]

# i = 0

# x1 = []
# x2 = []

# while i < len(x) :
# 	if x[i] % 2 == 0:
# 		x1.append(x[i])
# 	else :
# 		x2.append(x[i])
# 	i += 1

# print(x1)
# print(x2)


# 13-masala  Ekrandan biror son kiritilsa shunga mos holda karra jadvalini chiqaring 

# n = int(input("sonni kiriting :"))

# i = 1

# while i < 10 :
# 	print(f"{i} * {5} = {i * n}")
# 	i += 1

#  14-masala List berilgan cars = ["Audi", "Tayota", "Mazda", "Volvo", "Lada"] berilgan list elementlari ichidan eng uzun so'zni toping va uni ekranga chiqaring

# a = 100
# b=1.0001
# s = 0 

# while a <= 200 :
# 	a*=b
# 	s+=1

# print(s)


#1-masala 1 dan 100 gacha bo’ldan sonlarni yig’indisini toping

# s = 0

# for i in range(0, 100, 1) :
# 		s += i

# print(s)


# 2 masasla 1 da 50 gacha bo’lgan toq va juft sonlarni yig’indisini hisoblash.


# s = 0

# for i in range(0, 50, 1) :
# 		if i % 2 == 0 : 
# 		  s += i

# print(s)

# 3-masala -80 dan 80 gacha bo’lgan sonlar ichida 7 ga bo’linadiganlarni nechta ekanligini toping.

# s = 0

# for i in range(-80, 80, 1) :
# 		if i % 7 == 0 : 
# 		  s += 1

# print(s)


# 4-masala List berilgan mevalar = ['olma', 'banan', 'apelsin‘, ‘olma’]
# Listning ichida nechta ‘olma’ so’z borligni aniqlang.

# mevalar = ['olma', 'banan', 'apelsin', 'olma']

# s = 0 
# for meva in mevalar:
# 	if 'olma' == meva:
# 		s += 1

# print(s)		 


# 5-masala 	 A dan B gacha sonlar berilgan berilgan son ichida nechta toq va juft sonlar borligni aniqlang.

# a = int(input("a ni kiriting :"))
# b = int(input("b sonni kiriting :")) 


# s = 0 
# s2 = 0

# for i in range (a, b ,1) :
# 	if i % 2 == 0 :
# 		s += 1
# 	else:
# 		s2 += 1

# print(s)
# print(s2)

# 6-masala List x = [1,2,3,4,5,6,6,7,8,9] berilgan list ichida 2 ga bo’linadiganlarni nechta ekanligini aniqlang.

# x = [1,2,3,4,5,6,6,7,8,9]

# s = 0

# for i in x :
# 	if i % 2 == 0 :
# 		s += 1

# print(s)

# 7 masala . Ekrandan matn kiritiladi masalan: “Welcome to System”  shu matn ichida nechta katta harf bor ekanligini aniqlang.

# str = str(input("matnni kiriting :"))
# count = 0 
# for harf in str :
# 	if harf.isupper():
# 		count+=1
# print(count)

# 8 fizz buzz masala

# for i in range(1,100,1):
# 	if i % 3 != 0 and i % 5 != 0 :
# 		print(i)
# 	elif i % 3 == 0 and i % 5 == 0 :
# 		print("fizzbuzz")
# 	elif i  % 3 == 0  :
# 		print("fizz")
# 	elif i  % 5 == 0  :
# 		print("buzz")
# 
# 9-masala	

# dyumlar = [1, 2, 3, 4, 5]

# for i in dyumlar:
# 	dyumlar.append(i * 2.54)
# 	dyumlar.remove(i)

# print(dyumlar)

# 10-masla 

# sonlar = [5, 10, 15, 20, 25, 30]

# for i in sonlar :
# 	if i % 2 != 0 or i < 10 :
# 		continue
# 	print(i)


# 11-masalan
# sonlar = [5, 10, 15, 20, 25, 30]
# newlist = [i%3 for i in sonlar]

# print(newlist)



# x = ["olma", "banana", "olcha", "limon", "olxo'ri"]


# [print(i) for i in x if i.startswith("o")]


# Set (To'plam) bilan bog'liq masalalar:
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<---------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# 1.  To'plamdagi elementlarning unikal sonini hisoblash
#     To'plamni yarating va undagi elementlarning nechta unikal ekanligini aniqlang.


# numbers = [2, -3,5,4,3,2,-4,5,5,0, 2, 1]
# numbers2 = set(numbers)

# print(numbers)
# print(numbers2)
# print(len(numbers)- len(numbers2))



# 2.  Ikki to'plamning kesishmasini (intersection) topish
#     Ikkita to'plam berilgan, ularning kesishmasini toping.



# numbers1 = {2, -3,5,4,3,2,-4,5,5,0, 2, 1}
# numbers2 = {2, 43,5 ,44,5,43,0, 2, 1,3}

# newnumbers = numbers1 & numbers2

# print(newnumbers)



# 3.  To'plamdagi elementlarni o'chirish
#     To'plamda berilgan elementni o'chirishni amalga oshiring.

# numbers1 = {2, -3,5,4,3,2,-4,5,5,0, 2, 1}

# numbers1.remove(2)

# print(numbers1)

# 4.  To'plamni birlashtirish
#     Ikki yoki undan ortiq to'plamni birlashtirib, yangi to'plam yarating.



# numbers1 = {2, -3,5,4,3,2,-4,5,5,0, 2, 1}
# numbers2 = {2, 43,5 ,44,5,43,0, 2, 1,3}

# totalnum = numbers1.union(numbers2)

# print(totalnum)


# 5.  To'plamdagi eng katta va eng kichik elementni topish
#     To'plamdagi maksimal va minimal qiymatlarni aniqlang.


# numbers2 = {2, 43,5 ,44,5,43,0, 2, 1,3}

# max = max(numbers2)

# min = min(numbers2)

# print(max)
# print(min)



# 6.  To'plamdagi elementlarni o'zgartirish
#     To'plamni yaratib, unga yangi element qo'shing va eski elementni o'chirib tashlang.


# numbers2 = {2, 43,5 ,44,5,43,0, 2, 1,3}
# print(numbers2)

# numbers2.add(77)
# numbers2.remove(2)

# print(numbers2)


# 7.  Ikki to'plamning farqini (difference) hisoblash
#     Ikkita to'plam berilgan, ularning farqini toping (ya'ni, birinchi to'plamda bor, lekin ikkinchi to'plamda yo'q).


# numbers1 = {2, -3,5,4,3,2,-4,5,5,0, 2, 1}
# numbers2 = {2, 43,5 ,44,5,43,0, 2, 1,3}


# n =numbers2.difference(numbers1)

# print(n)


# 8.  To'plamdagi elementlarning ko'paytmasini hisoblash
#     To'plamda raqamli elementlar bor, ularning ko'paytmasini hisoblash.


# numbers1 = {2, -3,5,4,3,2,-4,5,5, 2, 1}

# s = 1

# for n in numbers1:
# 	s *= n 
# 	print(s)


# 9.  To'plamda bo'sh joyni tekshirish
#     To'plamning bo'sh yoki yo'qligini tekshirib chiqing.


# numbers1 = {2, -3,5,4,3, " ",2,-4,5,5, 2, 1}

# s = False

# for n in numbers1:
# 	if n == " " :
# 		s = True

# print(s)


# 10. To'plamning uzunligini hisoblash
#     To'plamdagi elementlar sonini hisoblang.


# numbers1 = {2, -3,5,4,3, " ",2,-4,5,5, 2, 1}

# s = 0

# for n in numbers1:
# 	s += 1

# print(s)
# print(len(numbers1))

# Dictionary (Lug'at) bilan bog'liq masalalar:

# 11. Lug'atni yaratish va element qo'shish
#     Bo'sh lug'at yarating va unga yangi elementlar qo'shing.


# password  = { 

# }

# print(password)
# password2  = { 
# 	'a':123 
# }
# password.update(password2)

# print(password)



# 12. Lug'atdagi elementni yangilash
#     Lug'atdagi mavjud elementni yangilang.

# password  = { 
# 		'ali': 1234,
# 	'babur': 4323,
# 	'nodir': '213ere',
# 	'sardor': 123456778,
# }

# print(password)

# password['ali'] = 4321

# print(password)



# 13. Lug'atdagi kalitni o'chirish
#     Lug'atdan ma'lum bir kalitni o'chirish.

# password  = { 
# 	'ali': 1234,
# 	'babur': 4323,
# 	'nodir': '213ere',
# 	'sardor': 123456778,
# }

# print(password)

# password.pop('ali') 

# print(password)



# 14. Lug'atdan faqat kalitlarni olish
#     Lug'atda faqat kalitlar (keys) ro'yxatini olish.


# password  = { 
# 	'ali': 1234,
# 	'babur': 4323,
# 	'nodir': '213ere',
# 	'sardor': 123456778,
# }

# for x in password :
# 	print(x)


# 15. Lug'atdagi eng katta qiymatni topish
#     Lug'atdagi maksimal qiymatni toping.



# password  = { 
# 	'ali': 1234,
# 	'babur': 4323,
# 	'nodir': '213ere',
# 	'sardor': 123456778,
# }

# max = max(password)
# print(max)



# 16. Lug'atni tartiblash
#     Lug'atdagi elementlarni qiymatlari bo'yicha tartiblang.

# my_dict = {'a': 3, 'b': 1, 'c': 4, 'd': 2}

# sorted_dict = sorted(my_dict)

# print(sorted)

# 17. Lug'atda kalit mavjudligini tekshirish
#     Lug'atda ma'lum bir kalit bor yoki yo'qligini tekshiring.


# my_dict = {'a': 3, 'b': 1, 'c': 4, 'd': 2}

# a = input('keyni kiriting : ')

# for x in my_dict: 
# 	if a == x :
# 		print(True)
# 	else: 
# 		print(False)


# 18. Lug'atda elementlar sonini hisoblash
#     Lug'atdagi elementlar sonini aniqlang.


# my_dict = {'a': 3, 'b': 1, 'c': 4, 'd': 2}
# s = 0
# for x in my_dict: 
# 	s += 1

# print(s)
# print(len(my_dict))



# 19. Lug'atni tekshirish va qo'shish
#     Lug'atga yangi element qo'shishdan oldin, mavjudligini tekshiring.



# my_dict = {'a': 3, 'b': 1, 'c': 4, 'd': 2}

# # Foydalanuvchidan kalit so'rash
# a = input('Keyni kiriting: ')

# # Kalit mavjudligini tekshirish
# if a in my_dict:
#     print('Element allaqachon qo\'shilgan.')
# else:
#     # Yangi element qo'shish
#     my_dict[a] = int(input(f"{a} uchun qiymatni kiriting: "))

# print(my_dict)



# 20. Lug'atni birlashtirish
#     Ikki lug'atni birlashtiring va natijaviy lug'atni qaytaring.



# my_dict1 = {'a': 3, 'b': 1, 'c': 4, 'd': 2}
# my_dict2 = {'s': 64, 'g': 54, 'f': 45, 'l': 2}

# my_dict1.update(my_dict2)
# print(my_dict1)

# n = int(input("Son kiriting (n): "))
 
# if n > 0:
#         digits = 1
#         while digits <= n:
#             start = 10**(digits - 1)   
#             end = 10**digits  
#             print(f"{digits} xonali sonlar:")
#             number = start
#             while number < end:
#                 print(number)
#                 number += 1
#             print()  
#             digits += 1
# else:
#         print(" musbat son kiriting")



# --------------------------------------------------------
# Masala 1 
# a = int (input("A ni kirting : "))
# b = int (input("B ni kirting : "))

# count = 0 
# while a >= b :
#     a-=b
#     count+=1

# print(count)

# Masala 2
# a = int (input("A ni kirting : "))
# b = int (input("B ni kirting : "))


# while a >= b :
#     a-=b

# print(a)

# Masala 3
# n = int (input("N ni kirting : "))
# k = int (input("K ni kirting : "))


# while n >= k :
#     n-=k

# print(n)


# Masala 4
# n = int(input("n: "))
# x = 1
# while x < n:
#     x *= 3
# if x == n:
#     print("3 - ning darajasi")
# else:
#     print("3 - ning darajasi emas")

# Masala 5
# n = int(input("n: "))
# x = 1
# while x < n:
#     x *= 2
# if x == n:
#     print("2 - ning darajasi")
# else:
#     print("2 - ning darajasi emas")

# Masala 6
# n = int(input("n: "))
# result = 1
# i = n
# while i > 1:
#     result *= i
#     i -= 2
# print(result)

# Masala 7
# n = int(input("n: "))
# k = 1
# while k * k <= n:
#     k += 1
# print(k - 1)

# Masala 8
# n = int(input("n: "))
# k = 1
# while k * k < n:
#     k += 1
# print(k)

# Masala 9
# n = int(input("n: "))
# k = 0
# while 3  k <= n:
#     k += 1
# print(k)

# Masala 10
# n = int(input("n: "))
# k = 0
# while 3  k < n:
#     k += 1
# print(k)

# Masala 11
# n = int(input("n: "))
# k = 0
# sum_ = 0
# while sum_ < n:
#     k += 1
#     sum_ += k
# print(k, sum_)

# Masala 12
# n = int(input("n: "))
# k = 0
# sum_ = 0
# while sum_ + k + 1 <= n:
#     k += 1
#     sum_ += k
# print(k, sum_)

# Masala 13
# a = float(input("a: "))
# sum_ = 0.0
# k = 0
# while sum_ < a:
#     k += 1
#     sum_ += 1 / k
# print(k, sum_)

# Masala 14
# a = float(input("a: "))
# sum_ = 0.0
# k = 0
# while sum_ + 1 / (k + 1) <= a:
#     k += 1
#     sum_ += 1 / k
# print(k, sum_)



# ------------------------------------------------------------1-----------------------------------------

# a = int(input("birinshi sonni kiriting :"))
# b = int(input("ekiinchi sonni kiriting :"))

# s = 0
# i = 1

# while i < a:
#     if a % i == 0:
#         s += i
#     i += 1
# print(s)

# s2 = 0
# i2 = 1

# while i2 < b:
#     if b % i2 == 0:
#         s2 += i2
#     i2 += 1
# print(s2)


# print(s == b and s2 == a)

# i = 1
# s = 0 

# while i :
# 	n = int(input(" sonni kiriting :"))
# 	if n != 0:
# 			s+=n
# 	elif n == 0:
# 		i = 0

# print(s)



# ------------------------------ for bilan isim chiqarish  --------------------------------

# col = int(input("col : "))
# row = int(input("row : "))

# -----------------------------------A--------------------------------------

# for i in range(1, col + 1):
# 	for j in range(1, row  + 1 ):
# 		if(
# 			(j == 1 and i != 1 or
# 			i == row // 2+1
# 			or j == col and i != 1 )
# 			or (i == 1 and j !=1 )
# 			and (i == 1 and j != col)
# 		 ) :
# 			print("*" ,end=" ")
# 		else:
# 			print(" ", end=" ")
# 	print()
 
# print()
# print()

# -----------------------------B------------------------------------

# for i in range(1, col + 1):
# 	for j in range(1, row  + 1 ):
# 		if(
#       (j == col and i != 1 and  j == col and i != row)  or 
#       (i == row // 2 +1 or j == 1)	or
# 		  (i == 1 and j != col or i == row and j != col) 

# ) :
# 			print("*" ,end=" ")
# 		else:
# 			print(" ", end=" ")
# 	print()

# print()
# print()

#  -------------------------------D--------------------------------

# for i in range(1, col + 1):
# 	for j in range(1, row + 1):
# 		if (
			
#       (j == col and i != 1 and  j == col and i != row)  or 
# 		  (i == 1 and j != col or i == row and j != col or j == 1) 
# 		):
# 			print("*", end=' ')
# 		else:
# 			print(" ", end=" ")
# 	print()

# print()
# print()

# ------------------------------------U-----------------------------

# for i in range(1, col + 1):
# 	for j in range(1, row + 1):
# 		if (
# 			(i == col and j != 1 and i == col and j != col) 
# 			or
# 			(j == 1 and i!= 5 or j == row and i != col) 
# 		):
# 			print("*", end=" ")
# 		else: 
# 			print(" ", end=" ")
# 	print()


# print()
# print()

# --------------------------------L--------------------------------


# for i in range(1, col + 1):
# 	for j in range(1, row + 1):
# 		if (i == col or j == 1
# 		):
# 			print("*", end=" ")
# 		else: 
# 			print(" ", end=" ")
# 	print()


# print()
# print()

# --------------------------------------H----------------------------


# for i in range(1, col + 1):
# 	for j in range(1, row + 1):
# 		if (
#       (j == 1 or j== row)	or
# 				 (i == row // 2 +1 or j == 1)		
# 			):
# 			print("*", end=" ")
# 		else: 
# 			print(" ", end=" ")
# 	print()

# print()
# print()

# ------------------------------------A----------------------------------

# for i in range(1, col + 1):
# 	for j in range(1, row  + 1 ):
# 		if(
# 			(j == 1 and i != 1 or	i == row // 2+1 or j == col and i != 1 )
# 			or (i == 1 and j !=1 )
# 			and (i == 1 and j != col)
# 		 ) :
# 			print("*" ,end=" ")
# 		else:
# 			print(" ", end=" ")
# 	print()

# print()
# print()


# -----------------------------Q-----------------------------


# for i in range(1, col + 1):
# 	for j in range(1, row + 1):
# 		if (
# 			(i == col and j != 1) and (i == col and j != col) 
# 			or 
# 			(i == 1 and j !=1 ) and (i == 1 and j != col) 
# 			or 
# 			(j == 1 and  i != col and j == 1 and  i != 1) 
# 			or 
# 			(j == 1 and  i != col and j == 1 and  i != 1) 
# 			or
# 			(j == col and i != 1 )  or
# 			(j == col -1 and i == col -1) 
# 			or
# 			(j == col -2 and i == col -2)
# 		):
# 			print("*", end=" ")
# 		else: 
# 			print(" ", end=" ")
# 	print()


# print()
# print()

 
  

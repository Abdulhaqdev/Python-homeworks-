# a = int(input("sonni kiriting :"))
# summa = ''

# while a >= 1 :
# 	q = a % 2
# 	summa = str(q) + summa
# 	a //= 2

# print(summa)


# mevalar = ["olma", "banan",  "behi", "limon" "glos"]

# for meva in mevalar :
# 	print(meva)


# str = "hello world"

# for harf in str:
# 	print(harf)




# for i in range(1, 20, 2) :
# 	print(i)



# sum = int(input("1kg summasi :"))

# for i in range(0,101,1):
# 	print(i * sum)
	

# x = [10,21,31,64,61,29]

# newlist = []

# for i in x :
# 	newlist.append(i % 10 + i // 10 )

# print(newlist)



# x = [1, 2, 3, 33, 8, 58, 37, 16, 9, 12, 4]
# y = []


# for i in range(0,len(x) - 1): 
#     y.append(x[i] + x[i + 1])  
    
# print(y)

# for i in range(0,len(x) - 1): 
# 	if x[i] > 9 and x[i] < 99 :
# 		y.append( x[i] % 10 + x[i] // 10 )
		
# print(y)

# x = ['olma', 'limon', 'banan', 'anor']

# for i in range(len(x)): 
#  		y.append(len(x[i])  )
		
# print(y)
 

#  -----------------------


# x = [1, 2, 3, 33, 8, 58, 37, 16, 9, 12]
# y = []

# for i in range(0,len(x) // 2): 
# 	y.append(x[i] + x[len(x) - 1 -i])
		
# print(y)


# for i in range(3,100,3):
# 		if i % 3 == 0 :
# 			continue
# 		print(i)

# ----------------------------------------------

# for i in range(-100,100,1):
# 		if i > -10 or i < 9  :
# 			continue
# 		print(i)

# ----------------------------------------------


# i = 1


# while i <= 10 :
# 	if i == 5 :
# 		i += 1
# 		continue
# 	print(i)
# 	i += 1

# ------------------

# son = int(input("sonni kiriting : "))
# sanoq = 0


# for i in range(1, son,1):
# 	if son % 


# letters = {'d', 's', 'e', 'a','o'}
# letters.add('q')
# print(letters)

# number1 = {1,2,3,4}
# number2 = {3,4,5,6}

# testUnion =number1.union(number2)

# print(testUnion)


# password  ={ 
# 	'ali': 1234,
# 	'babur': 4323,
# 	'nodir': '213ere',
# 	'sardor': 123456778,
# 	'elyor': " "	
# }


# c = password.copy()

# password.clear()


# print(password)
# print(c)


# matrix = [
# 	[1,23,32,45,90,19],
# 	[12,-3,29,57,0,-1],
# 	[-9,32,3,52,15,9],
# ]

# for i in range(0,3):
# 	max = matrix[i][0]
# 	for j in range(0,len(matrix[i])):
# 		print(f'{matrix[i][j]:2}', end=" ")
# 		if max <  matrix[i][j]:
# 			max = matrix[i][j]
# 	print(f'kattasi : {max}')

# row = int(input("row: "))
# col = int(input("col: "))
# for i in range(1, row+1):
#     for j in range(1, col+1):
#         if (
#             i == j or i + j == col+1
#         ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


col = int(input("col : "))
row = int(input("row : "))


# -----------------------------------A--------------------------------------

for i in range(1, col + 1):
	for j in range(1, row  + 1 ):
		if(
			(j == 1 and i != 1 or
			i == row // 2+1
			or j == col and i != 1 )
			or (i == 1 and j !=1 )
			and (i == 1 and j != col)
		 ) :
			print("*" ,end=" ")
		else:
			print(" ", end=" ")
	print()
 
print()
print()

# -----------------------------B------------------------------------

for i in range(1, col + 1):
	for j in range(1, row  + 1 ):
		if(
      (j == col and i != 1 and  j == col and i != row)  or 
      (i == row // 2 +1 or j == 1)	or
		  (i == 1 and j != col or i == row and j != col) 

) :
			print("*" ,end=" ")
		else:
			print(" ", end=" ")
	print()

print()
print()

#  -------------------------------D--------------------------------

for i in range(1, col + 1):
	for j in range(1, row + 1):
		if (
			
      (j == col and i != 1 and  j == col and i != row)  or 
		  (i == 1 and j != col or i == row and j != col or j == 1) 
		):
			print("*", end=' ')
		else:
			print(" ", end=" ")
	print()

print()
print()

# ------------------------------------U-----------------------------

for i in range(1, col + 1):
	for j in range(1, row + 1):
		if (
			(i == col and j != 1 and i == col and j != col) 
			or
			(j == 1 and i!= 5 or j == row and i != col) 
		):
			print("*", end=" ")
		else: 
			print(" ", end=" ")
	print()


print()
print()

# --------------------------------L--------------------------------


for i in range(1, col + 1):
	for j in range(1, row + 1):
		if (i == col or j == 1
		):
			print("*", end=" ")
		else: 
			print(" ", end=" ")
	print()


print()
print()

# --------------------------------------H----------------------------


for i in range(1, col + 1):
	for j in range(1, row + 1):
		if (
      (j == 1 or j== row)	or
				 (i == row // 2 +1 or j == 1)		
			):
			print("*", end=" ")
		else: 
			print(" ", end=" ")
	print()

print()
print()

# ------------------------------------A----------------------------------

for i in range(1, col + 1):
	for j in range(1, row  + 1 ):
		if(
			(j == 1 and i != 1 or	i == row // 2+1 or j == col and i != 1 )
			or (i == 1 and j !=1 )
			and (i == 1 and j != col)
		 ) :
			print("*" ,end=" ")
		else:
			print(" ", end=" ")
	print()

print()
print()


# -----------------------------Q-----------------------------
for i in range(1, col + 1):
	for j in range(1, row + 1):
		if (
			(i == col and j != 1) and (i == col and j != col) 
			or 
			(i == 1 and j !=1 ) and (i == 1 and j != col) 
			or 
			(j == 1 and  i != col and j == 1 and  i != 1) 
			or 
			(j == 1 and  i != col and j == 1 and  i != 1) 
			or
			(j == col and i != 1 )  or
			(j == col -1 and i == col -1) 
			or
			(j == col -2 and i == col -2)
		):
			print("*", end=" ")
		else: 
			print(" ", end=" ")
	print()


print()
print()


# p = [
# 	[0,0,0,0,0,0,0,0,0,0],
# 	[0,0,0,0,0,0,0,0,0,0],
# 	[0,0,0,0,0,0,0,0,0,0],
# 	[0,0,0,0,0,0,0,0,0,0],
# 	[0,0,0,0,0,0,0,0,0,0],
# 	[0,0,0,0,0,0,0,0,0,0],
# 	[0,0,0,0,0,0,0,0,0,0],
# 	[0,0,0,0,0,0,0,0,0,0],
# 	[0,0,0,0,0,0,0,0,0,0],
# 	[0,0,0,0,0,0,0,0,0,0],
# ]
# print(p)
# while True :
# 	row = int(input('row: '))
# 	col = int(input('col: '))
# 	car_name = input('car name: ')
	
	

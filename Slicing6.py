

"""input=["python","django",[1,2,3,4,(5,8,3,"DON","KING"),"don","king"],7,9,10]
				output=1
				output=DON (-)
				output=KING (-)
				output=ing  (+)
				output=ON (+)(-)
				output=8 (+)(-)
				output=N (+)(-)  "first occerence)
				output=k (+)(-)"""

i=["python","django",[1,2,3,4,(5,8,3,"DON","KING"),"don","king"],7,9,10]
print(i[2][0])

print(i[-4][-3][-2])

print(i[-4][-3][-1])

print(i[2][6][1::1])

print(i[2][4][3][1::1])

print(i[-4][-3][-2][-2::1])
print(i[2][4][1])

print(i[-4][-3][-4])

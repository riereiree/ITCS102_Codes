money = int(input("Enter amount to DEPOSIT -> "))
#computation here
b = 1000
c = 500
e = 200
g = 100
i = 50
j = 20
k = 10
l = 5
n = 1

thousand = money // 1000
five_hund = (money % 1000) // 500
two_hund = (money % 1000 % 500) // 200
one_hund = (money % 1000 % 500 % 200) // 100
fifty = (money % 1000 % 500 % 200 % 100) // 50
twenty = (money % 1000 % 500 % 200 % 100 % 50) // 20
ten = (money % 1000 % 500 % 200 % 100 % 50 % 20) // 10
five = (money % 1000 % 500 % 200 % 100 % 50 % 20 % 10) // 5
one = (money % 1000 % 500 % 200 % 100 % 50 % 20 % 10 % 5) // 1

#prints here
print(b, "1000 = ",thousand)
print(c, " 500 = ",five_hund)
print(e, " 200 = ",two_hund)
print(g, " 100 = ",one_hund)
print(i, "  50 = ",fifty)
print(j, "  20 = ",twenty)
print(k, "  10 = ",ten)
print(l, "   5 = ",five)
print(n, "   1 = ",one)
print("The total money deposited are",money)

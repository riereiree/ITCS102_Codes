money = int(input("Enter amount to DEPOSIT -> "))

#computation here

thousand = money // 1000
thousand_rem = money % 1000

five_hund = thousand_rem // 500
five_hund_rem = thousand_rem % 500

two_hund = five_hund_rem // 200
two_hund_rem = five_hund_rem % 200

one_hund = two_hund_rem // 100
one_hund_rem = two_hund_rem % 100

fifty = one_hund_rem // 50
fifty_rem = one_hund_rem % 50

twenty = fifty_rem // 20
twenty_rem = fifty_rem % 20

ten = twenty_rem // 10
ten_rem = twenty_rem % 10

five = ten_rem // 5
one = ten_rem % 5

#prints here
print("1000 = ",thousand)
print(" 500 = ",five_hund)
print(" 200 = ",two_hund)
print(" 100 = ",one_hund)
print("  50 = ",fifty)
print("  20 = ",twenty)
print("  10 = ",ten)
print("   5 = ",five)
print("   1 = ",one)
print("The total money deposited are",money)

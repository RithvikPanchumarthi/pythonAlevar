list_of_num = [1,2,4,5]

a = list_of_num[2]
b = list_of_num[-1]
c = list_of_num[:3]
d = list_of_num[2:]


print(a)
print(b)
print(c)
print(d)
print(type(a))


alphabet_list = ["A","B","J","D","E"]

for alphabet in alphabet_list:
    print(alphabet)
    if alphabet == "B":
        break


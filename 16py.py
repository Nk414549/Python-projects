shopping_list = ["drinks","chocolate","fruits","biscuit","bread","vegetable","icecream"]
print(shopping_list[4])
print(shopping_list[6])
print(shopping_list[0])
shopping_list.append("pizza")
shopping_list.append("pancakes")
print(shopping_list)


name = []
while True:
    n = input ("please input a name:")
    if n in name:
        print(n, "is the in the list already")
    else:
        name.append(n)
        print(name)

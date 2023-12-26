# all_low = "all are lower case"
#
# print(all_low.split(" "))
# print(all_low.upper())
#
# print("Batman rty".istitle())
# print("This is a".startswith("T"))
#
# print("...".join(["one", "two"]))
#
#
# print("hello world".strip())
# print("blueblueyellowblue".strip("eulb"))
#
# print("Good morning".replace("morning", "afternoon"))
#
# print(len("tree is life"))

#print(len(input("enter a string")))

# str_ent = input("enter a string")
# rev_str = ""
# str_len = len(str_ent)-1
# for item in range(str_len, -1, -1):
#     #print(str_ent[str_len-1])
#     print(str_ent[item])
#     rev_str += str_ent[item]
# print(rev_str)

# str_1 = "This is a super string"
# print(str_1.split(" "))
# counter = 0
# for item in range(len(str_1.split(" "))):
#     # print(item)
#     counter += 1
# print(counter)

str_2 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."
spaces_and_letters = ""

# this for loop reduces the string to letters, numbers, and spaces
for char in str_2:
    if char.isalnum() or char.isspace() or char == "-" or char == "'":
        spaces_and_letters += char
print(spaces_and_letters)
# .split() is used to put the words the into a list
words = spaces_and_letters.split()
number_of_words = len(words)

# print(words)
# print(number_of_words)

name = "abc"
exp = "7 years"
print("{} has {} years of exp".format(name, exp))
# Q5. how to update word in string ?


# string = "jai prakash"
# string[0] = "p"
# print(string)  # error


# concept 1
# string = immutable (we cannot update its value)


# string = "jai prakash"
# string = "pai prakash"
# print(string)


# string = "my name is jai"
# l1 = string.split()
# print(l1)
# word = "name"
# updatedValue = "firstName"
# if word in l1:
#     index = l1.index(word)
#     l1[index] = updatedValue
#     l1 = " ".join(l1)
# print(l1)


# l1 = ["jai", "prakash"]
# l1 = "".join(l1)
# print(l1)


def updatedWord(string, word, update):
    l1 = string.split()
    if word in l1:
        index = l1.index(word)
        print(f"{word} found at {index+1} position ")
        l1[index] = update
        string = " ".join(l1)
        print("Updated string")
        print(string)
    else:
        print(f"word not found")


string = "I Love Python"
word = "Python"
update = "javascript"
updatedWord(string, word, update)

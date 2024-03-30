# num = 1
#
# while num <= 5:
#     print('*' * num)
#     num += 1
# print("Done")


secret = 7
i = 0

while i < 3:
    user_number = int(input("Guess the number between 0 to 9 "))
    i += 1
    if user_number == secret:
        print("You Won!")
        break
else:
    print("Sorry, You Failed!")

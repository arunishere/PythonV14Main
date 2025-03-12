
# Question No.18

# list_1 = [1,2,3,4,5,6,7,8]
# list_2 = [9,10,11,12,13,14,15,16]
# final_list = []
# for i in range(0,7):
#     if i % 2 == 0:
#         final_list.append(list_1[i])
#     else:
#         final_list.append(list_2[i])
# print(final_list)


# letters = ["X", "A", "B", "Q", "P"]

# for idx, alphabet in enumerate(letters):
#     print(idx, alphabet)


# Question No.21

letter_number = {
                0: "Zero",
                1: "One",
                 2: "Two",
                 3: "Three",
                 4: "Four",
                 5: "Five",
                 6: "Six",
                 7: "Seven",
                 8: "Eight",
                 9: "Nine"
                }
# 89 - > "eight nine"
user_number_input = input("Enter the number: ")
#567

word_list = []
for i in user_number_input:
    word_list.append(letter_number[int(i)])
print(word_list)





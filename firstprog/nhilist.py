def polybiusCipher(s):
    for i in s:
        row = int((a.index(i)/ 8)+1)
        col = ((a.index(i) % 8) + 1)
        print(row, col, end='', sep='')
# if __name__ == "__main__":
a=[]
for i in range(48,58):
    a.append(chr(i))
for i in range(65,91):
    a.append(chr(i))
for i in range(97,123):
    a.append(chr(i))
a.append(chr(32))
a.append(chr(44))
s='g'
# s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,"
polybiusCipher(s)




# def decod(z):
#     y=str(z)
#     d=[ int(y[i:i+2]) for i in range(0, len(y), 2) ]
#     print(d)





# def polybiusCipher(s):
#     # convert each character to its encrypted code
#     for char in s:
#
#         # finding row of the table
#         row = int((ord(char) - ord('a')) / 5) + 1
#
#         # finding column of the table
#         col = ((ord(char) - ord('a')) % 5) + 1
#
#         # if character is 'k'
#         if char == 'k':
#             row = row - 1
#             col = 5 - col + 1
#
#         # if character is greater than 'j'
#         elif ord(char) >= ord('j'):
#             if col == 1:
#                 col = 6
#                 row = row - 1
#
#             col = col - 1
#
#         print(row, col, end='', sep='')
#
#
# # Driver's Code
# if __name__ == "__main__":
#     s = "geeksforgeeks"
#
#     # print the cipher of "geeksforgeeks"
#     polybiusCipher(s)

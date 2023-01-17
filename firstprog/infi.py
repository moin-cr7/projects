# # def funn(str):
# #     strn=str
# #     print(strn)
# #     print("hello")
# #     return
# #
# # ff=funn("world")
# # print(ff)
# # aa=[1,2,3,'a']
# # bb=[2,3,4,'s']
# # print(aa[2]+bb[2])
# # print(aa)
# # print(aa[3])
# # print(type(aa))
#
# # import keyword
# # a=keyword.kwlist
# # for i in a:
# #     print(i)
# #
#
# # a={'a','1','s'}
# # print(type(a))
#
# # x=0
# # i=0
# # while i<4:
# #     x+=i
# #     i+=1
# #     print(x)
# #
# # print(x)
#
# def fun(x):
#     r=0
#     for i in range(x):
#
#         r+=i
#         print(r)
# print(fun(4))

#patterns
# row=5
# col=10
# for i in range (1,row+1):
#     for j in range(1,col+1):
#         if(i==1 or j==1 or i==row or j==col):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

# row=5
# col=4
# count=0
# for i in range(row):
#     for j in range(i+1):
#         count=count+1
#         print(count,end="")
#     print()

row=5
col=4
for i in range(1,row):
    for j in range(1,col):
        print("*",end="")
        print()
    print()
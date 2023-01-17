# class starr:
#
#     def tristar(self):
#         print("enter the number of rows")
#         row=int(input())
#         for i in range(row):
#             print(" "*(row-i)+" *"*(i))
#     def parlstar(self):
#         print("Enter the number of rows")
#         rowss=int(input())
#         for o in range(rowss):
#             print(" "*(rowss-o)+" *"*(rowss))
#
# pyramid=starr()
# pyramid.tristar()
# pyramid.parlstar()

# def tristar():
#     print("enter the number of rows")
#     row=int(input())
#     for i in range(row):
#         drw=(" "*(row-i)+" *"*(i))
#         print(drw)
#
# def parlstar():
#     print("Enter the number of rows")
#     rowss = int(input())
#     for o in range(rowss):
#         draw=(" " * (rowss - o) + " *" * (rowss))
#         print(draw)
# # pyramid=starr()
# print(tristar())
# print(parlstar())

# class shape:
# print("Enter the number of terms i n fibinique sequence")
# n=int(input())
# a=0
# b=1
# print(a)
# print(b)
# for i in range (n):
#     c=a+b
#     print(c)
#     a=b
#     b=c

# def fibb(n):/


# fp=open("fii.txt","w")
#
# fp.write("hello world")
# fp.close()
# n=int (input())
# su=0
# for i in range(1,n+1):
#     su=su+i
#     i+=1
# print(su)
# def search(text,word):
#     if (text.find(word)!=-1):
#
#         return("found")
#     else:
#         return("not found")
# text="i won the game"
# word='gamre'
# print(search(text,word))

# t="i won the game"
# s=t.split(" ")
# word='game'
# print(s)
# for words in s:
#     if(word==words):
#         print("y")
#     else:
#         print("n")
# z= list(range(10))
# l = list(map(lambda x:x*x, z))
# print(l)
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# # ans = [[i, j, k] for i in range(x + 1) for j in range(y+ 1) for k in range(z + 1) if (i + j + k) != n]
# ans=[]
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if(i+j+k != n):
#                 ans.append([i,j,k])
# print(ans)
# arr,df,f,g,h = list(map(int,input().split()))
# print(arr,df)
# for i in range(1,10):
#     a.append(i)
# a.remove(8)
# print(a)
from collections import Counter
# a="give me one grand today night"
# b="give one grand today"
# print(Counter(a))
# print(Counter(b))
# if(Counter(b)-Counter(a)=={}):
#     print("Yes")
score_list=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    score_list.append([name, score])
print(score_list)
second_highest = sorted(set([score for name ,score in score_list]))[-2]
print(second_highest)
print('\n'.join(sorted([name for name, score in score_list if score == second_highest])))
# a=[545,55,5,5,55,56,4,2,45,1,8,2,47,4341,4,354,341,34,31]
# print(x:=sorted(set(a))[-1])

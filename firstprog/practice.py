#
# p=float(input("Enter the principle ammount"))
# R=float(input("Enter the rate of interst"))
# t=int(input("Enter the time period"))
# n=float(input("Enter the time as quterly(4) , half yearely(2) ,yearly(1)"))
# tottal_ammount=0
# r=R/100
# a=int(input("enter simple intrest(1) or compound interst(2)"))
# if(a==1):
#     for t in range(1,t+1):
#         tottal_ammount=p*(1+(r/n))**(n*t)
#     print(float(tottal_ammount))
#     ci=tottal_ammount-p
#     print(ci)
#
# elif(a==2):
#     si = 0
#     si = (p * r * t)
#     print(si)
# else:
#     for t in range(1,t+1):
#         tottal_ammount=p*(1+(r/n))**(n*t)
#     print(float(tottal_ammount))
#     ci=tottal_ammount-p
#     print(ci)
#     si = 0
#     si = (p * r * t)
#     print(si)

# n=int(input("enter the 3 digit number"))
# sum=0
# while(n!=0):
#     x=(n%10)
#     sum=sum+x
#     n=(n//10)
# print(sum)

# n=int(input("enter  the number "))
# x=1
# for i in range(1,n+1):
#     x=i*x
#     i=i+1
# print(x)

# l=int(input("enter  the number "))
# u=int(input("enter  the number "))
# for n in range(l,u+1):
#     if n>1 :
#         for i in range(2,n):
#             if(n%i==0):
#                 break
#         else:
#             print(n)
#     else:
#         print(1)



# yr=int(input("Enter the yr"))
# if((yr%4)==0 and (yr%100)!=0 or (yr%400)==0):
#     print("leap year")
# else:
#     print("not a leap year")



# a=[]
# n=6
# m=3
# i=3
# sum=0
# # x=a[i]
# for w in range(n):
#     a.append(int(input()))
# print(a)

# n= 6
# i=  3
# m= 4
# d= [6,7,5,3,9,4]
# aa=[]
# # for _ in range(n):
# #     d.append(int(input()))
# for i in range(i-1,i+1):
#     aa.append(sum(d[i:i+m]))
#     print(aa)

# import numpy as np
# a=np.array([[1,2,3,],[4,5,6]])
# print(a)

# def woo(*aa,**ff):
#     b=aa
#     c=ff
#     print(c)
#     print(b)
# woo("jii",5,"gpoo",a=6)


# def biggest(a,b,c):
#     if(a>b and a>c):
#         print(a)
#     elif(b>a and b>c):
#         print(b)
#     else:
#         print(c)
# x,y,z=input().split()
# biggest(x,y,z)

# biggest(x,y,z)

# def cube(x):
#     print(x*x*x)
# a=int(input())
# cube(a)

# def fac(x):
#     fac=1
#     if(x==0):
#         print(0)
#     else:
#         for i in range(1,x+1):
#             fac=fac*i
#         print(fac)
# a=int(input())
# fac(a)

# a=18
# b=24
# print(a%b)
# print(18%24)
# print(b%a)
# print(24%18)
# a=str("dfvdgvfbh")
# print(a[1:3])
# b=[]
# for i in str(a):
#     b.append(i)
# b.reverse()
# print(b)
# for i in b:
#     print(i,end="")
# a=int(input("enter the number"))
# print(a)
# t=a
# r=0
# while(t>0):
#     d=t%10
#     r=(r*10)+d
#     t=t//10
# print(r)
# if(a==r):
#     print("it is palindrome")
# else:
#     print("not a palindrome")
#

# a="Python1Hub"
# x=a.isalpha()
# print(x)

# a=[30,70,20,50,40,80]
# temp=0
# for i in range(len(a)):
#     while(i>=1):
#         if(a[i]<a[i-1]):
#             temp=a[i]
#             a[i]=a[i-1]
#             a[i-1]=temp
#         i-=1
# print(a)
# a=[30,70,20,50,40,80]
# a.sort(reverse=True)
# print(a)

# a=[7,18]
# c=0
# b=[9,-13,8,-7,-8,18,10]
# for i in b:
#     if(a[1]%i==0):
#         c+=1
# print(c)

# a=[11,10]
# b=[1,1,2,3,4,5,5,7,6,9,10]
# c=[11,12,13,4,5,6,7,18,19,20]
# d=[]
# for i in b:
#     if i not in c:
#         d.append(i)
# for i in c:
#     if i not in b:
#         d.append(i)
# print(len(d))

# a=int(input("Enter thr number atleast of 2 digit"))
# c=0
# while(a!=0):
#     r=a%10
#     c=c*10+r
#     a=a//10
# print(c)

# a,b=2,5
# print(b/a,b//a)

# n=int(input("enter the numbr"))
# fac=1
# if (n==0):
#     print(1)
# elif(n==1):
#     print(1)
# else:
#     for i in range(1,n+1):
#         fac=fac*i
#         print(fac,end="\n")

# a=1
# b=++a+ ++a+++a+a+
# +
# str="45345434"
# a=list(str)
# print(a)
# # x=int(str)
# # print(x)
# c=0
# for i in a:
#     if(int(i)==4):
#         c+=1
# print(c)
# n=int(input("enter tne number"))
# temp=n
# c=0
# while(n>0):
#     r=temp%10
#     c=c*10+r
#     temp=temp//10
# print(c)
# if(c==n):
#     print("palindronme")
# else:
#     print("not")
# yr=int(input("Enter the yr"))
# if((yr%4)==0 and (yr%100)!=0 or (yr%400)==0):
#     print("leap year")
# else:
#     print("not a leap year")
# a=int(input("enteer numbr"))
# t=a
# c=0
# while(t>0):
#     r=t%10
#     c=(c*10)+r
#     t=t//10
# print(c)
# n=int(input())
# a=list(map(int,str(n
# d=0
# for i in a:
#     d=(i**3)+d
# print(d)


def find_gcd(x, y):
    while (y):
        x, y = y, x % y

    return x


a = int(input())
b = []
for _ in range(a):
    b.append(int(input()))

num1 = b[0]

num2 = b[1]

gcd = find_gcd(num1, num2)

for i in range(2, a):

    gcd = find_gcd(gcd, b[i])

print(gcd)

# x=2
# y=2
# z=3
# n=5
# ans=[[i,j,k] for i in range (x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)==n]
# print(ans)
def fun(z):
    return z%2
a=[1,4,2,6,2,7,3,4]
b=sorted(sorted(a,key=fun,reverse=False),reverse=False)
print(b)
print(max(b))
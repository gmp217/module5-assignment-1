n = int(input("enter a n value:"))
d,s= {},0
for i in range(n):
    print('Enter key:')
    keys = input()
    print('Enter value:')
    values = int(input())
    d[keys] = values
print(d)
for i in d:
	s+=d[i]
print('sum=',s)
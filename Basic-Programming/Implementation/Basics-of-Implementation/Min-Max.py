n = int(input())
arr = [int(x) for x in input().split(' ')]
flag = True
for i in range(min(arr),max(arr)+1):
	if i not in arr:
		flag = False
		break
print('YES') if flag else print('NO')
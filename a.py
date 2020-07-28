a=[12,31,22,11,14,55,23,19]
for i in range(len(a)-1):
	for j in range(len(a)-1):
		if a[j]>a[j+1]:
			a[j],a[j+1]=a[j+1],a[j]
print(a)
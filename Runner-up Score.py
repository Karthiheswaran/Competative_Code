if __name__ == '__main__':
	n = int(input())
	arr = map(int, input().split())
	mylist = list(set(arr))
	mylist.sort()
	print(mylist[-2])

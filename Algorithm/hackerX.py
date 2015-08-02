def main():
		n = int(raw_input())
		missiles = [map(int,raw_input().split()) for _ in xrange(n)]
		mapped = map(lambda a: (a[0]+a[1],a[0]-a[1]),missiles)
		lordered = sorted(mapped,compSecond,reverse=False)
		print PlainSweep(lordered)+1

# arr sorted in ascending y
def PlainSweep(arr):
		n = len(arr)
		k = 0
		for i in xrange(1,n):
				if X(arr[i]) < X(arr[k]):
						k+=1
						arr[k], arr[i] = arr[i], arr[k]
				else:
						pos = binSearch(arr,arr[i],0,k)
						arr[pos], arr[i] = arr[i], arr[pos]
		return k

def X((a,b)):
		return a
def Y((a,b)):
		return b

def binSearch(arr,p,i,j):
		if i == j:
				return i
		mid = (j-i)/2 + i
		if X(arr[mid]) == X(p):
				return mid
		elif X(arr[mid]) > X(p):
				return binSearch(arr,p,mid+1,j)
		else:
				return binSearch(arr,p,i,mid)

def compSecond(a,b):
		return cmp(Y(a),Y(b))

if __name__ == "__main__":
		main()

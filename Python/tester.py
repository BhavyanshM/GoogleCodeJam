
import sys


def query(a):
	print(a)
	sys.stdout.flush()

def display(s):
	print(str(s),file=sys.stderr)

def calc(b,t,n):
	r = n//t
	total = sum([2^i for i in range(r)])
	return b*(t*() + ((n%t)+1)*2**(r))


T,W = tuple(map(int,input().split()))

rcount = []

for t in range(T):
	factors = []
	if W == 6:
		for i in range(W):
			query(i+1)	

			rcount.append((i,int(input())))



	display(rcount)

	result = " ".join([str(j) for j in range(1,7)])
	query(result)
	display(result)

	judge = int(input())
	display("Answer Result:{}".format(judge))


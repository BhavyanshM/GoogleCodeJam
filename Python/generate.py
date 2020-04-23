import numpy as np

f = open("data.txt", "+w")
T = 10
N = 10
f.write(str(T)+"\n")
for t in range(T):
	f.write(str(N)+"\n")
	for n in range(N):
		f.write("{} {}\n".format(np.random.randint(1440),np.random.randint(1440)))




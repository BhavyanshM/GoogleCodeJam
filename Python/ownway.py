


for t in range(int(input())):
	print("Works")





########################################################################################################



# import sys

# def getDec(B,offset):
# 	data = ""
# 	for i in range(offset,offset+B):
# 		req = str(i+1)
# 		# print("{},{}: Request:{}".format(t,i,req),file=sys.stderr)
# 		print(req)
# 		sys.stdout.flush()
# 		s = input()
# 		# print("{},{}: Response:{}".format(t,i,s),file=sys.stderr)

# 		r = s
# 		data += r
# 	return data

# def complement(data):
# 	s = list(data)
# 	for i in range(len(data)):
# 		if s[i] == "1":
# 			s[i] = "0"
# 		elif s[i] == "0":
# 			s[i] = "1"
# 	return "".join(s)


# if __name__ == "__main__":
# 	s = input().split()
# 	T,B = int(s[0]),int(s[1])

# 	res = ""
# 	state = 0 

# 	done = False
# 	for t in range(T):
# 		data = ""
# 		# print("TEST_CASE:",t,file=sys.stderr)
# 		if done==True:
# 			break

# 		if B == 10:
# 			for i in range(B):
# 				req = str(i+1)
# 				# print("{},{}: Request:{}".format(t,i,req),file=sys.stderr)
# 				print(req)
# 				sys.stdout.flush()
# 				s = input()
# 				# print("{},{}: Response:{}".format(t,i,s),file=sys.stderr)

# 				r = s
# 				data += r

# 		if B == 20:
# 			print("{},{}: Requested".format(B,0),file=sys.stderr)
# 			data10 = getDec(10,0)
# 			data11 = getDec(10,0)

# 			data20 = getDec(10,10)
# 			data21 = getDec(10,10)
# 			print("Response:{},{}".format(data1,complement(data1)),file=sys.stderr)

# 		# print(data,file=sys.stderr)

# 		# print("{}: Answering:{}".format(t,data),file=sys.stderr)
# 		print(data1+data2)
# 		sys.stdout.flush()
# 		last_resp = input()
# 		# print("{}: Answer Response:{}".format(t,last_resp),file=sys.stderr)
# 		if last_resp == "N":
# 			sys.exit()

		# final_resp = input()

		# if final_resp == "N":
		# 	done = True

		# ok = input()
		# print("END {}:{}",t,ok,file=sys.stderr)



####################################################################################################################

# if __name__ == "__main__":
# 	T = int(input())

# 	res = ""
# 	for t in range(T):
# 		final = ""
# 		impossible = False
# 		N = int(input())
# 		person = ["U" for n in range(N)]
# 		queued, running, orig, workers, done = [],[],[],["C","J"],[]
# 		for n in range(N):
# 			s = input().split()
# 			queued.append((int(s[0]),int(s[1]),n,"U"))

# 		queued.sort(key = lambda x: -x[0])

# 		people = 2
# 		start,end = 0,0
# 		freePopRun,freePopStart = True,True
# 		event = False
# 		started,ended = (0,0),(0,0)
# 		JEnds,CEnds = 0,0
# 		JWorking, CWorking = False,False
# 		# print("TIME:{},RUNNING:{},QUEUED:{},DONE:{},WORKERS:{}".format(0,running,queued,done,workers))
# 		for i in range(1441):
# 			while len(running)>0:
# 				if running[-1][1] == i:
# 					event = True
# 					ended = running.pop()

# 					workers.append(ended[3])
# 					done.append(ended)

# 					people += 1
# 					# print(" END ",end=" ")
# 				else:
# 					break

# 			while len(queued)>0:
# 				if queued[-1][0] == i:
# 					event = True
# 					started = queued.pop()

# 					if len(workers) > 0:
# 						worker = workers.pop()
# 						started = (started[0], started[1], started[2], worker)
# 						running.append(started)
# 						running.sort(key = lambda x: -x[1])
# 						person[started[2]] = started[3]


# 					people -= 1
# 					# print(" START ",end=" ")
# 				else:
# 					break
			
# 			# if event:
# 			# 	print("TIME:{},RUNNING:{},QUEUED:{},DONE:{},WORKERS:{}".format(i,running,queued,done,workers))
# 			event = False
			
# 			if people < 0:
# 				# print("Time:",i, " IMPOSSIBLE_FOUND")
# 				impossible = True
# 				break





# 		# print()





# 		# for i in range(N):
# 		# 	for j in range(i,N):
# 		# 		if person[i]==person[j] and i!=j and overlap(orig[i],orig[j]):
# 		# 			impossible = True


# 		final = ""
# 		if impossible:
# 			final = "IMPOSSIBLE"
# 		else:
# 			for i in range(N):
# 				final += person[i]



# 		res += "Case #{}: {}".format(t+1,final)
# 		res += "\n"

# 	print(res, end="")

############################################################################################################


# def flip(x):
# 	if x == 1:
# 		return 2
# 	elif x == 2:
# 		return 1


# def overlap(a,b):
# 	if (a[1]>b[0] and a[1]<b[1]) or  (a[0]>b[0] and a[0]<b[1]) or (b[1]>a[0] and b[1]<a[1]) or (b[0]>a[0] and b[0]<a[1]) or (b[0]==a[0] and b[1]==a[1]):
# 		return True
# 	else:
# 		return False


# if __name__ == "__main__":
# 	T = int(input())

# 	res = ""
# 	for t in range(T):
# 		impossible = False
# 		N = int(input())
# 		person = [0 for n in range(N)]
# 		acts = []
# 		for n in range(N):
# 			s = input().split()
# 			acts.append((int(s[0]),int(s[1])))



# 		for i in range(N):
# 			if person[i] == 0:
# 				person[i] = 1
# 			for j in range(i,N):
# 				# print(i,j,person)
# 				if overlap(acts[i],acts[j]) and i!=j:
# 					# print("I,J:Overlap",acts[i],acts[j])
# 					if person[i] == person[j]:
# 						# print("FOUND_IMP:",i,j)
# 						impossible = True
					
# 					if person[j] == 0:
# 						person[j] = flip(person[i])


# 		for i in range(N):
# 			for j in range(i,N):
# 				if person[i]==person[j] and i!=j and overlap(acts[i],acts[j]):
# 					impossible = True


# 		final = ""
# 		if impossible:
# 			final = "IMPOSSIBLE"
# 		else:
# 			for i in range(N):
# 				if person[i] == 1:
# 					final += "J"
# 				elif person[i] == 2:
# 					final += "C"



# 		res += "Case #{}: {}".format(t+1,final)
# 		res += "\n"

# 	print(res, end="")




##################################################################

# if __name__ == "__main__":
# 	T = int(input())

# 	res = ""
# 	for t in range(T):
# 		final = ""
# 		S = input()
# 		op,cl = 0,0
# 		diff = int(S[0])
# 		flag = False
# 		l = ""
# 		debug = []
# 		S = S + "0"
# 		for s in range(len(S)-1):
# 			if diff > 0:
# 				l = "("
# 			elif diff < 0:
# 				l = ")"
# 			final += l*abs(diff) + S[s]
# 			debug.append(diff)
# 			diff = -(int(S[s]) - int(S[s+1]))

# 		final = final + ")"*int(S[len(S)-2])

# 		res += "Case #{}: {}".format(t+1,final)
# 		res += "\n"

# 	print(res)


#####################################################################


# if __name__ == "__main__":
# 	T = int(input())

# 	res = ""
# 	for t in range(T):
# 		N = int(input())
# 		M = [[0 for j in range(N)] for i in range(N)]

		
# 		for i in range(N):
# 			s = input().split()
# 			for j in range(N):
# 				M[i][j] = int(s[j])

# 		# print(M)
# 		k = 0
# 		for i in range(N):
# 			k += M[i][i]

# 		# print(k)
# 		rcnt,ccnt = 0,0 
# 		for i in range(N):
# 			uni = [0 for x in range(N+1)]
# 			for j in range(N):
# 				uni[M[i][j]] += 1
		
# 			rr = 0
# 			for j in range(N):
# 				if uni[M[i][j]] > 1:
# 					rr = 1
# 			if rr == 1:
# 				rcnt += 1

# 			# print(rcnt)

# 		for i in range(N):
# 			uni = [0 for x in range(N+1)]
# 			for j in range(N):
# 				uni[M[j][i]] += 1
		
# 			rr = 0
# 			for j in range(N):
# 				if uni[M[j][i]] > 1:
# 					rr = 1
# 			if rr == 1:
# 				ccnt += 1

# 			# print(ccnt)

# 		res += "Case #{}: {} {} {}".format(t+1,k,rcnt,ccnt)
# 		res += "\n"

# 	print(res)


############################################

# def cost(l):
# 	damage = 0
# 	charge = 1
# 	print(code,1)
# 	for c in l:
# 		if c == 'C':
# 			charge *= 2
# 		if c == 'S':
# 			damage += charge
# 	return damage, charge


# if __name__ == "__main__":
# 	T = int(input())

# 	for t in range(T):
# 		s = input().split()
# 		D = int(s[0])
# 		code = s[1]

# 		while(True):
# 			d,c = cost(code)

# 			if d < D:
# 				break

# 			ci = (code.rfind("C"))
# 			cstr = list(code)
# 			cstr[ci], cstr[ci+1] = cstr[ci+1], cstr[ci]
# 			code = ''.join(cstr)
# 			print(code)





##############################################################################################

# seq = []
# filled = []
# R, C = 0, 0
# done = False

# def hit(ind, r,c):
# 	global done

# 	new_ind = ind+1
# 	filled[r][c] = new_ind
# 	# seq.append((r,c))

# 	if ind == R*C-1:
# 		# print("done")
# 		done = True
# 		return
	
# 	# print(r,c)
# 	# print(filled)

# 	for i in range(R):
# 		for j in range(C):
# 			if (filled[i][j] == 0) and (i != r) and (j != c) and ((i+j) != (r+c)) and ((i-j) != (r-c) and (done == False)):
# 				# print("Going into: ",i,j, seq, done)
# 				hit(new_ind,i,j)
# 				# print(filled)
# 				# print("Came out of: ",i,j, seq, done)
# 				if done == False:
# 					# seq.pop()
# 					filled[i][j] = 0

# if __name__ == "__main__":
# 	T = int(input())

# 	for t in range(T):
# 		s = input().split()
# 		R = int(s[0])
# 		C = int(s[1])


# 		# filled = [[0 for i in range(C)] for j in range(R)] 
# 		# seq = []
# 		# hit(0,0,0)
# 					# print(fi
# 		done = False
# 		for i in range(R):
# 			for j in range(C):
# 				if done == False:
# 					filled = [[0 for i in range(C)] for j in range(R)] 
# 					# seq = []
# 					print("New:",i,j)
# 					hit(0,i,j)
# 		# 			# print(filled)

# 		if done == True:
# 			# print(seq)
# 			print(filled)




#######################################################################################



# if __name__ == "__main__":
# 	T = int(input())
    
# 	for t in range(T):
# 		inp = input().split()
# 		N = int(inp[0])
# 		B = int(inp[1])
# 		F = int(inp[2])

# 		for f in range(F):
# 			arg = "1"*N
# 			print(arg, flush=True)
# 			resp = input()
            
# 		result = "0 "*B
# 		print(result)



########################################################################################








# def gcd(a,b):
# 	# print("GCD", a,b)
# 	x = min(a,b)
# 	y = max(a,b)
# 	if x == 0:
# 		return y
# 	else:
# 		return gcd(x,y % x)

# if __name__ == '__main__':

#     T = int(input())

#     for t in range(T):
#         inp = input().split()
#         N = int(inp[0])
#         L = int(inp[1])

#         nums = []
#         x = []
#         p = input().split()
#         res = ""
#         for l in range(L-1):
#         	a,b = int(p[l]),int(p[l+1])
#         	h = gcd(a,b)
#         	nums.append(h)
#         	if h not in x:
#         		x.append(h)


#        	first = int(int(p[0])/x[0])
#        	last = int(int(p[len(p)-1])/x[len(x)-1])
#         x.append(first)
#         x.append(last)


#         x.sort()

#         alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#         result = ""

#         result += alpha[x.index(first)]
#         for i in nums:
#         	result += alpha[x.index(i)]
#         result += alpha[x.index(last)]

#         res += "Case #" + str(t+1) + ": " + result
#         res += "\n"

#         print(res)


        # print(len(x), x)

        # for c in s:
        # 	if c == 'S':
        # 		res += 'E'
        # 	if c == 'E':
        # 		res += 'S'
        # res += "\n"

        # print(res)





################################################################



# if __name__ == '__main__':

#     T = int(input())

#     for t in range(T):
#         n = int(input().strip())


#         s = input()

#         res = ""
#         res += "Case #" + str(t+1) + ": "
#         for c in s:
#         	if c == 'S':
#         		res += 'E'
#         	if c == 'E':
#         		res += 'S'
#         res += "\n"

#         print(res)
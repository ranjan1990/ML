import random as r
import math as m
import chromosome as c
import sys

def genqList(N,L):
    Ql=[]
    for i in range(N):
	Ql.append(r.random()%0.6)


    return Ql

def cal_best(L):
    m = ''.join(r.choice('0') for _ in range(L))
    for i in range(2**L):
        s = str(bin(i))[2:]
        for j in range(L-len(s)):
            s = "0"+s
        if c.fitness(s) > c.fitness(m):
            m = s

    print "The best Solution: ",m," with a fitness value of ",c.fitness(m)


def gen(iteration):
    M = 10
    p = 0.8
    N = iteration
    L = 15
    qList = genqList(N,L)
    print  qList
    Q0 = c.createSet(M,L)
    s0 = c.getFittest(Q0)
    ctr = 1
    for q in qList:
        Q1 = c.selection(Q0, M)
        Q2 = c.crossOver(Q1, p)
        Q3 = c.mutateSet(Q2,q)
        s1 = c.getFittest(Q3)
        if c.fitness(s1) >= c.fitness(s0):
            Q0 = Q3[:]
            s0 = (s1+".")[:-1]
        else:
            i = r.randint(0,M-1)
            Q3[i] = s0
            Q0 = Q3[:]
        print "fitness= ",c.fitness(s0)
  	print "string=",s0
        ctr += 1
   




gen(int(sys.argv[1]))


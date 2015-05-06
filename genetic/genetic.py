from math import pi
from math import sin
from random import randint



def fitness(x):
	#theta=pi*x/180;
	theta=x
	if(x>=0 and x<=2*pi):
		return sin(theta)+6
	elif(x<=4*pi):
		return 2*sin(theta)+6
	elif(x<=6*pi):
		return 3*sin(theta)+6
	elif(x<=8*pi):
		return 4*sin(theta)+6
	elif(x<=10*pi):
		return 5*sin(theta)+6
	elif(x<=32):
		return 6*sin(theta)+6
	

		

def g(s1):	#return the value of the string
	s=0.0;
	for i in range(15,0,-1):
		co=pow(2.0,5-i);
		s=s+(s1&1)*co;
		s1=s1>>1;
	return(s);

def return_random_cromosome(L,M):	#length L and 	no of cromosome =M

	r=pow(2,L+1);
	A=[];
	for i in range(M):
		x=randint(0,r)
		A.append(x);
	return(A);


def selection(F):		#F=[(value,fitness),...] return= array after seletoin process
	FIT=[];
	s=0;
	for i in range(len(F)):
		s=s+F[i][1];
		FIT.append(s)
	N_F=[];
	for i in range(len(F)):
		x=randint(0,int(s))
		
		for i in range(len(F)):
			if(x<FIT[i]):
				N_F.append(F[i])
				break;
	

	def getkey(item):
		return(item[1])
	N_F=sorted(N_F,key=getkey,reverse=True);
	return(N_F);


def gen_all_fitness(A):
	F=[]
	for i in range(len(A)):
		F.append((A[i],fitness(g(A[i]))));
	return(F);




def crossover(F,p):
	i=randint(0,len(F)-1)
	j=randint(0,len(F)-1)

		
	t1=F[i][0];
	t2=F[j][0];

	a1=t1>>8;
	a1=a1<<8;
	b1=0x00FF&t2;
	tx1=a1|b1;
	
	a1=t2>>8;
	a1=a1<<8;
	b1=0x00FF&t1;
	tx2=a1|b1;
	
	F[i]=(tx1,fitness(g(tx1)));
	F[j]=(tx2,fitness(g(tx2)));
	return(F);

def mutation(F,M):		#M=length of cromosome
	i=randint(0,len(F)-1)
	t1=F[i][0];
	j=randint(0,M)
	if((t1>>j)&1==1):
		t1=~((1<<j)|(~t1))
	else:
		t1=((1<<j)|t1)
	

	F[i]=(t1,fitness(g(t1)));

	return(F);

def select_merge(A,A1,K):
	
	def getkey(item):
		return(item[1])
	A1=sorted(A1,key=getkey);
	A1=A1[:K];
	for i in range(1,K):
		A[-i]=A1[i]
	return(A);
		

			
def genetic(L,M,gen):
	C=return_random_cromosome(L,M)	
	F=gen_all_fitness(C)
	#print F
	gen=1;
	for i in range(gen):
		#print F
		A=selection(F);
		print "top two string= ",g(A[0][0]);
		print "fitness=",A[0][1]
		print "--------------------------------------------------"
		
		A1=crossover(A,1);
		A1=mutation(A1,M);
		A=select_merge(A,A1,1);
	max=-1
	for i in range(len(A)):	
		x=A[i][0];
		if(x>max):
			max=x;
	#print "max string= ",bin(x);
	#print "val=",x
	#print "--------------------------------------------------"


#print return_random_cromosome(15,10);

L=15
M=10
gen=100;
#for gen in range(10,2000):
genetic(L,M,gen)



"""
C=return_random_cromosome(L,M)
for c in  C:
	print c,g(c),fitness(g(c))

F=gen_all_fitness(C)
A=selection(F);
print A


"""



		




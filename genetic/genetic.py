from math import pi
from math import sin
from random import randint



def fitness(x):
	x=pi*x/180;
	if(x>=0 and x<=2*pi):
		return sin(x)+6
	elif(x<=4*pi):
		return 2*sin(x)+6
	elif(x<=6*pi):
		return 3*sin(x)+6
	elif(x<=8*pi):
		return 4*sin(x)+6
	elif(x<=10*pi):
		return 5*sin(x)+6
	elif(x<=32*pi):
		return 6*sin(x)+6
			
def mutate(st1,st2):
	




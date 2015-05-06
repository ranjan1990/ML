import random as r
import math as m

   
def createString(length):
    string =  ''.join(r.choice('01') for _ in range(length))
    return string

def createSet(M,L):
    s = []
    for i in range(M):
        s.append(createString(L))
    return s
    
def mutate(string, q):
    newStr = ""
    for char in string:
        if r.random() <= q:
            c = 0
            if int(char) == 0:
                c = 1
            newStr += str(c)
        else:
            newStr += char
    return newStr
    
def mutateSet(stringSet,q):
    newSet = []
    for string in stringSet:
        newSet.append(mutate(string,q))
    return newSet
        
    
def mate(string1, string2):
    str1 = ""
    str2 = ""
    l = r.randint(1,len(string1)-1)
    p11 = string1[:l]
    p21 = string2[:l]
    p12 = string1[l:]
    p22 = string2[l:]
    str1 = p11+p22
    str2 = p21+p12
    return str1, str2

def G(string):
    val = 0.0
    i = 1
    #print string
    for char in string:
        val += (2**(5-i)) * float(char)
        i += 1
    return val

def fitness(string):
    g = G(string)
    if g >= 0 and g <= 2*m.pi:
        return (m.sin(g) + 6)
    elif g > 2*m.pi and g <= 4*m.pi:
        return (2*m.sin(g) + 6)
    elif g > 4*m.pi and g <= 6*m.pi:
        return (3*m.sin(g) + 6)
    elif g > 6*m.pi and g <= 8*m.pi:
        return (4*m.sin(g) + 6)
    elif g > 8*m.pi and g <= 10*m.pi:
        return (5*m.sin(g) + 6)
    elif g > 10*m.pi and g <= 32:
        return (m.sin(g) + 6)

def getFittest(stringSet):
    fittest = stringSet[0]
    m = fitness(stringSet[0])
    for string in stringSet[1:]:
        if fitness(string) > m:
            m = fitness(string)
            fittest = string
    return fittest


def crossOver(stringSet, p):
    newSet = []
    r.shuffle(stringSet)
    for i in range(0,len(stringSet),2):
        str1 = stringSet[i]
        str2 = stringSet[i+1]
        if r.random() <= p:
            s1, s2 = mate(str1,str2)
            newSet.append(s1)
            newSet.append(s2)
        else:
            newSet.append(str1)
            newSet.append(str2)
    return newSet

def selection(stringSet,M):
    cum = 0.0    
    fSet = []
    for string in stringSet:
        cum += fitness(string)
        fSet.append((fitness(string),string))
    fSet.sort()
    cSet = []
    cSet.append((fSet[0][0]/cum,fSet[0][1]))
    for f in fSet[1:]:
        cSet.append((cSet[-1][0]+(f[0]/cum),f[1]))
    
    selSet = []
    #print cSet
    for i in range(M):
        rand = r.random()
        j = cSet[0][1]
        #print rand
        for c in cSet[1:]:
            #print c
            if rand < c[0]:
                break
            j = c[1]
        #print j
        #if j > M:
            #print "Here"
            #j = M - 1
        #print j
        selSet.append(j)
    return selSet
    
            
        
        
    
        
        
        
        

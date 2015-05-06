from numpy import array;
from numpy import *
import math
def norm_pdf_multivariate(x, mu, sigma):
    #print sigma
    size = len(x)
    if size == len(mu) and (size, size) == sigma.shape:
        det = linalg.det(sigma)
        if det == 0:
            raise NameError("The covariance matrix can't be singular")

        norm_const = 1.0/ ( math.pow((2*pi),float(size)/2) * math.pow(det,1.0/2) )
        x_mu = matrix(x - mu)
        inv = sigma.I        
        result = math.pow(math.e, -0.5 * (x_mu * inv * x_mu.T))
        return norm_const * result
    else:
        raise NameError("The dimensions of the input don't match")



from PIL import Image
from numpy import cov
class BAYES:
	def __init__(self,D,N):	
		self.data=D;	#D=[[class 1 data],[class 2 data],[..],...] 
		self.NC=N;	#NC NUMBER of class;
		self.data=array(self.data);
		self.mean_cov=[]
		for i in range(len(self.data)):
			D=array(self.data[i]);
			cmat=matrix(cov(D.transpose()))		#covarience
			#print cmat

			D_m=D.mean(axis=0);		#mean
			self.mean_cov.append((D_m,matrix(cmat)));

	def distance(self,X,Y):	#return diatance between vector X and Y point 
		x=array(X)
		y=array(Y);
		d=array((x-y))
		#print d
		d=d.dot(d.transpose())
		return(d);

	def find_class(self,x,K):		#return the class number considering K=K
		DIST=[]
		
		for i in range(len(self.data)):
			for y in self.data[i]:
				DIST.append((self.distance(x,y),i));
		DIST.sort()
		DIST=DIST[:K]
		cls=DIST[0][-1];
		mcount=1;
		dist=DIST[0][0];
		HASH_MAP={};
		for t in DIST:
			tc=t[1];
			if(HASH_MAP.has_key(tc)):
				HASH_MAP[tc]=HASH_MAP[tc]+1;
				if(HASH_MAP[tc]>mcount):
					mcount=HASH_MAP[tc];
					cls=tc;	
			else:
				HASH_MAP[tc]=1;
	#	print HASH_MAP
		return(tc);

	def find_class1(self,X):
		#print self.mean_cov[0][1]
		p1=norm_pdf_multivariate(array(X),self.mean_cov[0][0],self.mean_cov[0][1])
		p2=norm_pdf_multivariate(array(X),self.mean_cov[1][0],self.mean_cov[1][1])
		P=0.3
		if(P*p1>(1-P)*p2):
			return(0);
		else:	
			return(1);



def read_image():
	im1 = Image.open("band1.gif");
	im2 = Image.open("band2.gif");
	im3 = Image.open("band3.gif");
	im4 = Image.open("band4.gif");
	pix1=im1.load()
	pix2=im2.load()
	pix3=im3.load()
	pix4=im4.load()
	f=open("cord.txt","r")
	N=f.readline()
	Data=[]
	for c in range(int(N)):
		n=f.readline()
		A=[];
		for cord in range(int(n)):	#for each point in class
			axis=f.readline()
			axis=axis.split(",");
			x=int(axis[0])
			y=int(axis[1])
			A.append([pix1[x,y],pix2[x,y],pix3[x,y],pix4[x,y]]);
			#A.append([pix1[x,y],pix3[x,y]]);
		Data.append(A);
	return(Data);

Data=read_image();
knn=BAYES(Data,2)






im1 = Image.open("band1.gif");
im2 = Image.open("band2.gif");
im3 = Image.open("band3.gif");
im4 = Image.open("band4.gif");
pix1=im1.load()
pix2=im2.load()
pix3=im3.load()
pix4=im4.load()

im= Image.open("knn.gif");
pix=im.load()
for i in range(im4.size[0]):
	for j in range(im4.size[1]):
		x=[pix1[i,j],pix3[i,j],pix3[i,j],pix4[i,j]]
		#x=[pix1[i,j],pix3[i,j]]
		output_class=knn.find_class1(x)
		if(output_class==0):
			pix[i,j]=255;
		else:
			pix[i,j]=0;
	
im.save("bayes.png");
del im;


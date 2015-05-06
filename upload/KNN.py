from numpy import array;

from PIL import Image

class KNN:
	def __init__(self,D,N):	
		self.data=D;	#D=[[class 1 data],[class 2 data],[..],...] 
		self.NC=N;	#NC NUMBER of class;


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
			A.append([pix1[x,y],pix3[x,y],pix3[x,y],pix4[x,y]]);
		Data.append(A);
	return(Data);

Data=read_image();
knn=KNN(Data,2)
im1 = Image.open("band1.gif");
im2 = Image.open("band2.gif");
im3 = Image.open("band3.gif");
im4 = Image.open("band4.gif");
pix1=im1.load()
pix2=im2.load()
pix3=im3.load()
pix4=im4.load()
for k in [1,3,5,7,9,11,13]:
	print k
	im= Image.open("knn.gif");
	pix=im.load()
	for i in range(im4.size[0]):
		for j in range(im4.size[1]):
			x=[pix1[i,j],pix3[i,j],pix3[i,j],pix4[i,j]]
			output_class=knn.find_class(x,k)
			if(output_class==0):
				pix[i,j]=255;
			else:
				pix[i,j]=0;
		
	im.save("knn"+str(k)+".png");
	del im;




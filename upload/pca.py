import numpy as np
from PIL import Image
def save_image(im_vec_array,k):	#row col not used change it 	      	
	IM_VR=im_vec_array
        im = Image.open("avg.gif")
        pix=im.load()
	col=im.size[1];
        for i in range(im.size[0]):
                for j in range(im.size[1]):
                        pix[i,j]=int(IM_VR[i*col+j])
        im.save("pca"+str(k)+".png");
	return(IM_VR);


def read_pic(pic_name_array):	#returns N*M array N=num of pic M=dimention i.e all pixel 
	image_vector_array=[]
	
	im1 = Image.open(pic_name_array[0])
	pix1=im1.load()
	im2 = Image.open(pic_name_array[1])
	pix2=im2.load()
	im3 = Image.open(pic_name_array[2])
	pix3=im3.load()
	im4 = Image.open(pic_name_array[3])
	pix4=im4.load()
	

	im_vector=[];
	for i in range(im1.size[0]):            #all the row
        	for j in range(im1.size[1]):
			im_vector.append([pix1[i,j],pix2[i,j],pix3[i,j],pix4[i,j]]);

	return(np.array(im_vector));



def find_pca(A):		#A=array #row=number of data   #number of dimention
	#X=np.array(A)			#N*M matrix . M=dimention i.e total pic	N=number of image
	X=A			
	avg_X=X.mean(axis=0)		#1*M matrix
	#X=X-avg_X		#normalizing the avg	 
	#cov_mat=X.dot(X.transpose())		#M*M matrix
	#print cov_mat
	X=X-avg_X;
	X=X.transpose();
	#print "xxxxxxxxx=",len(A);
	cov_mat=X.dot(X.transpose())/len(A)		#M*M matrix
	print "cov_mat=",cov_mat
	eigen_vals,eigen_vector=np.linalg.eigh(cov_mat)
	print "eigen value=",eigen_vals
	print "eigen vector=",eigen_vector
	eigen_vector=eigen_vector.transpose();
	print "lamda*X",eigen_vector[0]*eigen_vals[0]
	print "A*X= ",cov_mat.dot(eigen_vector[0])
	return(eigen_vals,eigen_vector);
	
def save_pic(A,name):
	im = Image.open("avg")
        pix=im.load()
        col=im.size[1];
        for i in range(im.size[0]):
                for j in range(im.size[1]):
                        pix[i,j]=int(A[i*col+j])
                        #print pix[i,j],"  ",int(IM_VR[i*row+j])

        im.save(name);







train_array=["band1.gif","band2.gif","band3.gif","band4.gif"];
im_vr=read_pic(train_array);
print im_vr
mean=im_vr.mean(axis=0);
print "mean=",mean
e_value,e_vector=find_pca(im_vr);


"""

def new1(new_image,k):
	print new_image
	min1=new_image.min()
	max1=new_image.max()
	new_image=((new_image-min1)*255/(max1-min1))
	print new_image
	save_image(new_image,k);


for i in [0,1,2,3]:
	new_image=im_vr.dot(e_vector[i])
	new1(new_image,i)

"""


for i in range(4):
	new_image=im_vr.dot(e_vector[i])
	min1=new_image.min()
	max1=new_image.max()
	#print "e_vector=",i,e_vector[i]
	new_image=((new_image-min1)*255/(max1-min1))
	#print new_image
	save_image(new_image,i);















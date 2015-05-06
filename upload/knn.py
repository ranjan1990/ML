import numpy as np
from PIL import Image
def save_avg_image(im_vec_array):	#row col not used change it 	      	
	#IM_VR=np.array(im_vec_array);
	IM_VR=im_vec_array
	IM_VR=IM_VR.mean(axis=0);
	#print IM_VR
        im = Image.open("avg")
        pix=im.load()
	col=im.size[1];
        for i in range(im.size[0]):
                for j in range(im.size[1]):
                        pix[i,j]=int(IM_VR[i*col+j])
			#print pix[i,j],"  ",int(IM_VR[i*row+j])

        im.save("avg1.gif");
	return(IM_VR);


def read_pic(pic_name_array):			#returns N*M array N=num of pic M=dimention i.e all pixel 
	image_vector_array=[]
	for pic_name in pic_name_array:
		im_vector=[];
		im = Image.open(pic_name)
		pix=im.load()
		for i in range(im.size[0]):            #all the row
	        	for j in range(im.size[1]):
				im_vector.append(pix[i,j]);
		image_vector_array.append(im_vector)

	return(np.array(image_vector_array));



def find_pca(A):		#A=array #row=number of data   #number of dimention
	#X=np.array(A)			#N*M matrix . M=dimention i.e total pic	N=number of image
	X=A			
	avg_X=X.mean(axis=0)		#1*M matrix
	X=X-avg_X		#normalizing the avg	 
	cov_mat=X.dot(X.transpose())		#M*M matrix
	#print cov_mat
	eigen_vals,eigen_vector=np.linalg.eigh(cov_mat)
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

def distance(vec1,vec2):
	sum1=0;
	for i in range(len(vec1)):
		sum1=sum1+(vec1[i]-vec2[i])**2;
	return(sum1)

def cal_weight_vector(im_var,eigen_faces):
	diff=im_var-eigen_faces
	#print diff
	#print"difference =\n",diff.dot(diff.transpose())
	weight=[];
	for i in range(len(diff)):
		weight.append(distance(im_var[i],eigen_faces))
		
		
	w=np.array(weight)
	return w
	#return(w/w.mean())

def classify_face(train_w,test_w):
	po=0;
	diff=999999999999999999;
	for i in range(len(train_w)):
		d1=abs(train_w[i]-test_w)
		if(d1<diff):
			po=i;
			diff=d1;

	return(train_array[po]);
	







train_array=["subject01.normal","subject02.normal","subject03.normal","subject04.normal","subject05.normal","subject06.normal","subject07.normal","subject08.normal","subject09.normal","subject10.normal","subject11.normal","subject12.normal","subject13.normal","subject14.normal","subject15.normal"]



test_array=["subject01.sad","subject02.sad","subject03.sad","subject04.sad","subject05.sad","subject06.sad","subject07.sad","subject08.sad","subject09.sad","subject10.sad","subject11.sad","subject12.sad","subject13.sad","subject14.sad","subject15.sad"]

#train_array=["f1","f2","f3","f4","f5"];
im_vr=read_pic(train_array);
avg_v=save_avg_image(im_vr);
e_value,e_vector=find_pca(im_vr);
#print e_value
#print im_vr
#print e_vector
eigen_faces=e_vector.dot(im_vr)
eigen_faces=eigen_faces+avg_v
#print eigen_faces[0]








tr_w=cal_weight_vector(im_vr,eigen_faces[0])


for  pic in range(len(test_array)):
	im_vt=read_pic([test_array[pic]])
	te_w=cal_weight_vector(im_vt,eigen_faces[0])
	print "-----------------------------------------------------"
	print "original id= ",test_array[pic]
	print "output   id=%s"%classify_face(tr_w,te_w)
	

























import sys
import os
import dlib
import glob
import numpy as np
from skimage import io
import cv2

def doCropping(theImage1,theImage2):
    if(isinstance(theImage1,str)):
        img1=cv2.imread(theImage1)
    else:
        img1=cv2.imdecode(np.fromstring(theImage1.read(), np.uint8),1)
    if(isinstance(theImage2,str)):
        img2=cv2.imread(theImage2)
    else:
        img2=cv2.imdecode(np.fromstring(theImage2.read(), np.uint8),1)
    size1=img1.shape
    size2=img2.shape
    diff0=(size1[0]-size2[0])//2
    diff1=(size1[1]-size2[1])//2
    avg0=(size1[0]+size2[0])//2
    avg1=(size1[1]+size2[1])//2
    if(size1[0]==size2[0] and size1[1]==size2[1]):
        return [img1,img2]
    elif(size1[0]<=size2[0] and size1[1]<=size2[1]):
        scale0=size1[0]/size2[0]
        scale1=size1[1]/size2[1]
        if(scale0>scale1):
            res=cv2.resize(img2,None,scale0,scale0,interpolation=cv2.INTER_AREA)
        else:
            res=cv2.resize(img2,None,scale1,scale1,interpolation=cv2.INTER_AREA)
        return doCroppingHelp(img1,res)
    elif(size1[0]>=size2[0] and size1[1]>=size2[1]):
        scale0=size2[0]/size1[0]
        scale1=size2[1]/size1[1]
        if(scale0>scale1):
            res=cv2.resize(img1,None,scale0,scale0,interpolation=cv2.INTER_AREA)
        else:
            res=cv2.resize(img1,None,scale1,scale1,interpolation=cv2.INTER_AREA)
        return doCroppingHelp(res,img2)
    elif(size1[0]>=size2[0] and size1[1]<=size2[1]):
        return [img1[diff0:avg0,:],img2[:,-diff1:avg1]]
    else:
        return [img1[:,diff1:avg1],img2[-diff0:avg0,:]]

def doCroppingHelp(img1,img2):
    size1=img1.size
    size2=img2.size
    diff0=(size1[0]-size2[0])//2
    diff1=(size1[1]-size2[1])//2
    avg0=(size1[0]+size2[0])//2
    avg1=(size1[1]+size2[1])//2
    if(size1[0]==size2[0] and size1[1]==size2[1]):
        return [img1,img2]
    elif(size1[0]<=size2[0] and size1[1]<=size2[1]):
        return [img1,img2[-diff0:avg0,-diff1:avg1]]
    elif(size1[0]>=size2[0] and size1[1]>=size2[1]):
        return [img1[diff0:avg0,diff1:avg1],img2]
    elif(size1[0]>=size2[0] and size1[1]<=size2[1]):
        return [img1[diff0:avg0,:],img2[:,-diff1:avg1]]
    else:
        return [img1[:,diff1:avg1],img2[-diff0:avg0,:]]

def makeCorrespondence(thePredictor,theImage1,theImage2):

    # Detect the points of face.
    predictor_path = thePredictor
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(predictor_path)

    # Setting up some initial values.
    array = np.zeros((68,2))
    size=(0,0)
    imgList=doCropping(theImage1,theImage2)
    list1=[]
    list2=[]
    j=1

    for img in imgList:

        size=(img.shape[0],img.shape[1])
        if(j==1):
            currList=list1
        else:
            currList=list2

        # Ask the detector to find the bounding boxes of each face. The 1 in the
        # second argument indicates that we should upsample the image 1 time. This
        # will make everything bigger and allow us to detect more faces.
        # Also give error if face is not found.
        dets = detector(img, 1)
        if(len(dets)==0):
            if(isinstance(f,str)):
                return [[0,f],0,0,0,0,0]
            else:
                return [[0,"No. "+str(j)],0,0,0,0,0]
        j=j+1

        for k, d in enumerate(dets):
            
            # Get the landmarks/parts for the face in box d.
            shape = predictor(img, d)
            for i in range(0,68):
                currList.append((int(shape.part(i).x),int(shape.part(i).y)))
                array[i][0]+=shape.part(i).x
                array[i][1]+=shape.part(i).y
            currList.append((1,1))
            currList.append((size[1]-1,1))
            currList.append(((size[1]-1)//2,1))
            currList.append((1,size[0]-1))
            currList.append((1,(size[0]-1)//2))
            currList.append(((size[1]-1)//2,size[0]-1))
            currList.append((size[1]-1,size[0]-1))
            currList.append(((size[1]-1)//2,(size[0]-1)//2))

    narray=array/2
    narray=np.append(narray,[[1,1]],axis=0)
    narray=np.append(narray,[[size[1]-1,1]],axis=0)
    narray=np.append(narray,[[(size[1]-1)//2,1]],axis=0)
    narray=np.append(narray,[[1,size[0]-1]],axis=0)
    narray=np.append(narray,[[1,(size[0]-1)//2]],axis=0)
    narray=np.append(narray,[[(size[1]-1)//2,size[0]-1]],axis=0)
    narray=np.append(narray,[[size[1]-1,size[0]-1]],axis=0)
    narray=np.append(narray,[[(size[1]-1)//2,(size[0]-1)//2]],axis=0)

    return [size,imgList[0],imgList[1],list1,list2,narray]

# makeCorrespondence('shape_predictor_68_face_landmarks.dat','4.jpg','2.jpg')
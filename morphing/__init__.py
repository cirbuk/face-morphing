from morphing.face_landmark_detection import makeCorrespondence
from morphing.delaunay import makeDelaunay
from morphing.faceMorph import makeMorphs
import subprocess
import argparse
import shutil
import os

def doMorphing(thePredictor,theImage1,theImage2,theDuration,theFrameRate,theResult):
	[size,img1,img2,list1,list2,list3]=makeCorrespondence(thePredictor,theImage1,theImage2)
	if(size[0]==0):
		print("Sorry, but I couldn't find a face in the image "+size[1])
		return
	list4=makeDelaunay(size[1],size[0],list3)
	makeMorphs(theDuration,theFrameRate,img1,img2,list1,list2,list4,size,theResult)

if __name__ == "__main__":

	parser=argparse.ArgumentParser()
	parser.add_argument("which", help="Face Or Body Detection?")
	parser.add_argument("img1", help="The First Image")
	parser.add_argument("img2", help="The Second Image")
	parser.add_argument("dur",type=int, help="The Duration")
	parser.add_argument("fr",type=int, help="The Frame Rate")
	parser.add_argument("res", help="The Resultant Video")
	args=parser.parse_args()

	if(args.which=="face"):
		with open(args.img1,'rb') as image1, open(args.img2,'rb') as image2:
			doMorphing('shape_predictor_68_face_landmarks.dat',image1,image2,args.dur,args.fr,args.res)
	elif(args.which=="body"):
		print("Body Detection Coming Soon!")
	else:
		print("Please enter correct detection type.")

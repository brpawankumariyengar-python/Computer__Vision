# Program to create Sketch from Image

import cv2 as Vidyut_Netra


def Pawan_Photo_to_Pencil_Sketch(Photo_Ka_Pata, Kahan_Pe_Rakkhoon):
	Photo_Ka_Pata = Photo_Ka_Pata
	Kahan_Pe_Rakkhoon = Kahan_Pe_Rakkhoon
	#We import original imange into the variable Asli_Chitra
	Asli_Chitra = Vidyut_Netra.imread(Photo_Ka_Pata)
	del Photo_Ka_Pata


	#Now we create a grascale (Black and White) Image from original Image
	Rang_heen_chitra = Vidyut_Netra.cvtColor(Asli_Chitra, Vidyut_Netra.COLOR_BGR2GRAY)


	#We now invert the Image. That is we invert the pixel brightness. This is something like the negatives.
	Vipareet_Chitra = 255 - Rang_heen_chitra

	#we now blur the image by using the gaussian function. This is as pencil sketches are never very sharp
	Dhundla_Vipareet_Chitra = Vidyut_Netra.GaussianBlur(Vipareet_Chitra, (35,35),0)


	#We invert image again to get the blurred  image. This is like taking photo from negative
	Dhundla_Chitra = 255 - Dhundla_Vipareet_Chitra


	#Finally we create a pencil sketch Image. This is done vis devide method in opencv.
	Chitrakaari = Vidyut_Netra.divide(Rang_heen_chitra, Dhundla_Chitra, scale = 256.0) 

	Kahan_Pe_Rakkhoon = Kahan_Pe_Rakkhoon + "Pawan__Made__This.JPG"
	Vidyut_Netra.imwrite(Kahan_Pe_Rakkhoon, Chitrakaari)
	Vidyut_Netra.imshow("This is the original image", Asli_Chitra)
	Vidyut_Netra.imshow("This is the pensil sketch", Chitrakaari)
	Vidyut_Netra.waitKey(0)




if __name__ =="__main__":
	print("Ho Gaya")
	Pawan_Photo_to_Pencil_Sketch("ko.jpg", "/Users/brpawankumar/Desktop/")

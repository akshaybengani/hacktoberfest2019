#!/usr/bin/python3
# importing cv2 library for image processing
import cv2
import reciever_module as r
import os
import gc
# class which represent the specific block covered by a camera
class A():

    # it is to read the image map
    image = cv2.imread('/home/pykid/Desktop/index.jpeg')
    
    #function for yellow color image range 10 to 20
    def A_yellow(self):
        blocka = self.image[400:637,575:800].copy() - [255,0,0]
        blocka = blocka.astype('uint8')
        self.image[400:637,575:800] = blocka
        return self.image

    # function red color image range 40 above that is max
    def A_red(self):
        blocka = self.image[400:637,575:800].copy() - [255,255,0]
        blocka = blocka.astype('uint8')
        self.image[400:637,575:800] = blocka
        return self.image

    # function for minimum no of people that is i range 1 to 10
    def A_green(self):
        blocka = self.image[400:637,575:800].copy() - [150,50,90]
        blocka = blocka.astype('uint8')
        self.image[400:637,575:800] = blocka
        return self.image

    # function for people in range of 20 to 30
    def A_orange(self):
        blocka = self.image[400:637,575:800].copy() - [200,100,0]
        blocka = blocka.astype('uint8')
        self.image[400:637,575:800] = blocka
        return self.image

    # function for crowd in range of 30 to 40
    def A_brown(self):
        blocka = self.image[400:637,575:800].copy() - [150,100,60]
        blocka = blocka.astype('uint8')
        self.image[400:637,575:800] = blocka
        return self.image


#x = int(input())
i = 0
while i<5:
    objects = A()
    x = r.reciever("192.168.10.212",4444) 
    x = int(x)
    #os.system('rm -rfv /home/pykid/Desktop/Adhoc/__pycache__')
    #os.system('rm -rfv /home/pykid/Desktop/Adhoc/image.jpeg')
    if x==0:
        break
    print(x)
    if 0< x < 10:
        maps = objects.A_green()
        cv2.imwrite('image'+str(i)+'.jpg',maps)
    elif 10<= x <20:
        maps = objects.A_yellow()
        cv2.imwrite('image1.jpeg',maps)
    elif 20<= x <30:
        maps = objects.A_orange()
        cv2.imwrite('image2.jpeg',maps)
    elif 30<= x <40:
        maps = objects.A_brown()
        cv2.imwrite('image3.jpeg',maps)
    elif x >=40:
        maps = objects.A_red()
        cv2.imwrite('image4.jpeg',maps)
    else:
        print('kuch kaam ni aata tumhe')
    i = i+1
    gc.collect()


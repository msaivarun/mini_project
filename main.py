import cv2
from queue import PriorityQueue 
  
q = PriorityQueue() 
haar_cascade = 'cars.xml'

img1=cv2.imread('traffic3.webp')
img2=cv2.imread('traffic2.webp')
img3=cv2.imread('traffic1.webp')
img4=cv2.imread('traffic4.webp')

car_cascade = cv2.CascadeClassifier(haar_cascade)
        
# convert to gray scale of each frames 
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) 
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) 
gray3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY) 
gray4 = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY) 
# Detects cars of different sizes in the input image 
cars1 = car_cascade.detectMultiScale(gray1, 1.1, 1) 
cars2 = car_cascade.detectMultiScale(gray2, 1.1, 1) 
cars3 = car_cascade.detectMultiScale(gray3, 1.1, 1) 
cars4 = car_cascade.detectMultiScale(gray4, 1.1, 1) 

# To draw a rectangle in each cars 
f,s,t,fo=0,0,0,0
for (x,y,w,h) in cars1: 
    f+=1
for (x,y,w,h) in cars2: 
    s+=1
for (x,y,w,h) in cars3: 
    t+=1
for (x,y,w,h) in cars4: 
    fo+=1
# Display frames in a window
q.put((f,'img1'))
q.put((s,'img2'))
q.put((t,'img3'))
q.put((fo,'img4'))
print('images according to the number of cars in them are displayed in the order of their priority')
while not q.empty():
    print(q.get()[1])
cv2.waitKey(0)
cv2.destroyAllWindows()
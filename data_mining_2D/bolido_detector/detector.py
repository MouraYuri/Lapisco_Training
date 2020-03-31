import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from skimage.feature import local_binary_pattern as lbp, greycoprops,greycomatrix

cap =  cv.VideoCapture('./data_mining_2D/bolido_detector/dataset/bolido_dataVarginha.mp4')

orb = cv.ORB_create()
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=False)


bolido_fraco = cv.imread('./data_mining_2D/bolido_detector/dataset/bolido_brilhoFracoBH.png', cv.IMREAD_GRAYSCALE)
ret, bolido_fracoThresholded = cv.threshold(bolido_fraco,200,1,cv.THRESH_BINARY)
bolido_fracoSegmented = np.multiply(bolido_fracoThresholded, bolido_fraco)

kp1, des1 = orb.detectAndCompute(bolido_fracoSegmented,None) #finding keypoints on the trainImage


while(cap.isOpened()):
    #reading the current frame
    ret, currentFrame = cap.read()

    #if not was readed then break
    if currentFrame is None:
        break

    #converting currentFrame to grayscale
    currentFrame = cv.cvtColor(currentFrame, cv.COLOR_BGR2GRAY)

    #thresholding image and segmenting it
    ret, thresholdedImg = cv.threshold(currentFrame,200,1,cv.THRESH_BINARY)
    currentFrameSegmented = np.multiply(thresholdedImg, currentFrame)

    #finding keypoints on the query image
    kp2, des2 = orb.detectAndCompute(currentFrameSegmented,None) #query image


    if des2 is not None:
        #matche two images        
        matches = bf.match(des1,des2)

        #sort the matches by distance
        matches = sorted(matches, key = lambda x:x.distance)
        #retImage = cv.drawMatches(bolido_fracoSegmented,kp1,currentFrame,kp2,matches[:5],None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        pos = kp2[matches[0].trainIdx].pt
        retImage = cv.circle(currentFrame, (int(pos[0]), int(pos[1])), 70, color=(190))
        cv.imshow('retImage',retImage)
    else:
        cv.imshow('retImage',currentFrame)

    if cv.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
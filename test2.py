# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 11:14:35 2023

@author: fclin
"""

import cv2

def image_process(src):
    dstx = cv2.Sobel(src, cv2.CV_32F, 1, 0)         # 計算 x 軸影像梯度
    dsty = cv2.Sobel(src, cv2.CV_32F, 0, 1)         # 計算 y 軸影像梯度
    dstx = cv2.convertScaleAbs(dstx)                # 將負值轉正值
    dsty = cv2.convertScaleAbs(dsty)                # 將負值轉正值
    dst =  cv2.addWeighted(dstx, 0.5,dsty, 0.5, 0)  # 影像融合
    cv2.imwrite('sobel_processsing.jpg', dst)
    
source = cv2.imread("photo.jpg")
image_process(source)
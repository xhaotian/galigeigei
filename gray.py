from PIL import Image
import numpy as np
import math
import sys, random

gscale10 = '@%#*+=-:. '
gscale70 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

def getAverageL(image):

    im = np.array(image)
    w, h = im.shape
    return np.average(im.reshape(w*h))

def covertImageToAscii(fileName, cols, scale):
    #scale为0.43，字体为courier,用其它字体时比例随之变化
    global gscale10, gscale70

    image = Image.open(fileName).convert('L')
    W, H = image.size[0], image.size[1]#像素数
    w = W/cols  #根据所给列数求每个块（即每个ascii字符）所占像素宽带
    h = w/scale #根据比例计算每个块所占像素长度
    rows = int(H/h) #计算共有多少行ascii字符

    if cols>W or rows>H:
        print('Image too small for specified cols!')
        exit(0)

    aimg = []
    for j in range(rows):   #遍历每一行ascii
        y1 = int(j*h)
        y2 = int((j+1)*h)
        if j == rows -1:
            y2 = H
        aimg.append('')
        for i in range(cols):   #遍历行中每一个ascii，找到对应字符并添加至结果中
            x1 = int(i*w)
            x2 = int((i+1)*w)
            if i == rows - 1:
                x2 = W
            img = image.crop((x1, y1, x2, y2))
            avg = int(getAverageL(img))
            #print(avg)
            gray = gscale70[int((avg*69)/255)]
            aimg[j] += gray
    
    return aimg
path = input('input path:')
for some in covertImageToAscii(path, 240, 0.43):
    print(some)


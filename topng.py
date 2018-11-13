from PIL import Image
import sys
#path = 'jia2.jpg'
im = Image.open(sys.argv[1])
im.save(sys.argv[1].split(".",1)[0]+'.png')

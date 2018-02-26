import cv2
import argparse

parser = argparse.ArgumentParser(description="parse command line arguments")
parser.add_argument('img1', help="the original image", type=str)
parser.add_argument('img2', help="the result image", type=str)
parser.add_argument('img', help="the small image", type=str)
parser.add_argument('start_r', help="the starting row number", type=int)
parser.add_argument('end_r', help="the ending row number", type=int)
parser.add_argument('start_c', help="the starting column number", type=int)
parser.add_argument('end_c', help="the ending column number", type=int)

args = parser.parse_args()

img1 = cv2.imread('img/'+args.img1)
img2 = cv2.imread('img/'+args.img2)
img1_small = img1[args.start_r:args.end_r,args.start_c:args.end_c]
img2_small = img2[args.start_r:args.end_r,args.start_c:args.end_c]
#img1_small = cv2.resize(img1_small,(120,120),cv2.INTER_AREA)
#img2_small = cv2.resize(img2_small,(120,120),cv2.INTER_AREA)
cv2.imwrite('img/'+args.img+'_before.png',img1_small)
cv2.imwrite('img/'+args.img+'_after.png',img2_small)


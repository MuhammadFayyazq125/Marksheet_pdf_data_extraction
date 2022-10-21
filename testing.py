# import fitz
# from numpy import matrix
# import cv2
import glob
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('data/images/2.png',0)
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
# pd = "data/template/*.pdf"

# def pdf_to_images(pdf_path):
#     pdffile =glob.glob(pdf_path)
#     if (pdffile):
#         print("what is line_length ",len(pdffile))
#         count = 0
#         for pdf in pdffile:
#             doc = fitz.open(pdf)
#             page = doc.load_page(page_id=0)  # number of page
#             # print("what is pdf ", page)
#             pix = page.get_pixmap()
#             count += 1
#             output = "data/images/"+str(count)+".png"
#             pix.save(output)
#     else:
#         print("No pdf file found")

# pdf_to_images(pd)

# Read image
# im = cv2.imread("data/images/278.pdf-0.png")

# Edge preserving filter with two different flags.
# imout = cv2.edgePreservingFilter(im, flags=cv2.RECURS_FILTER)
# cv2.imwrite("data/template/edge-preserving-recursive-filter.jpg", imout)

# imout = cv2.edgePreservingFilter(im, flags=cv2.NORMCONV_FILTER)
# cv2.imwrite("data/template/edge-preserving-normalized-convolution-filter.jpg", imout)

# Detail enhance filter
# imout = cv2.detailEnhance(im)
# cv2.imwrite("data/template/detail-enhance.jpg", imout)

# Pencil sketch filter
# imout_gray, imout = cv2.pencilSketch(im, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
# cv2.imwrite("data/template/pencil-sketch.jpg", imout_gray)
# cv2.imwrite("data/template/pencil-sketch-color.jpg", imout)

# Stylization filter
# cv2.stylization(im,imout)
# cv2.imwrite("data/template/stylization.jpg", imout)
# im = cv2.imread("data/images/278.pdf-0.png")
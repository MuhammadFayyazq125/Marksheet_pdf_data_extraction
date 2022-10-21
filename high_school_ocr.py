from email import header
from operator import index
from traceback import print_tb
from utils.plots import data_in_json
import glob
import cv2
import json
import os
import pandas as pd
import sys
import argparse
from pathlib import Path 
from utils.general import (LOGGER, check_file, check_img_size, check_imshow, check_requirements, colorstr, cv2,
                           increment_path, non_max_suppression, print_args, scale_coords, strip_optimizer, xyxy2xywh)
FILE = Path(__file__).resolve()
# DATA = PureWindowsPath
ROOT = FILE.parents[0] 
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative
# USed for acquire old result by proving exp unique IDs 
def all_high_school(
    highocr
    ):
    print("what is path ",highocr)
    # print("what is file parent ",FILE.parents[0] )
    arr = []
    dic=dict()
    for i in glob.glob(highocr + "/*"):
        # print("what is i ",i)
        path = i + '/'
        for j in glob.glob(path + "*.jpg"):
            arr.append(j)
    for array in arr:
        data =array.split("\\")
        dic[data[-2]]=cv2.imread(array)
    result = data_in_json(dic)
    with open("High_School_ocr.json", "w") as outfile:
        json.dump(result, outfile)
    dictionary = json.dumps(result)
    return dictionary
    
def parse_opt():
    parser = argparse.ArgumentParser()
    # parser.add_argument('--highocr', type=PureWindowsPath)
    parser.add_argument('--highocr', type=str, help='file/dir/URL/glob, 0 for webcam')
    opt = parser.parse_args()
    return opt

def main(opt):
    check_requirements(exclude=('tensorboard', 'thop'))
    all_high_school(**vars(opt))

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)


# arr=[]
# crop_path = []
# for i in glob.glob('runs/detect/*'):
#     path=i+'/'
#     print("what is os directories ", os.listdir(path))

# for j in glob.glob(path+'*'):
#     path2 = j+'/'
#     # print('what is path2 ',path2)

# for k in glob.glob(path2+'*'):
#     crop_path.append(k)
# print("what is crop_path",crop_path)

# dic=dict()
# for i in arr:
#    for j in glob.glob(path+"crops/"+i.split('\\')[-1]+'/*.jpg'):
#        dic[i.split('\\')[-1]]=cv2.imread(j)

# result=data_in_json(arr,dic)
# print("what is the result ",result)
# json.dumps(result)  
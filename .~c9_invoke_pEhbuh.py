# import libraries
import glob                           #explore folder content
import os                             #manage file paths
import sys                            #add location of local packages

import xml.etree.ElementTree as ET    #parse xml files
from pathlib import Path

from PIL import Image                 #Image object
import matplotlib.pyplot as plt       #protting features
import matplotlib.patches as patches

import warnings
warnings.filterwarnings(action='ignore', category=DeprecationWarning)

def split_path_to_list(path: str):
    """function to split a path into a list"""
    print(path)
    rest, tail = os.path.split(path)
    print(rest, tail)
    if (rest == '/'):
        return tail,
    return split_path_to_list(rest) + (tail,)

def set_output_directory(path: str):
    """function to set a new output directory"""
    input_path_elements = list(split_path_to_list(path))
    output_path_elements = [e if e != 'xml_files' else 'txt_files'
                                                for e in input_path_elements]
    return os.path.join('/', *output_path_elements)

def parse_xml(input_filename: str):
    """Read the file from the argument list and dump the contents and keywords
    into a new file in a txt directory"""

    # set new output directory
    output_path = set_output_directory(input_filename)
    new_filename = os.path.splitext(output_path)[0]
    print(new_filename)
    #C:\Duke University\4th Term\Data_analysis_cloud-IDS721\projects\project2\xml_files\Locust_Ridge

    with open(new_filename + ".txt", "w") as myfile:
        print(input_filename)
        tree = ET.parse(input_filename)
        root = tree.getroot()

        for x in root:
            if x.tag == 'size':
                size = x.find("width").text

            for y in list(x.getchildren()):
                if y.tag == 'bndbox':
                    xmin, ymin, xmax, ymax = y.find("xmin").text, \
                                             y.find("ymin").text, \
                                             y.find("xmax").text, \
                                             y.find("ymax").text
                    x =  (float(xmin) + float(xmax))/(2*float(size))
                    y =  (float(ymin) + float(ymax))/(2*float(size))
                    height = (float(ymax) - float(ymin))/(float(size))
                    width = (float(xmax) - float(xmin))/(float(size))

                    myfile.write("0 " + " ".join([str(x), str(y),
                                          str(width), str(height)]) + '\n')
    
    return
    
def draw_bounding_box(img_path: str, bndbox_path: str):
    """function to return a figure object with an image and its labels
    over the tagged objects"""
    # create Image object
    im = Image.open(img_path)

    # Create figure and axes
    fig,ax = plt.subplots()

    # Display the image
    ax.imshow(im)

    # Create rectangular patches from the bounding boxes
    rect_patches = []
    with open(bndbox_path, 'r') as myfile:
        lines = myfile.readlines()
        for line in lines:
            [tag, x, y, w, h] = list(map(float, line.split()))
            xmin = (x-w/2)
            ymin = (y-h/2)
            rect_patches.append(patches.Rectangle((xmin*608,ymin*608),
                       w*608,h*608,linewidth=1,edgecolor='r',facecolor='none'))

    for rect_patch in rect_patches:
        ax.add_patch(rect_patch)

    return fig
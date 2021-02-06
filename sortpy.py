# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:27:51 2021

@author: Nilesh
"""
import os
from shutil import copy

#########################################
## These are the list of file extensions.
#########################################

# Image Exntensions
image_extension = ["tif", "tiff","bmp","jpg","jpeg","gif","png","eps","raw","svg"]

# Video Extensions
video_extension = ["mp4", "m4a", "m4v", "f4v", "f4a", "m4b", "m4r", "f4b", "mov", "3gp", "3gp2", "3g2", "3gpp", "3gpp2", "ogg", "oga", "ogv", "ogx","wmv", "wma", "asf",
"webm","flv"]

# Document Extensions
doc_extension = ["doc","docx","odt","pdf","xls","xlsx","csv","ods","ppt","pptx","txt"]

# Audio Extensions
audio_extension = ["wav","mp3","acc","aiff","ogg","wma","flac","alac"]

# Programming Code
code_extension = ["c","cpp","h","java","asm","html","xml","py","ipynb","js","css","cs","php","swift","vb","cgi","pl","class"]

######################
## Store File Function
######################

def Store_file(Type,file,PATH):
    """
    Store the file in a Classifies Folder
    ------------------------------------------
    Input: Type of file and name of the file
    Output: Create folder or store the file in existing folder
    """
    DEST = os.getcwd()+"\\"+Type
    
    if Type not in os.listdir():
        os.mkdir(PATH+"\\"+"\\"+Type)
        src = PATH
        dest = PATH + "\\"+"\\"+Type
        try:
            copy(src+"\\"+"\\"+file,dest)
            print("DONE!")
        except:
            print("The current directory contains folder which will not be sorted.")
        
    else:
        src = PATH
        dest = PATH + "\\"+"\\"+Type
        try:
            copy(src+"\\"+"\\"+file,dest)
            print("DONE!")
        except:
            print("The current directory contains folder which will not be sorted.")
        
        
        
    
####################
## Classify Function
####################

def Classify_File(name_of_the_file,PATH):
    """
    Classify_File is a user-defined function.
    -------------------------------------------
    Input: Name of the File
    Output: Type of the File
    
    """
    
    ## Extension stored here
    EXTENSION = name_of_the_file.split(".")[-1].lower()
    
    if EXTENSION in image_extension:
    
        Store_file("IMAGE",name_of_the_file,PATH)
    
    elif EXTENSION in video_extension:
    
        Store_file("VIDEO",name_of_the_file,PATH)
    elif EXTENSION in doc_extension:
    
        Store_file("DOCUMENTS",name_of_the_file,PATH)
    elif EXTENSION in audio_extension:
    
        Store_file("AUDIO",name_of_the_file,PATH)
    elif EXTENSION in code_extension:
    
        Store_file("PROGRAMMING",name_of_the_file,PATH)
    else:
        Store_file("OTHERS",name_of_the_file,PATH)


# Main
print("----------------------Welcome to SortPy----------------------")   
PATH = os.getcwd()
confirm = input("Do you want to sort the folder {} ? [y/n]\n".format(PATH))
if confirm.lower() == "n":
    PATH = input("Enter the location: \n")
    PATH = PATH.replace("\\","\\"+"\\")
    os.chdir(PATH)
    Files = os.listdir()
    for i,_ in enumerate(Files):
        print("File {}: {}".format(i+1,_))
        Classify_File(_,PATH)
        try:
            os.remove(_)
        except:
            pass
    
elif confirm.lower() == "y":
    Files = os.listdir()
    for i,_ in enumerate(Files):
        print("File {}: {}".format(i+1,_))
        Classify_File(_,PATH)
        try:
            os.remove(_)
        except:
            pass
else:
    print("Invalid Input!")
if os.listdir(PATH+"\\"+"\\"+"OTHERS") == []:
    os.rmdir(PATH+"\\"+"\\"+"OTHERS")
print("Sorting is Complete!")
    
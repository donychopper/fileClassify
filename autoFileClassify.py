# coding=UTF-8
# -*- coding: utf-8 -*- 
'''
from os import listdir
from os.path import isfile, isdir, join
'''
import os
import shutil
from os import *
from os.path import *

mypath = raw_input("Please input the path you want to classify:")
fileAndDir = [ f for f in listdir(mypath) if join(mypath,f) ]
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
onlydirectorys = [ f for f in listdir(mypath) if isdir(join(mypath,f)) ]
for file in fileAndDir:
    print(file)
    fileFormat = file.split('[')
    if len(fileFormat) > 2:
        animateName = fileFormat[2][:-1]
        print(file)
        print(animateName)
        fileFullPath = mypath + '/' + file
        dirFullPath = mypath + '/' + animateName
        print(fileFullPath)
        print(dirFullPath)
        if os.path.exists(dirFullPath):
            shutil.move(fileFullPath, dirFullPath)
        else :
            os.mkdir(dirFullPath)
            shutil.move(fileFullPath, dirFullPath)
        '''
        for context in fileFormat:
            context = context[:-1]
            print(context)
        '''


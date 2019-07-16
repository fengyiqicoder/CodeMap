#
#  Created by FengYQ on 2019/7/12.
#  Copyright © 2019 FengYQ. All rights reserved.
#


import os
from SourceCode.test import *
class Node:
    def __init__(self,value):
        self.val = value
        self.nodes = []

#多叉树的层次遍历

def checkFileTree(node,url,level,classLabel):#先序遍历
    fileName = node.val
    fileLocation = url+"/"+fileName
    newUrl = fileLocation if level != 1 else url
    # print(newUrl)
    #写入目录
    title = getTitleLevel(level)
    if fileName.endswith(".swift"):
        # print(fileLocation)
        scanFile(fileLocation,level-1,classLabel)
    else:
        with open(writeInFileName, 'a') as newFile:
            newFile.write(title+fileName+lineBreak)
    for subNode in node.nodes:
        checkFileTree(subNode,newUrl,level+1,classLabel)

def getTitleLevel(level):
    result = ""
    for _ in range(0,level):
        result += "#"
    result += " "
    return result

def scanProject(folderName,classLabel):
    #文件树的创建
    mainName = folderName.split("/").pop()
    fileTree = Node(mainName)
    for root, dirs, files in os.walk(folderName):
        for name in files:
            if name.endswith(".swift"):
                fileLocation = root+"/"+name
                fileName = fileLocation[len(folderName)+1:]
                nameArray = fileName.split("/")
                #创建它
                currentNode = fileTree
                for nodeName in nameArray:
                    hasNode = False
                    for node in currentNode.nodes:
                        if node.val == nodeName:
                            currentNode = node
                            hasNode = True
                            break
                    if not hasNode:
                        newNode = Node(nodeName)
                        currentNode.nodes.append(newNode)
                        currentNode = newNode  
    #删除原有文件如果它存在的话
    if os.path.exists(writeInFileName):
        os.remove(writeInFileName)
    #遍历文件树
    checkFileTree(fileTree,folderName,1,classLabel)
    print("CodeMap 生成成功!")
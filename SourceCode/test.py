#
#  Created by FengYQ on 2019/7/12.
#  Copyright © 2019 FengYQ. All rights reserved.
#

from SourceCode.words import *

# name = 'DocumentListBaseViewController.swift'
writeInFileName = 'CodeMap.md'
lineBreak = '\n'
#传入一个文件名称和当前的基础#数量
def scanFile(name,titleStartFrom,classLabelEnable):
    #生成基础的#数量
    baseTitle = ""
    for _ in range(0,titleStartFrom):
        baseTitle += "#"
    classNode = {}
    documentName = name
    with open(documentName) as file_object: 
        contents = file_object.readlines()
        currentClassName = "None"
        currentPropertyName = ""
        for line in contents:
            wordList = line.strip().split(" ")
            if line.strip().startswith("//"):
                continue
            regularLine = True
            for index in range(0,len(wordList)):
                word = wordList[index]
                # 这一行是Class
                if word in firstClassArray:
                    # name = word + " " + dealWithColon(wordList[index+1])
                    name = line
                    if name not in classNode.keys():
                        classNode[name] = {}
                        currentClassName = name
                    regularLine = False
                    break
                # 这一行是属性 或者 init
                if (len(line) > 5 and (line[4] != " " or line[2] != " ") and word in secondNodeArray) or (checkIfThisLineIsInitFunction(word)) :
                    #确认index是否能够被使用
                    # if index >= len(wordList)-1 :
                    #     # currentPropertyName = word
                    #     print(word)
                    # else:
                    #     # name = dealWithColon(wordList[index+1])
                    #     currentPropertyName = word + " " + name
                    currentPropertyName = line
                    #添加这个属性名到字典里,并且添加第一行
                    if currentClassName not in classNode.keys():#注意:不严谨单单为了None而存在
                        classNode[currentClassName] = {}
                    classNode[currentClassName][currentPropertyName] = line
                    regularLine = False
                    break
            if regularLine and currentClassName != "" and currentPropertyName != "":
                if currentPropertyName in classNode[currentClassName].keys() :#注意:不严谨无法处理未在字典中定义的东西
                    oldValue = classNode[currentClassName][currentPropertyName]
                    classNode[currentClassName][currentPropertyName] = oldValue + line
    with open(writeInFileName, 'a') as newFile:
        newFile.write(baseTitle + "# "+documentName.split("/").pop()+lineBreak)
        classNames = classNode.keys()
        for className in classNames:
            newFile.write(baseTitle + "## " + className +lineBreak)
            classDict = classNode[className]
            #分开不同种类的属性
            if classLabelEnable:
                diffProperDict = {}
                for propertiesWholeName in classDict.keys():
                    properName = propertiesWholeName.split(" ")[0]
                    if properName not in diffProperDict.keys():
                        diffProperDict[properName] = [propertiesWholeName]
                        # print(diffProperDict[properName])s
                    else:
                        oldList = diffProperDict[properName]
                        oldList.append(propertiesWholeName)
                        # print(type(oldList))
                        diffProperDict[properName] = oldList
                for properName in diffProperDict.keys():
                    newFile.write(baseTitle + "### "+properName+lineBreak)
                    for name in diffProperDict[properName]:
                        newFile.write(baseTitle + "#### "+name+lineBreak)
                        newFile.write(classNode[className][name])
            else:
                #不分开直接输出
                for propertiesWholeName in classDict.keys():
                    newFile.write(baseTitle + "### "+propertiesWholeName+lineBreak)
                    newFile.write(classNode[className][propertiesWholeName])        
def dealWithColon(word):
    if word[len(word)-1] == ":":#删除某些name可能会带有:
        return word[:-1]
    else:
        return word

def checkIfThisLineIsInitFunction(word):
    # print(word)
    return word.startswith("init")

from SourceCode.getFIles import scanProject

#使用须知⚠️⚠️⚠️
#1.文件夹的深度不能最好不要超过三层 如果文件夹更深的话可以对子文件夹生成CodeMap
#2.默认的Swift属性缩进为4个空格,请确保.swift文件的缩进规范


#参数1:目录位置
folderName = "/User/....."
#参数2:是否对class中的var let fun进行分类
classLabel = False 

scanProject(folderName,classLabel)

#执行后将文件夹下的CodaMap.md导入XMind
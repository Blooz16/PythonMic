import os


def FolderFinder(Path):
    temp = os.listdir(Path)
    resultList=[]
    for i in temp:
        clearString = os.path.splitext(i)
        resultList.append(clearString[0])
    print(resultList)
    return resultList

#FolderFinder("C:/Users/User/Desktop")

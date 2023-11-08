from FolderFinder import FolderFinder
import os


def SearchbyName(search, desktop):
    result = "Не найдено ни одного совпадения"
    count = 0
    maxElements = len(desktop)

    while count < maxElements:
        if desktop[count] == search:
            # print("Исходный элемент находится под номером", count)
            result = count
        count += 1
    return result


search = "Текстовый документ"
desktopPath = "C:/Users/User/Desktop"
desktop = FolderFinder(desktopPath)

result = SearchbyName(search, desktop)
print(result)

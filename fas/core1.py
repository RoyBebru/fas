from pathlib import (Path, PosixPath)

dir_list=[
    Path('/home/su/My/GoIT/aaa=o/folder1/folderA/ddd'),
    Path('/home/su/My/GoIT/aaa=o/folder1/folderA'),
    Path('/home/su/My/GoIT/aaa=o/folder1/folder2/xxx'),
    Path('/home/su/My/GoIT/aaa=o/folder1/folder2'),
    Path('/home/su/My/GoIT/aaa=o/folder1/1/picture/wallpaper'),
    Path('/home/su/My/GoIT/aaa=o/folder1/1/picture/icons'),
    Path('/home/su/My/GoIT/aaa=o/folder1/1/picture/Other/icons'),
    Path('/home/su/My/GoIT/aaa=o/folder1/1/picture/Other'),
    Path('/home/su/My/GoIT/aaa=o/folder1/1/picture/Logo'),
    Path('/home/su/My/GoIT/aaa=o/folder1/1/picture'),
    Path('/home/su/My/GoIT/aaa=o/folder1/1/dist/svg'),
    Path('/home/su/My/GoIT/aaa=o/folder1/1/dist/png'),
    Path('/home/su/My/GoIT/aaa=o/folder1/1/dist/jpg'),
    None,
    Path('/home/su/My/GoIT/aaa=o/folder1/1/dist/jpeg'),
    Path('/home/su/My/GoIT/aaa=o/folder1/1/dist'),
    Path('/home/su/My/GoIT/aaa=o/folder1/1'),
    Path('/home/su/My/GoIT/aaa=o/folder1'),
    None,
    Path('/home/su/My/GoIT/aaa=o')
    ]

"""
[1]     /home/su/My/GoIT/aaa=o/folder1/folderA/ddd
[1]     /home/su/My/GoIT/aaa=o/folder1/folder2/xxx
[1]     /home/su/My/GoIT/aaa=o/folder1/1/picture/wallpaper
[1]     /home/su/My/GoIT/aaa=o/folder1/1/picture/icons
[1]     /home/su/My/GoIT/aaa=o/folder1/1/picture/Other/icons
[1]     /home/su/My/GoIT/aaa=o/folder1/1/picture/Logo
[1]     /home/su/My/GoIT/aaa=o/folder1/1/dist/svg
[1]     /home/su/My/GoIT/aaa=o/folder1/1/dist/png
[1]     /home/su/My/GoIT/aaa=o/folder1/1/dist/jpg
[1]     /home/su/My/GoIT/aaa=o/folder1/1/dist/jpeg
[2]     /home/su/My/GoIT/aaa=o/folder1/folderA
[2]     /home/su/My/GoIT/aaa=o/folder1/folder2
[2]     /home/su/My/GoIT/aaa=o/folder1/1/picture/Other
[2]     /home/su/My/GoIT/aaa=o/folder1/1/dist
[3]     /home/su/My/GoIT/aaa=o/folder1/1/picture
[4]     /home/su/My/GoIT/aaa=o/folder1/1
[5]     /home/su/My/GoIT/aaa=o/folder1
[6]     /home/su/My/GoIT/aaa=o
"""

def div_by_threads(dir_list: list):
    th_list_list = []
    len_dir_list = len(dir_list)
    rootpath = dir_list[len_dir_list-1]
    dir_list = dir_list[0:len_dir_list-1]
    while True:
        th_list = []
        dir_list = [e for e in dir_list if e is not None]

        dix = 0
        len_dir_list = len(dir_list)
        if len_dir_list == 0:
            th_list_list.append([rootpath])
            break

        while True:
            path = dir_list[dix]
            th_list.append(path)
            dir_list[dix] = None
            dix += 1

            while dix < len_dir_list:
                path = path.parent
                if path != dir_list[dix]:
                    break
                dix += 1
            else: # while without break
                # end of dir_list
                break

        th_list_list.append(th_list)
    
    return th_list_list


th_list_list = div_by_threads(dir_list)

i = 0
for t in th_list_list:
    i += 1
    for tt in t:
        print(f"[{i}]\t{tt}")

import os, sys

def creatTest(path, list):
    mypath = path
    full_path = mypath + "/test" + '.txt'  # 也可以创建一个.doc的word文档
    # full_path = mypath + "\\test" + '.txt'  # 也可以创建一个.doc的word文档
    file = open(full_path, 'w')
    for string in list:
        file.write(string + " " + "1" + "\n")
    file.close()

if __name__ == '__main__':
    # 打开文件
    path = "dataset2"
    dirs = os.listdir( path )
    # 输出所有文件和文件夹
    creatTest(path,dirs)
    for file in dirs:
        print(file+" "+"0")
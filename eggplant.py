import os
import linecache
__version__ = '0.1'
def bulidFile(filename,extension='.txt',path='',content='',encoding='utf-8'):
    with open(path+filename+extension,'w+',encoding=encoding) as f:
        f.write(content)

def delFile(filename,extension='.txt',path=''):
    os.remove(path+filename+extension)

def allWriteFile(filename,content,extension='.txt',path='',encoding='utf-8'):
    with open(path+filename+extension,'w',encoding=encoding) as f:
        f.write(content)

def addWriteFile(filename,content,extension='.txt',path='',encoding='utf-8'):
    with open(path+filename+extension,'a',encoding=encoding) as f:
        f.write(content)

def insWriteFile(filename,content,extension='.txt',path='',encoding='utf-8'):
    with open(path+filename+extension,'a',encoding=encoding,index='END') as f:
        if index!='END':
            f.seek(index)
        f.write(content)

def readFile(filename,extension='.txt',path='',encoding='utf-8',size=None):
    with open(path+filename+extension,'r',encoding=encoding) as f:
        return f.read(size)

def readLinesFile(filename,extension='.txt',path='',encoding='utf-8',size=None):
    with open(path+filename+extension,'r',encoding=encoding) as f:
        return f.read(size).split('\n')

def readLineFile(filename,extension='.txt',line=1,path='',encoding='utf-8',size=None):
    return linecache.getline(path+filename+extension,line).strip()

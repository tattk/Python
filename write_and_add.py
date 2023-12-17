#!/usr/bin/env python
# coding: utf-8
# Jupyter Notebookで作成し，一部デフォルメ
# https://note.nkmk.me/python/

#Pythonで任意の.txtへ書き込みを行うコード
#encoding確認
import locale
print(locale.getpreferredencoding())

#実行前にターミナルのパス権限確認
path = '/Users/username/Desktop/filename.txt'
with open(path) as f:
    print(type(f))

#filename.txtへ書き込み
#mode='w'は上書き、'a'は末尾に追記.どちらもファイルなければ新規作成

s = '\nadd line' 
with open(path, mode='a') as f:
    f.write(s)
with open(path) as f:
    print(f.read())

#配列、
l = ['x', 'y', 'z']
l.insert(0,'First')

with open(path,mode='w') as f:
    f.write('\n'.join(l))

with open(path) as f:
    print(f.read())


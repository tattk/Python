#!/usr/bin/env python
# coding: utf-8
# Jupyter Notebookで作成し，一部デフォルメ
# https://note.nkmk.me/python/

#和暦西暦htmlの表をcsvで一括取得
#データ分析lib pandasでtable取得
import pandas as pd

url = 'https://www.jcb.co.jp/processing/share/wareki.html'
dfs = pd.read_html(url)
print(len(dfs))

#head()メソッドのデフォは先頭5行
print(dfs[0].head())

#DataFrameの連結;concat, ignore_indexで再連番取得
df = pd.concat([dfs[0],dfs[1],dfs[2],dfs[3],dfs[4]], ignore_index=True)
print(df)
#和暦列をindexにする
df_reset = df.set_index('和暦')
print(df_reset)

#wareki.csvファイルとして出力
df_reset.to_csv('/Users/username/Desktop/wareki.csv', mode='w')



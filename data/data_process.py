# 将数据汇总到一起

# 输出当前目录
from multiprocessing.dummy import current_process
import os
import sys
import json
import ast
from tracemalloc import start

test_path = 'data/mnre_test.txt'
train_path = 'data/mnre_train.txt'
val_path = 'data/mnre_val.txt'

data_paths = [test_path, train_path, val_path]
datas = []
for i in range(len(data_paths)):
    with open(data_paths[i], 'r', encoding='utf-8') as f:
        data = f.read().split('\n')
        datas += data

# 单引号解析
datas = [ast.literal_eval(i) for i in datas]


for i in range(len(datas)):
    datas[i]['img_path'] = 'images/' + datas[i]['img_id']
    datas[i]['sentence'] = ' '.join(datas[i]['token'])
    datas[i]['token_html'] = datas[i]['token']
    for j in range(datas[i]['h']['pos'][0], datas[i]['h']['pos'][1]):
        datas[i]['token_html'][j] = '<b class="head_entity">' + datas[i]['token_html'][j] + '</b>'
    for j in range(datas[i]['t']['pos'][0], datas[i]['t']['pos'][1]):
        datas[i]['token_html'][j] = '<b class="tail_entity">' + datas[i]['token_html'][j] + '</b>'
    datas[i]['sentence_html']  = ' '.join(datas[i]['token_html'])
    datas[i] = str(datas[i]) 
    
    


with open('data/mnre.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(datas))


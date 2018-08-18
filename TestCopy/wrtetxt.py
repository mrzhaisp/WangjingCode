#coding=utf-8
import time
tag = 'ocdzykc'
poorDerNumBer='0001808186582699'
creaTeDate = time.strftime("%Y-%m-%d %H:%M:%S")
with open('../DataShare/zykc-ordernumbs.txt', 'a') as f:
    f.write(poorDerNumBer + '    ')
    f.write(creaTeDate + '    ')
    f.write(tag + '\n')
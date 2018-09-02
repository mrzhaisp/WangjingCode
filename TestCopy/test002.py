#coding=utf-8
import sys,time
# for i in range(0,110,10):
#     sys.stdout.write("▒▒▒"+" %"+str(i))
#     sys.stdout.flush()
#     time.sleep(0.5)


# import time
# N = 100
# for i in range(N):
#     print("进度:{0}%".format(round((i + 1) * 100 / N)) )
#     time.sleep(0.01)

import sys,time
for i in range(100):
    k = i + 1
    str = '▒'*i+''*(100-k)
    sys.stdout.write('\r'+str+'[%s%%]'%(i+1))
    sys.stdout.flush()
    time.sleep(0.05)
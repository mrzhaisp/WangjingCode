#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
#
# b = a.encode('utf-8')
# # print(b)
# a='\u559c\u6b22\u4e00\u4e2a\u4eba'
# print a.decode('raw_unicode_escape')

b = '\u8865\u5f55\u5b8c\u6210'
print(b)
print b.decode('unicode_escape')
#
# c =  u'\xe8\xa1\xa5\xe5\xbd\x95\xe4\xb8\x93\xe7\xba\xbf\xe5\xb1\x9e\xe6\x80\xa7'
# print(c.decode("string_escape"))









# coding=utf-8
from __future__ import print_function
import sys

# 接收shell的ll命令，取文件名，例如：
# [root@iZwz93v6r4t2hixjvy9acoZ mytest]# ll
# total 24
# -rwxrwx--- 1 197609 197609  45 Apr 11 11:48 01_HelloWorld.py
# -rwxrwx--- 1 197609 197609 190 Apr 12 09:33 02_DealWithPipeline.py
# -rwxrwx--- 1 197609 197609 434 Apr 10 17:00 mytest.iml
# -rw-r--r-- 1 root   root    60 Apr 11 11:54 python
# -rwxrwx--- 1 197609 197609 434 Apr 11 10:55 pythontest.iml
# -rw-r--r-- 1 root   root   497 Apr 12 09:31 result.txt
# You have new mail in /var/spool/mail/root

# 输出结果
# [root@iZwz93v6r4t2hixjvy9acoZ mytest]# ll | python 02_DealWithPipeline.py > result.txt && cat result.txt
# 抽取文件名为：-> 20
# 抽取文件名为：-> 01_HelloWorld.py
# 抽取文件名为：-> 02_DealWithPipeline.py
# 抽取文件名为：-> mytest.iml
# 抽取文件名为：-> python
# 抽取文件名为：-> pythontest.iml
# 抽取文件名为：-> result.txt


for line in sys.stdin.readlines():
    filename = line.split(' ')[-1].strip()  #取文件名，并去掉空白字符，空白字符包括换行符
    print("抽取文件名为：", filename, end="\n", sep="-> ")


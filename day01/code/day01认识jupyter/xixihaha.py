# import shutil
# import os
# # print(os.getcwd())
# # os.chdir('F:\shuju_code\day01\code')
# # print(os.getcwd())
# # cmd = 'find '+ 'day*'
# # print(cmd)
# # file_list = os.popen(cmd)
# # print(file_list.name)
# cmd = 'netstat -naop|grep 3360'
# print(os.popen(cmd))
# import subprocess
# ping = subprocess.Popen(["ping","127.0.0.1"],stdout = subprocess.PIPE,stderr = subprocess.PIPE)
# out,error = ping.communicate()
# print(out.decode('gbk'))
#
# ping = subprocess.Popen(["netstat -naop | grep 3360"],stdout = subprocess.PIPE,stderr = subprocess.PIPE)
# out,error = ping.communicate()
# print(out.decode('gbk'))

import sys
ip = sys.argv[2]
port = sys.argv[1]

print(ip,port)

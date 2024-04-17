# coding=utf-8
import commands
import glob
import json
import logging
import logging.handlers
import os
import sys
import httplib
import time

print "======================================== 字符串 =======================================";
# 占位符
# 其中，%s 表示字符串类型，%d 表示整数类型。可以根据需要使用不同的格式化符号来表示不同类型的变量。
# 例如下面输出：
# hello: 15岁生日快乐。 zhangsan, lisi, wangwu
msg = "hello: %d岁生日快乐。 %s, %s, %s" % (15, "zhangsan", "lisi", "wangwu")
print msg;

# 使用一个分隔符，来链接一个列表的所有值
# 例如下面输出：
# zhangsan-分隔符-lisi-分隔符-wangwu
oldMsg = ["zhangsan", "lisi", "wangwu"]
joinMsg = "-分隔符-".join(oldMsg);
print joinMsg

# 字符串是否在为指定字符串的子串
if "zhangsan" in "zhangsan and lisi":
    print "zhangsan is in zhangsan and lisi"

# 字符串转成16进制
# 将字符串转换为16进制的好处有以下几点：
# 1、节省存储空间：将字符串转换为16进制后，每个字符只需要占用2个字节（16位）的空间，而ASCII码则需要8个字节（64位）。因此，使用16进制可以大大减少存储空间的占用。
# 2、提高传输效率：在网络传输中，使用16进制可以减少传输的数据量，从而提高传输效率。
# 3、便于处理二进制数据：16进制是一种二进制表示方式，可以将字符串中的每个字符转换为对应的16进制数，方便进行二进制数据处理和操作。
# ascII字符串传输方式，在网络发送的时候也会转成2进制发送，1个字节8位，需要8个二进制表示。但如果直接发送16进制数据，则需要2个16进制就可以表示了
hexStr = "7B22636C757374657254797065223A322C22636F6E7461696E657254797065223A22544F4D434154222C2269734173796E63223A66616C73652C2267726F75704964223A2232353262626434312D343031382D346436322D396563662D646331326231346532636434222C22454441535F5441534B5F4652414D455F736372697074446F776E6C6F616455726C223A22687474703A2F2F656461732D737A2E6F73732D636E2D7368656E7A68656E2D696E7465726E616C2E616C6979756E63732E636F6D2F616374696F6E5363726970742F332E362E31322F7363726970742E7461722E677A222C2274797065223A2264656661756C74222C226563754964223A2265653539393336652D653830382D343565612D393236352D386366396636653230333135222C226F70657261746F72223A2231353839333839343234353231373639222C2274696D656F7574223A302C22697041646472223A223139322E3136382E32392E313334222C22454441535F5441534B5F4652414D455F616374696F6E56657273696F6E223A22332E362E3132222C226170704964223A2262386233313365612D396332322D346238632D623538352D316466636363323666663831222C227461736B4E616D65223A227374617274496E7374616E6365222C226563634964223A2264313530306530302D303061342D346230372D386334332D323663373933323361363230222C227461736B4964223A2265363566356133642D633165622D343363662D393736392D376533336532663332396163222C22636964223A2265363566356133642D633165622D343363662D393736392D376533336532663332396163227D";
decodeStr = hexStr.decode("hex");
newHexStr = decodeStr.encode("hex").upper();
print "16进制解码解码结果为：%s" % (decodeStr);
print "hexStr   ：%s" % (hexStr);
print "newHexStr：%s" % (newHexStr);
if hexStr == newHexStr:
    print "16进制编码结果一致"


print "======================================== json库 =======================================";
# 需要import json
# 在Python中，大括号 {} 用于多种用途，具体取决于上下文：可以是字典值，my_dict = {'key': 'value'}，可以是set:my_set = {1, 2, 3},或者其他
jsonContent = {};
if decodeStr is not None:
    # 字符串转json对象
    jsonContent = json.loads(decodeStr, "utf-8");
print "json格式化输出：";
print json.dumps(jsonContent, "utf-8", indent=4);
print "containerType=%s" % (jsonContent.get("containerType"))


print "======================================== time库-时间、格式化 =======================================";
# 获取当前时间结构体
current_time = time.localtime()
print("当前时间结构是：%s" % current_time);
# 打印指定格式时间
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
print("当前时间格式化：%s" % formatted_time);

# 获取当前时间毫秒
current_time2 = time.time();
print("当前时间毫秒是：%s" % current_time2);
# 打印格式化时间，需要用time.localtime(毫秒值),先把毫秒值，转化成结构体
formatted_time2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(current_time2))
print("当前时间格式化：%s" % formatted_time2);


print "======================================== os库-操作系统路径、文件操作 =======================================";
# 获取当前工作目录 get current work directory
current_dir = os.getcwd();
print(current_dir);

# 修改工作目录
# Change the current working directory to the specified path.
# os.chdir(os.getenv('HOME', '/home/admin'))

# 智能拼接目录，主要是文件分隔符不用关系了
libdir = os.path.join(current_dir, "lib");
print (libdir);

# 从文件全路径，获取文件名
fileFullPath = '/home/admin/edas/script/actions/non_docker_task/checkMachineConfigVersion.py';
fileBasename = os.path.basename(fileFullPath);
# fileBasename=checkMachineConfigVersion.py
print "fileBasename=%s" % (fileBasename);

# 获取目录下所有文件详细信息
def get_files_info(directory):
    files = os.listdir(directory)
    for file in files:
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            print("文件名： %s" % file)
            print("文件路径： %s" % file_path)
            print("文件大小： %s bytes" % os.path.getsize(file_path))
            formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime(file_path)))
            print("最后修改时间： %s" % formatted_time)
            print("----------")

get_files_info(current_dir)

# 获取指定目录下的空间和inode
# only support linux
def getFreeSpaceInBytes(folder):
    """ Return folder/drive free space (in bytes)
    """
    st = os.statvfs(folder)
    return st.f_bavail * st.f_frsize


# 每个文件和目录都由一个名为inode的结构体来唯一标识。inode不包含文件的实际内容（即数据），而是包含了关于文件的一系列重要信息，如：文件类型：指示该inode代表的是普通文件、目录还是特殊文件等。权限和所有权：定义了哪些用户或进程可以对文件执行读、写、执行等操作。
# inode可能会在存储大量小文件时不够用。以下是一些详细的情景：大量小文件存储：当一个文件系统存储了过多的小文件时，每个文件都会占用一个inode，即使文件的实际内容很小。
# 监控inode使用情况：定期检查文件系统的inode使用情况，确保没有接近或达到其上限。这可以通过df -i命令来完成，它会显示每个文件系统的inode使用情况。
def getFreeINodes(folder):
    st = os.statvfs(folder)
    return st.f_ffree


# 输出：
# /root/mytest
# /root/mytest/lib
# getFreeSpaceInBytes=30GB
# getFreeINodes=2549570
def hostHealthCheck():
    freeBytes = getFreeSpaceInBytes(current_dir)
    print "getFreeSpaceInBytes=%sGB" % (freeBytes / 1024 / 1024 / 1024);
    if freeBytes < 10 * 1024 * 1024:
        return 10000, "No space left on device. Free space (for /home/admin) in bytes: %d" % freeBytes
    freeInodes = getFreeINodes(current_dir)
    print "getFreeINodes=%s" % (freeInodes);
    if freeInodes < 1000:
        return 10000, "No space left on device. Free inodes (for /home/admin) : %d" % freeInodes
    # 返回结构可以参考这种方式：第一个参数表示状态码，第二个参数表示错误消息
    return 0, ""


hostHealthCheck();

# 获取当前所有环境变量
allKeys = os.environ.iterkeys()
print "打印所有环境变量=====>";
for envKey in allKeys:
    print "%s=%s" % (envKey, os.environ[envKey]);

allItems = os.environ.iteritems();
print "打印所有环境变量=====>";
for envItem in allItems:
    print "%s=%s" % (envItem[0], envItem[1]);

# 更新环境变量
os.environ["test"] = "test";
# 获取指定环境变量
print 'os.environ["test"] = %s' % os.environ.get("test")

os.environ.update({"test": "testValue"})
print 'os.environ["test"] = %s' % os.environ.get("test")

# 删除环境变量
del os.environ["test"];


# 用户创建文件或目录的掩码
# 用户（拥有者）不变、组（用户组）移除掉2写权限，和其他（其他所有用户）移除掉2写权限
os.umask(0022)
# umask是"user file-creation mode mask"的缩写。
# umask是一个Linux命令，它用于设置用户创建文件时的默认权限掩码。这个命令的全称是"user file-creation mode mask"，意在指明当用户创建新文件或目录时，系统应该如何屏蔽（mask）权限。具体来说，umask的值由三个八进制数字组成，这些数字决定了新创建的文件和目录的默认权限设置。
# 例如，如果umask设置为022，那么当用户创建新文件时，默认的权限会是644（即666减去022），而创建新目录的默认权限会是755（即777减去022）。这样的设置有助于保护文件和目录不被其他非授权用户随意访问或修改。


print "======================================== commands库-执行shell命令 =======================================";
# import commands
status, output = commands.getstatusoutput("dir");
# status=0
# output=01_HelloWorld.py	04_CommonLib.py   lib	      pythontest.iml
# 02_DealWithPipeline.py	edas.qiuxy.trace  mytest.iml  readme.txt
# 03_ArgsParseer.py	example.log	  python      result.txt
print "status=%s" % status;
print "output=%s" % output;


print "======================================== sys库-当前python运行时环境相关 =======================================";
# sys.path 是一个 Python 列表，它包含了 Python 解释器在搜索模块和包时会查找的路径。
# 当你在 Python 程序中导入一个模块或包时，Python 解释器会在 sys.path 中的目录里查找对应的文件。
# 默认情况下，sys.path 包括当前工作目录、Python 安装目录下的 lib/site-packages 等。

#打印sys.path
print("当前sys.path是：%s" % sys.path);
for sysPath in sys.path:
    print sysPath

# 如果你想将其他目录添加到 sys.path，以便在这些目录中查找模块和包，可以使用 sys.path.append() 方法：
sys.path.append(os.path.join(os.getcwd(), "lib"))
print("当前sys.path是：%s" % sys.path);
for sysPath in sys.path:
    print sysPath

# 动态import模块
# 动态加载：__import__() 允许程序在运行时根据需要而不是在启动时静态地导入模块，这提供了一种灵活的方式来管理代码依赖性
# __import__(name)
__import__('math')

# sys.modules[name] 的作用是获取指定名称的模块对象。
# 当一个模块被导入时，它会被添加到 sys.modules 字典中，其中键是模块的名称，值是模块对象本身。通过使用 sys.modules[name]，可以访问已经导入的模块对象
# 获取模块对象
module_obj = sys.modules['math']
# 使用模块对象调用函数
result = module_obj.sqrt(16)
print("动态导入math模块，获取math模块的引用module_obj.sqrt(16)=%s" % result)  # 输出： 4.0

# 获取命令行参数
# 执行：
# [root@iZwz93v6r4t2hixjvy9acoZ mytest]# python 04_CommonLib.py do -a test -m testMethod
# sys.argv[0]: /root/mytest/04_CommonLib.py
# sys.argv[1]: do
# sys.argv[2]: -a
print ("sys.argv[0]: " + sys.argv[0]);
print ("sys.argv[1]: " + sys.argv[1]);
print ("sys.argv[2]: " + sys.argv[2]);


print "======================================== httplib =======================================";
# 发送httpget请求
def httpGet(url):
    try:
        conn = httplib.HTTPConnection(url);
        conn.request("GET", "/");
        response = conn.getresponse();
        print response.status;
        print response.reason;
        print response.read();
    except Exception, e:
        print e;
    finally:
        conn.close();

httpGet("www.baidu.com");

print "======================================== logging 和 logging.handlers =======================================";
# 参考：https://docs.python.org/2.7/howto/logging.html#logging-basic-tutorial
# A very simple example is: root logger
# 注意：basicConfig必须放到最前面，否者在第一次调用打印接口后，就不会再去更新配置了。不指定文件，默认输出到标准输出
logging.basicConfig(filename='example.log', level=logging.DEBUG)
# Logging to a file
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')


# 用占位符
logging.warning('%s before you %s', 'Look', 'leap!')

# 指定日志格式和文件滚动
# 内置的日志格式属性：https://docs.python.org/2.7/library/logging.html#logrecord-attributes
FMT = '%(asctime)s [%(process)d] - %(filename)s:%(lineno)s - %(name)s - %(message)s'
FORMATTER = logging.Formatter(FMT, "%Y-%m-%d %H:%M:%S %Z")
LOGGER_MAP = {}
def getLogger(name = "action"):
    if name not in LOGGER_MAP:
        logFile = os.path.join("/root", "mytest", "edas.%s.trace" % name)
        if not os.path.isdir(os.path.dirname(logFile)):
            os.makedirs(os.path.dirname(logFile))
        handler = logging.handlers.RotatingFileHandler(logFile, maxBytes = 20*1024*1024, backupCount = 3)
        handler.setFormatter(FORMATTER)
        logger = logging.getLogger(name)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        LOGGER_MAP.update({name: logger})
    return LOGGER_MAP.get(name)
mylogger = getLogger("qiuxy");
mylogger.info("hello world");
# 输出结果：
# [root@iZwz93v6r4t2hixjvy9acoZ mytest]# pwd
# /root/mytest
# [root@iZwz93v6r4t2hixjvy9acoZ mytest]# cat edas.qiuxy.trace
# 2024-04-16 11:31:18 CST [17538] - 04_CommonLib.py:149 - qiuxy - hello world


print "======================================== 文件通配符glob库 =======================================";
# 需要import glob
# 找出通配符的文件
fileList = glob.glob("/root/my*/*.py");
for file in fileList:
    print "%s 文件大小为：%s； 文件创建时间为%s" % (file, os.path.getsize(file), os.path.getctime(file))

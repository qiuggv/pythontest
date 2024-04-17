# coding=utf-8
import argparse
import sys


def getParser():
    parser = argparse.ArgumentParser(description="EDAS agent actions executer")
    subparsers = parser.add_subparsers(help='Avilable sub-commands')
    parser_a = subparsers.add_parser('do', help='Execute actions with args')
    # class
    parser_a.add_argument("-a", "--action", help="Action name", action="store", type=str, required=True)
    # method
    parser_a.add_argument("-m", "--method", help="Method name", action="store", type=str)
    # clusterType
    parser_a.add_argument("-ct", "--cluster-type", help="cluster type", action="store", type=int)
    # 参数
    parser_a.add_argument("-p", "--params", help="Execute method with args", action="append", type=str)
    # json化参数
    parser_a.add_argument("-j", "--json", help="Parse json string as object, Attributes used by action", action="store",
                          type=str)
    # 文件参数
    parser_a.add_argument("-f", "--file", help="File absolute path. Action Attributes", action="store", type=str)
    # 超时时间
    parser_a.add_argument("-t", "--timeout", help="Action execute timeout", action="store", type=int)
    # async
    parser_a.add_argument("--async", help="Execute async", action="store_true")
    # local
    parser_a.add_argument("-q", "--quiet", help="Execute but not report to console", action="store_true")
    parser_b = subparsers.add_parser('version', help='Display script version')
    # 查看当前脚本版本
    parser_b.add_argument("-s", "--show", help="Show script version", action="store_true")
    parser_b.add_argument("--history", help="Show script version history", action="store_true")
    parser_b.add_argument("--rollback", help="Rollback to version", action="store", type=str)
    parser_c = subparsers.add_parser('actions', help='Display actions')
    # 显示所有可用的Action列表
    parser_c.add_argument("-l", "--all-actions", help="Display all avilebal actions", action="store_true")
    return parser


# 执行：
# [root@iZwz93v6r4t2hixjvy9acoZ mytest]# python 03_ArgsParseer.py do -a test -m testMethod
parser = getParser();
args = parser.parse_args();
# args.action: test
# args.method: testMethod
print("args.action: " + args.action);
print("args.method: " + args.method);

# sys.argv[0]: 03_ArgsParseer.py
# sys.argv[1]: do
# sys.argv[2]: -a
print ("sys.argv[0]: " + sys.argv[0]);
print ("sys.argv[1]: " + sys.argv[1]);
print ("sys.argv[2]: " + sys.argv[2]);
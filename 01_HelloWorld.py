# coding=utf-8
print "====================== hello world =========================="
print "hello world!"
print("hello world2")

print "====================== 语句和变量 =========================="
# 1、语句：不强制要求有;
# 2、变量：动态语言，不需要定义变量类型
a = "compare python with java"
print a

print "====================== 数字类型 =========================="
# 1、整数
numbers = 100;  # 直接整型值
numbers = int("100");  # 字符串转整型

# 2、浮点型
myFloat = 1.0;  # 浮点值直接值
myFloat = float("1.0");  # 字符串转浮点

# 3、null值
special = None;

print "====================== boolean类型 =========================="
# None是false
# 空字符串也是false
if special:
    print "special is None, and is true"
else:
    print "special is None, and is false"

str = "";
if str:
    print "str is empty, and is true";
else:
    print "str is empty, and is false";

print "====================== 控制流 =========================="
# 语句：不需要用{},而是用:和缩进

# if
condition = 10;
if condition > 10:
    print "condition > 10";
elif condition == 10:
    print "condition == 10";
else:
    print "condition < 10";

aVar = None;
# 判断是否为null
if aVar is None:
    print "aVar is None, and is true";

# while
while condition > 1:
    print "condition > 1, current value=", condition;
    condition = condition - 1;

# for
for i in range(0, 10):
    print "i=", i;


# switch
def f(x):
    return {
        1: 1,
        2: 2,
        3: 3
    }[x]


print f(condition)

print "====================== 类和继承 =========================="


# 1、关键字class是小写
class Animal():
    # 2、构造函数，必须显式传入self，类似java里面的this
    def __init__(self, name):
        self.name = name;

    # 3、实例方法，第一个参数必须是self
    def saySomething(self):
        print "I am an animal, my name is ", self.name;


# 4、继承时，父类放到括号里
class Dog(Animal):
    # 5、如果是有参构造函数，子类不强制要求提供有参构造函数，但java是要的

    # 6、重写父类的方法
    def saySomething(self):
        print "I am a dog, my name is ", self.name;


# 7、 创建类的对象实例，不需要new关键字
dog = Dog('zhangsan');
dog.saySomething();

print "====================== 反射 =========================="

# dir() 方法在 Python 中的作用是列出对象的所有属性和方法。它返回一个包含对象所有属性和方法名称的列表。
# 使用 dir() 方法列出对象的属性和方法
print("dog对象的所有属性和方法： %s" % dir(dog))
# 遍历所有的方法
for methodName in dir(dog):
    if methodName == "saySomething":
        method =getattr(dog, methodName);
        if callable(method):
            print methodName, " is callable";
            print "动态执行该方法，只需要在method对象后面加上()"
            # 并动态执行该方法，只需要在method对象后面加上()
            method();


print "====================== 文件处理 =========================="
# 使用内置函数open返回一个File对象，通过操作File对象的read()函数，读取文件内容
# open(name[, mode[, buffering]]) Open a file, returning an object of the file type described in section File Objects.
myFile = open("/root/mytest/readme.txt");
try:
    # file.read([size]) If the size argument is negative or omitted, read all data until EOF is reached.
    print myFile.read();
except Exception as e:
    print e;
finally:
    # 注意，这种写法必须手动关闭流
    myFile.close();


# with open(...) as fp 是Python中的一种文件操作语法，用于打开文件并确保文件在操作完成后被正确关闭。这种语法的优点包括：
#
# 代码简洁：使用 with 语句可以避免重复编写关闭文件的代码，使得代码更加简洁易读。
# 自动资源管理：with 语句会自动管理文件对象的生命周期，即使在处理文件过程中发生异常，也能保证文件最终会被关闭，避免了资源泄露的问题。
# 错误处理：如果在文件操作过程中出现错误，with 语句可以帮助更好地处理这些错误，因为它会确保文件在异常发生后被关闭。
# 具体来说，with open(...) as fp 语句的工作原理是：
#
# open(...) 是一个内置函数，用于打开文件。它接受文件路径和打开模式（如 'r' 表示读取）作为参数。
# as fp 部分是将打开的文件对象赋值给变量 fp，这样在接下来的代码块中就可以通过 fp 来操作文件了。
# with 语句的作用是创建一个上下文环境，在这个环境中执行代码。当代码块执行完毕后，with 语句会自动调用文件对象的 close() 方法来关闭文件，即使在代码块中有异常发生也会执行这个操作。
# 总的来说，with open(...) as fp 是一种推荐的文件操作语法，它不仅使得代码更加简洁，而且提高了代码的健壮性和可读性。
try:
    with open("/root/mytest/readme.txt", "r") as fp:
        print fp.read();
except Exception as e:
    print e;

print "====================== 异常处理 =========================="
# 1、try...except...finally

print "====================== 集合List =========================="
# list
aList = [];
aList.append("a");
aList.append("b");
aList.append("c");
aList.append("d");
print aList;
bList = list();
bList.append("a");
bList.append("b");
print bList;

print "====================== 字典dict，和JavaMap一样 =========================="
aMap = {};
aMap["a"] = "aValue";
print "aMap.get('a')=%s" % aMap.get('a');

aMap.update({"b": "bValue"});
print "aMap.get('b')=%s" % aMap.get('b');



print "====================== 元组Tuple =========================="
# Tuple类型
# 元组在Python中被定义为一种基本的数据类型，与列表（List）相似，它们都是用来存放一组有序的对象。然而，与列表不同的是，元组一旦创建后其元素就不能被修改，这意味着元组是不可变的。
# 与Java数组区别
# 1、Python的元组是不可变的，这意味着一旦创建就不能修改其内容。而Java的数组是可变的，可以对其进行添加、删除和更改操作。
# 2、Python的元组可以包含不同类型的元素，这是它与列表相似的地方。Java的数组也可以存储不同类型的数据，但这通常是通过使用Object类型的数组来实现的
# 3、在性能优化方面，Python的元组由于其不可变性，在某些情况下可以提供更快的处理速度。而Java的数组则可能需要更多的内存管理和类型检查工作

# 元组的创建通常是通过圆括号 () 来定义的，并且元素之间用逗号 , 分隔。例如，tup1 = (12, 34.56)
# <type 'int'> 注意，如果只有一个元素，则不是Tuple类型，如果只有一个元素，需要在后面加一个逗号
aTuple = (1);
print type(aTuple)
# <type 'tuple'>
aTuple1 = (1,);
print type(aTuple1)

aTuple2 = (1, 3);
print aTuple, aTuple1, aTuple2
# 尽管元组的元素不能被修改，但元组之间可以进行连接组合。例如，tup3 = tup1 + tup2 会创建一个新的元组，其中包含了 tup1 和 tup2 的所有元素
aTuple3 = aTuple1 + aTuple2
print aTuple3


print "====================== 函数定义、调用和返回值 =========================="

# 函数返回多个值时会将它们封装成一个元组返回
# 在Python中，如果函数需要返回多个值，这些值会被自动组合成一个元组（tuple），即使这个元组的括号被省略了。这种特性使得Python在处理多返回值时显得非常灵活和方便。具体来看：
# 1、返回值的封装：当使用return语句返回多个值时，Python内部会自动将这些值封装成一个元组。尽管在语法上可以省略元组的括号，但返回的结果仍然是一个元组对象。
# 2、解包操作：调用者可以选择将这个元组赋值给一个单独的变量，或者使用解包操作将其分解到多个变量中。例如，a, b, c = func()这样的语句就能够将返回的元组中的值分别赋给变量a、b和c。
# 3、不可变性：需要注意的是，元组本身是不可变的，这意味着一旦创建，元组内部的值就不能改变。但是，如果元组内部包含的是可变对象（如列表），那么这些可变对象的内容是可以更改的。
def func():
    return 1, 2, "hello"


a, b, c = func()
print(a)  # 输出：1
print(b)  # 输出：2
print(c)  # 输出："hello"


# 函数定义支持设置默认值
def greet(name='zhangsan', age=15):
    """Import a module.

    函数加注释。参考这里The 'package' argument is required when performing a relative import. It
    specifies the package to use as the anchor point from which to resolve the
    relative import to an absolute import.

    """
    print "Hello, %s! You are {%d} years old." % (name, age);


# 函数调用支持顺序传参，也支持关键字传参
# 使用顺序传参，当很多非必传项时，就很不方便
greet("Alice", 30);
# 使用关键字参数调用greet函数，只传指定的实参
greet(age=30);


# 函数里使用全局变量
# 在Python中，global关键字用于声明一个变量是全局变量。
# 当在函数内部需要修改全局变量的值时，需要使用global关键字声明该变量为全局变量，否则会创建一个新的局部变量。
default = None;
def getAnimal(name):
    global default;
    if default is not None:
        return default;
    default = Animal(name);
    return default;

singleton = getAnimal('singleton');
singleton.saySomething();

print "====================== 集合Set =========================="
aSet = set();
aSet.add("a");
aSet.add("b");
aSet.add("c");
print "--------aSet:--------";
for element in aSet:
    print element;

print "--------bSet:--------";
bSet = set(["a", "b", "d"]);
for element in bSet:
    print element;

print "--------并集--------";
cSet = aSet | bSet;
for element in cSet:
    print element;

print "--------交集--------";
dSet = aSet & bSet;
for element in dSet:
    print element;

print "--------不在bSet里的--------";
eSet = aSet.difference(bSet);
for element in eSet:
    print element;


print "====================== 异常处理 =========================="
# Python和Java在异常处理方面有相似之处，但也存在一些差异。
#
# 相同点：
# 异常处理机制：都采用了try-catch（或except）结构来捕获异常。
# 异常分类：都有对异常进行分类，并且提供了不同的异常类型。
# 异常链：都能够通过异常对象追踪到异常发生时的上下文信息。
# 异常传播：如果异常没有被内部的try-catch结构捕获，它们都会向上级调用方法传播。
# 不同点：
# 强制程度：Java对于检查型异常要求必须显式处理（通过try-catch或者throws声明），而Python在这方面更加灵活，不强制要求显式地处理异常，程序员可以根据需要决定是否捕获异常。
# 异常声明：Java需要在方法签名中声明可能抛出的检查型异常，而Python不需要这样的声明。
# 异常继承结构：Java中的异常体系结构较为复杂，有明确的层次划分，包括Error和Exception两大类，其中Exception又分为检查型和运行时异常。Python的异常结构相对简单，所有的异常都派生自BaseException类和其子类。
# 语法细节：在具体实现上，Java使用关键字throw来抛出异常，而Python则使用raise；在捕获异常时，Java使用catch而Python使用except。
# 执行块：Java中有finally块，无论异常是否被捕获，该代码块始终会被执行。Python也有类似的finally语句，但除此之外还有一个else块，它在没有异常发生时执行。
try:
    result = 10 / 0
except ZeroDivisionError as e:
    result = float('inf')
    print("Error: Division by zero is not allowed.")
    # pass
    # pass表示什么都不做
    # 可以继续往上抛
    # raise e;
finally:
    print("Finally block is executed.")



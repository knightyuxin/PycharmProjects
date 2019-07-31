import math
def my_abs(a=0):
    a=int(a)
    # return a if a>0 else -a
    return a if a>0 else -a
a=my_abs
b=abs
# print(b(-8))
# print(a(-9))
def add(x,y,f):
    return f(x)+f(y)
# print(add(-5,-6,a))
# def pf(x):
#     return x*x
# print(add(-5,-6,pf))
# print(add(-5,-6,lambda  x:x**2))
# print(math.sqrt(pow(-5,-6,a)))
# print(math.sqrt(pow(-5,-6,a)))

c=map(a,'1234')
from collections import Iterable,Iterator,Generator#判断可迭代,迭代器
# c.__next__()    #next(c)
# c.__le__()      #len(c)
# print(isinstance(c,Iterator))
# print(isinstance(c,Iterable))
# print(list(c))
# for i in c:
#     print(i)
# print(list(c))
# d=map(lambda x:x**2,(1,2,3,4,5))#求一个可迭代对象的平方
# print(list(d))
# print(str(d))
from functools import reduce
# def add(a,b,c=0):
#     print(a+b+c)
#     return a+b+c
# print(add(add(add(1,2),3),4))
# e=reduce(add,(1,2,3,4))
# print(e)
#使用reduce实现序列中所有数的乘积，要求使用lambda,reduce方法中第一个参数要求函数只能有两个确定参数
# def jc(a,b):
#     print(a*b)
# print(reduce(lambda x,y:x*y ,(1,2,3,4,5)))
#将第二个序列参数中的每两个元素放到第一个参数的函数中去执行，并将结果作为下一次函数调用的第一个参数
#将一个列表中的所有数字拼成一个数字返回，负数要绝对值，要求使用reduce与lambda[12,34,567,-8]12345678
# f=reduce(lambda a,b:abs(a)*10**len(str(abs(b)))+abs(b),[12,34,567,-8])
# g=reduce(lambda a,b:int(str(abs(a))+str(abs(b))),[12,34,567,-8])
# print(f)
# print(g)

#python中False的可能：数字0，0.0，-0.0，‘’，b‘’，()，[],{},{},None,False,...

#filter过滤器，参数一函数的返回值如果是True就取当前对象，否则丢失

#输出奇数
# h=filter(lambda a:a%2,range(1,21))
# print(list(h))
# #输出偶数
# i=filter(lambda a:a%2-1,range(1,21))
# print(list(i))
#输出素数
# j=filter(lambda a,b:a%b,range(1,21))
# print(list(j))

# from math import sqrt
# N = 100
# result =[]
# for num in range(2,N):  #range(2,N) 表示在到2~N之间
#     f = True
#     for snu in range(2,int(sqrt(num))+1):
#         if num %snu ==0:
#             f = False
#             break
#     if f:
#         result.append(num)
# print(result)

#求素数
# list=[]
# i=2
# for i in range (2,100):
#     j=2
#     for j in range(2,i):
#         if(i%j==0):
#             break
#     else:
#         list.append(i)
# print(list)

#求因数
# def sushu(number):
#     for i in range (2,int(number**0.5)+1):
#         if number%i==0:
#             return False
#     else:
#         return True
# n=int(input("请输入数字："))
# while True:
#      if sushu(n):
#          print(str(n)+"是素数")
#          break
#      else:
#          for j in range(2,n):
#              if sushu(j):
#                  if n%j==0:
#                      print(j)
#                      if sushu(n%j):
#                          exit()
#                      else:
#                          n=n%j

#求因数
# def ys(n):
#     l=[]
#     for i in range(1,n//2+1):
#         if n%i==0:l.append(i)
#     l.append(n)
#     return l
# print(ys(9))


#求素数
# def ys(n):
#     l=[]
#     for i in range(1,n//2+1):
#         if n%i==0:l.append(i)
#     l.append(n)
#     return not len(l) - 2
#     # return l #return not len(l)-2
# print(ys(1))
# i=filter(ys,range(1,100))
# print(list(i))

# s=filter(lambda x:not [x%i for i in range(2, int(math.sqrt(x))+1) if x%i ==0],range(2,101))

#重载
# def my_sum(*args):
#     return reduce(lambda a,b:a+b,args)
# a=(12,34,567,56,365)
# # print(my_sum(*a))
# #函数名称作为返回值，在需要执行的地方调用
# def my_sum1(*args):
#     def nb_sum():
#         return reduce(lambda a,b:a+b,args)
#     return nb_sum   #返回函数对象
# print(my_sum1(*a)())

#变量的使用按照就近原则寻找
#变量的赋值如果是操作全局变量，而非局部变量，就需要global声明
#global用于局部变量使用全局变量进行赋值操作
# a=[1]
# def my_gl():
#     a.append(2)
#     print(a)
#     return a
# print(my_gl())
# print(a)
# a=1
# def my_gl():
#     a=2 #赋值语句不往外找
#     print(a)
#     return a
# print(my_gl())
# print(a)


# name='python'
# def f1():
#     print(name)
# def f2():
#     name='linux'
#     f1()
# f2()

def f1(a):
    def f2(a=a):
        return a*a
    return f2
#lambda匿名函数，没有函数名的函数对象，冒号前面为参数，冒号后面为函数返回语句，
# 无需return，默认就有return，只能有一个语句
# la=lambda a:lambda a=a:a*a
# print(type(la))
# print(type(la(6)))
# print(type(la(7)()))
# print(la(9)())
# print(la(9)(8)) #9是默认参数

#构成闭包的条件： 函数的嵌套 内部函数使用外部函数的变量 外部函数返回内部函数
#内部函数先定义并返回，没有执行，当外部执行时以外部函数最终的变量值为准

# def count():
#     fs=[]
#     for i in range(4):
#         def f(i=i): #def f():
#             return i*i
#         fs.append(f)
#     return fs
# a=count()
# # print(a)
# for i in a:
#     print(i())
# print(a[0]())
# print(a[1]())
# print(a[2]())

# li=[lambda x=x:x for x in range(10)]
# def li():
#     for x in range(10):
#         def f(x=x):
#             return x
#     return f
# print(li)   #打印十个函数
# ret=li[0]()
# print(ret)

#当运行自己本身模块时，__name__=='__main__':
#否则__name__为当前模块名称
# import sys
# if __name__=='__main__':
#     print(__name__)
#     print(sys.__name__)

# def now():
#     print('2018-5-1')
# def log(f):
#     def wrap(*args,**kw):  # (*args,**kw):   #万能参数
#         print('call %s()' % f.__name__)
#         f(*args,**kw)  # now(*args,**kw) print('2018-5-1')
#         print('finish %s()' % f.__name__)
#     return wrap
# @log    # 装饰器，相当于now=log(now),装饰器定义在函数声明的上一行，将当前函数对象作为装饰器函数的参数
# #装饰器函数满足闭包条件，内部函数为一个包装器，外部函数返回内部函数
# def now():
    # print('2018-5-1')
# log(now)()#实际地层写法
# now=log(now) #now() 定义新的now函数
# now()   #执行新的now函数
# @log
# def yes(n=1):
#     print(n+100)
# yes()
# yes(5)
# print(now())
# print("********")
# print(log(now)()) #   @log
# print(now())


def log(text):
    def deco(f):
        def wrap(*args,**kw):
            print('call %s %s()'% (text,f.__name__))
            f()
            print('finish %s %s()' % (text, f.__name__))
            return wrap
        return deco
    @log('execute')#相当于now=log('execute')(now)
    def now():print('2018-5-1')
    now()

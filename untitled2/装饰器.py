def log(f):
    def wrap(*args,**kw):
        print('call %s()'%f.__name__)
        f()
        print('finish %s()'%f.__name__)
    return wrap
@log  #相当于now=log(now)   装饰器定义在函数声明的上面一行，将当前函数对象作为装饰器函数的参数
#装饰器函数满足闭包条件，内部函数为一个包装器，外部函数返回内部函数
def now():
    print('2018-5-1')
now()
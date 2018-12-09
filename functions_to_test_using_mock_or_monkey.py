import  os


def func(p):
    """
    Change the current directory. Uses hard coded os object.
    Testing the function requires patching os
    @param p: 
    @return: string done always
    """
    os.chdir(p)
    return "done"


def func_get():
    """
    function using a hard coded object to get the current directory.
    Testing the function requires patching os
    @return: current directory
    """
    pwd = os.getcwd()
    return pwd


class Operations(object):
    def add(self, v1, v2):
        return v1 + v2

    def sub(self, v1, v2):
        return v1 - v2
    
    
def execute_operations(op, v1, v2):
    """
    execute_operations an requires an external object and will call methods add and sub on this object.
    Testing this function only need to Mock this external object
    @param op: injected object operation
    @param v1: 
    @param v2: 
    @return: 
    """
    sub_res = op.sub(v1, v2)
    return op.add(v1, v2)


def func_throwing_up():
    try:
        val = 100/0
    except ZeroDivisionError:
        raise ValueError('Bad bad bad')



# -*- coding:utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import division
import inspect
import sys
import types


if sys.version_info < (3, 0):
    pyv = 2
else:
    pyv = 3

def is_class_method(name, val):
    if pyv == 2:
        return isinstance(val, types.MethodType) and val.im_self is None
    elif pyv == 3:
        # in python 2, a class method is unbound method type
        # in python 3, a class method is function type as well as a function
        raise Exception("python 3 only has function type and bound method type")

def is_instance_method(name, val):
    if pyv == 3:
        return inspect.ismethod(val)
    elif pyv == 2:
        return isinstance(val, types.MethodType) and val.im_self is not None

def is_pan_function(name, val):
    """detect pan-function which including function and bound method in python 3
    function and unbound method and bound method in python 2
    """
    return inspect.isfunction(val) or inspect.ismethod(val)

def print_exc_plus():
    """
    Print the usual traceback information, followed by a listing of all the
    local variables in each frame.
    """
    tb = sys.exc_info()[2]
    while 1:
        if not tb.tb_next:
            break
        tb = tb.tb_next
    stack = []
    f = tb.tb_frame
    while f:
        stack.append(f)
        f = f.f_back
    stack.reverse()
    traceback.print_exc()
    print("Locals by frame, innermost last")
    for frame in stack:
        print()
        print("Frame %s in %s at line %s" % (frame.f_code.co_name,
                                             frame.f_code.co_filename,
                                             frame.f_lineno))
        for key, value in frame.f_locals.items():
            print("\t%20s = " % key, end='')
            # We have to be careful not to cause a new error in our error
            # printer! Calling str() on an unknown object could cause an
            # error we don't want.
            try:
                print(value)
            except:
                print("<ERROR WHILE PRINTING VALUE>")



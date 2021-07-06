from tkinter import *
import matplotlib.pyplot as plt
from tkinter import messagebox
from math import exp
import numpy as np

def f(x):
    return x-exp(x)/5

def f1(x):
    return exp(x)/5

def df(x):
    return 1-exp(x)/5

def list_get(rang):
    try:
        list_a_b = [float(x) for x in rang.strip().split()]

        if len(list_a_b) == 0 or len(list_a_b) > 2:
            return -1
        return list_a_b

    except ValueError:
        return -1

def iteration(a1,b1,max_iter,eps):
    error =0
    iter_n = 0
    x0=a1
    x1=f1(x0)
    while abs(x1-x0) >= eps:
        x0=x1
        x1=f1(x0)
    iter_n += 1    
    if iter_n > max_iter:
        error =1
    return x1,iter_n,error

def Errorvalue(range_, shag_,eps_,iter_):
    a=0
    range_list = list_get(range_)
    a=range_list[0]
    b = range_list[1]
    if a >= b:
        a=1

    shag = float(shag_.strip())
    if shag < 0:
        a=1

    eps = float(eps_.strip())
    if not (0 < eps < shag / 2):
        a=1

    iterr = int(iter_.strip())
    if iterr < 0:
        a=1
    return a

def calc_roots(range_, shag_,eps_,iter_):
    range_list = list_get(range_)
    a=range_list[0]
    b = range_list[1]
    shag = float(shag_.strip())
    eps = float(eps_.strip())
    iterr = int(iter_.strip())
    if Errorvalue(range_, shag_,eps_,iter_) == 1:
        return -1
    else:
        try:
            n=1
            it = 0
            err = 0
            n_list = []
            x_list = []
            fx_list = []
            left_l = []
            right_l = []
            iter_list = []
            error_list = []

            while a+shag*(n-1)<b:
                left = a+shag*(n-1)
                right = a+shag*(n) if a+shag*(n)<b else b
                if f(left)*f(right) <= 0:
                    x,it,err = iteration(left,right,iterr,eps)
                else:
                    n += 1
                    continue

                if (err == 0 or err==1) and (len(x_list) == 0 or abs(x - x_list[-1]) > 2 * eps):
                    n_list.append(n)
                    x_list.append(x)
                    fx_list.append(f(x))
                    left_l.append(left)
                    right_l.append(right)
                    iter_list.append(it)
                    error_list.append(err)                
                n+=1
            print(n_list)
            print(x_list)
            print(fx_list)
            print(left_l)
            print(right_l)
            print(iter_list)
            print(error_list)
        except:
            return -1
range_=input()
shag_=input()
eps_=input()
iter_=input()
calc_roots(range_, shag_,eps_,iter_)
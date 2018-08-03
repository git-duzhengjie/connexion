# coding:utf-8
# python version:
# author: duzhengjie
# date: 2018/8/3 14:19
# description:

# ©成都爱车宝信息科技有限公司版权所有


def say_hello(name=None):
    return {"message": "Hello {}, from API!".format(name or "")}

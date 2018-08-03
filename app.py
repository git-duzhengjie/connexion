# coding:utf-8
# python version: 3.6
# author: duzhengjie
# date: 2018/8/3 13:47
# description:

# ©成都爱车宝信息科技有限公司版权所有
import connexion


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, specification_dir='swagger/')
    app.add_api('my_api.yaml')
    app.run(port=5000)
from app import app
import json
import sys
import os
from flask import Flask,request,url_for

reload(sys) 
sys.setdefaultencoding('utf8')

def valid_int(value):
    try:
        value= int(value)
        if value>0 and  value<9223372036854775807:
            return True
        else:
            return False
    except ValueError:
        return False
    return True
def valid_string(value):
    if isinstance(value,basestring):
        if len(value.strip('/"'))<=0:
            return False
        else:
            return True
    else:
        return False


@app.route('/')
@app.route('/shopee/test')
def index():
    ret_info={}
    ret_info['err_code']="11"
    ret_info['err_msg']="system error"
    ret_info['reference']="null"

    input_args = request.args.items()
    input_a = request.args.get('a','')
    input_b = request.args.get('b','')

    args_num = len(input_args)

    if args_num!=2 or not input_a  or not input_b:
        ret_info['err_code']="21"
        ret_info['err_msg']="empty or wrong param"
        ret_info['reference']="null"
    else:
        if valid_int(input_a) and valid_string(input_b):
            ret_info['err_code']="0"
            ret_info['err_msg']="success"
            ret_info['reference']="param is:a={0} and b={1}".format(input_a,input_b)
        else:
            ret_info['err_code']="21"
            ret_info['err_msg']="empty or wrong param"
            ret_info['reference']="null"
    ret_json = json.dumps(ret_info)
    return ret_json

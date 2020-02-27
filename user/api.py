# from django.shortcuts import render

from lib.http import render_json
from common import error
from user.logic import send_verify_code, check_vcode
from user.models import User

def get_verify_code(request):
    '''手机注册'''
    phonenum = request.GET.get('phonenum')
    send_verify_code(phonenum)
    return render_json(None, 0)
    
def login(request):
    '''短信验证登陆'''
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    if check_vcode(phonenum, vcode):
    	# 获取用户
    	user, created = User.object.get_or_create(phonenum=phonenum)
    	
    	# 记录用户状态
    	request.session['uid'] = user.id
    	return render_json(user.to_dict(), 0)
    else:
    	return render_json(None, error.VCODE_ERROR)

    cache.get(key)

def get_profile(request):
    '''获取个人资料'''

    pass

def modify_profile(request):
    '''修改个人资料'''
    pass

def upload_avatar(request):
    '''头像上传'''
    pass

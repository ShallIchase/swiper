
from user.models import User
from lib.http import render_json
from common import error

class AuthMiddleware(MiddlewareMixin):
	'''用户登录验证中间件'''

	WHITE_LIST = [
		'api/user/verify',
		'api/user/login',
	]

	def process_request(self, request):
		# 如果请求的 URL 在白名单内，直接跳过检查
		for path in self.WHITE_LIST:
			if request.path in self.WHITE_LIST:
				return
		# 进行登录检查
		uid = request.session.get('uid')
		if uid:
			try:
				request.user = User.objects.get(id=uid)
				return 
			except User.DoesNotExist:
				request.session.flush()
		return render_json(None, code=error.LOGINERROR)
		
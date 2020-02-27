
from user.models import User
from lib.http import render_json
from common import error

class AuthMiddleware(MiddlewareMixin):
	'''用户登录验证中间件'''
	def process_request(self, request):
		uid = request.session.get('uid')
		if uid:
			try:
				request.user = User.objects.get(id=uid)
				return 
			except User.DoesNotExist:
				request.session.flush()
		return render_json(None, code=error.LOGINERROR)
		
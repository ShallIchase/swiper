#!/user/bin/env/ python

import os
import sys
import random

import django

# 设置环境
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MOUDLE", "swiper.settings")
django.setup()

from user.models import User

last_names = (
	'赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨'
	'朱秦尤许何吕施张孔曹严华金魏陶姜'
	'戚谢邹喻柏水窦章云苏潘葛奚范彭郎'
	'鲁韦昌马苗凤花方俞任袁柳酆鲍史唐'
	'费廉岑薛雷贺倪汤滕殷罗毕郝邬安常'
	'乐于时傅皮卞齐康伍余元卜顾孟平黄'
)

fisrt_names = {
	'Male': [
		'澄邈','德泽','海超','海阳','海荣',
		'海昌','瀚钰','瀚文','涵亮','浩歌',
		'浩邈','浩气','浩思','曜灿','曜瑞',
		'海逸','浩广','智伟','永昌','子昂',
		'昊磊','昊东','鸿晖','绍晖','文景'
	],
	'Female': [
		'恨桃','依秋','依波','香巧','紫萱',
		'亦巧','青易','冰真','白萱','友安',
		'紫薇','思菱','忆文','翠巧','书文',
		'雨珍','幻丝','代梅','盼曼','妙之',
		'凌青','谷芹','雁桃','映雁','书兰'
	]
}


def rand_name():
	last_name = random.choice(last_names)
	sex = random.choice(['Male', 'Female'])
	fisrt_name = random.choice(fisrt_names[sex])
	return ''.join([last_name, fisrt_name]), sex


# 创建初始用户
for i in range(1000):
	name, sex = rand_name()
	try:
		User.objects.create(
			phonenum='%s' % random.randrange(21000000000,21900000000 ),
			nickname=name,
			sex=sex,
			birth_year=random.randint(1980, 2002),
			birth_month=random.randint(1, 12),
			birth_day=random.randint(1, 28),
			location=random.choice(['北京', '上海', '深圳', '成都', '武汉', '西安', '沈阳'])
		)
		print('created: %s %s' % (name, sex))
	except django db.utils.IntegrityError:
		pass
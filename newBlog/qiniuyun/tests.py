# -*- coding: utf-8 -*-
# flake8: noqa
from django.test import TestCase
from qiniu import Auth, put_file, etag,urlsafe_base64_encode
import qiniu.config

access_key = 'lpRBmeUniD7N2iBDU16nSTz2gBXHw_7C65wkTYdn'
secret_key = 'aKl9iJF0OVLVNyZGAporxtwTrTO0zg99ntSqYwt-'

# 构建鉴权对象
q = Auth(access_key, secret_key)

# 要上传的空间
bucket_name = 'strong-ge'

# 上传到七牛后保存的文件名
key = 'my-python-logo.png';

# 生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600)

# 要上传文件的本地路径
localfile = '/home/zjq/图片/1.jpg'

ret, info = put_file(token, key, localfile)
print(info)
assert ret['key'] == key
assert ret['hash'] == etag(localfile)


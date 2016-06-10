# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from qiniu import Auth, put_file, etag,urlsafe_base64_encode

# Create your views here.
access_key = 'lpRBmeUniD7N2iBDU16nSTz2gBXHw_7C65wkTYdn'
secret_key = 'aKl9iJF0OVLVNyZGAporxtwTrTO0zg99ntSqYwt-'
bucket_name = 'strong-ge'


def index(request):
    return render(request, 'qiniuyun/index.html')


def upload(request):
    my_file = request.FILES['file']
    print my_file
    result, new_name = profile_upload(file)
    status_dict = {'data': 'ok'}
    return JsonResponse(status_dict)


def profile_upload(file):
    '''文件上传函数'''
    if file:
        path=settings.MEDIA_ROOT
        suffix=(file.name).split()[-1]
        file_name=str(int(time.time()))+suffix
        path_file=os.path.join(path,file_name)
        print(path_file)
        fp = open(path_file, 'wb')
        for content in file.chunks():
            fp.write(content)
        fp.close()
        return (True,file_name) #change
    return (False,file_name)   #change

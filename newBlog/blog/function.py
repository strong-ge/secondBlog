# coding:utf-8
from blog.models import Blog
# 按月归档


def get_blog_by_month():
    post_date = Blog.objects.datetimes('publish_time', 'month')
    date_list = []
    for i in range(len(post_date)):
        date_list.append([])
    for i in range(len(post_date)):
        current_year = post_date[i].year
        current_month = post_date[i].month
        temp_article = Blog.objects.filter(update_time__year=current_year).filter(update_time__month=current_month)
        temp_num = len(temp_article)
        date_list[i].append(post_date[i])
        date_list[i].append(temp_article)
        date_list[i].append(temp_num)
    return date_list

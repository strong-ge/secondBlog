from django.db import models


class Tag(models.Model):
    """docstring for Tags"""
    tag_name = models.CharField(max_length=20, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tag_name


class Blog(models.Model):
    """docstring for Blogs"""
    title = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    blog = models.ForeignKey(Blog, related_name="images")
    top = models.BooleanField(default="false")
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

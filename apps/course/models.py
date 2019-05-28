from django.db import models
from datetime import datetime


# 课程表
class Course(models.Model):
    name = models.CharField(max_length=30, default="",verbose_name=u"课程名称")
    detail = models.CharField(max_length=300, default="",verbose_name=u"课程描述")
    notice = models.CharField(default="", max_length=300, verbose_name=u"课程须知")
    # image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"封面图", max_length=100)
    degree = models.CharField(verbose_name=u"难度",default=u"", choices=(("easy", "初级"), ("ordinary", "中级"), ("advanced", "高级")), max_length = 20)
    category = models.CharField(default=u"后端开发", max_length=20, verbose_name=u"课程类别")
    duration = models.IntegerField(default=0, verbose_name=u"课程时长")
    tag = models.CharField(default="", verbose_name=u"课程标签", max_length=10)
    learn_num = models.IntegerField(default=0, verbose_name=u'学习人数')
    collect_num = models.IntegerField(default=0, verbose_name=u'收藏人数')
    click_num = models.IntegerField(default=0, verbose_name=u"点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_course_chapter(self):
        # 获取课程所有章节
        return self.chapter_set.all()


# 章节表
class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"章节名")
    learn_minutes = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_chapter_video(self):
        # 获取章节下所有视频的信息
        return self.video_set.all()


# 视频表
class Video(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, verbose_name=u"章节")
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    learn_minutes = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    url = models.CharField(max_length=200, default="", verbose_name=u"访问地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

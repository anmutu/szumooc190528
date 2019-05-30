from django.shortcuts import render

from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

from .models import Course, Video
from user.models import CourseComments


class ChapterListView(View):
    """
    课程章节信息
    """

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        return render(request, "course-chapter-video.html", {
            "course": course,
        })


class VideoPlayView(View):
    """
    视频播放
    """

    def get(self, request, video_id):
        video = Video.objects.get(id=int(video_id))
        course = video.chapter.course
        return render(request, "video-play.html", {
            "course": course,
            "video": video,
        })


class GetCommentsView(View):
    """
    获取课程评论数据
    """

    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        all_comments = CourseComments.objects.filter(course=course).order_by("-id")
        return render(request, "course-comment.html", {
            "course": course,
            "all_comments": all_comments
        })


class AddCommentView(View):
    """
    增加课程评论
    """
    def post(self, request):
        # if not request.user.is_authenticated():
        #     # 判断用户登录状态
        #     return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')

        course_id = request.POST.get("course_id", 0)
        comments = request.POST.get("comments", "")
        if int(course_id) > 0 and comments:
            course_comments = CourseComments()
            course = Course.objects.get(id=int(course_id))
            course_comments.course = course
            course_comments.comments = comments
            course_comments.user = request.user
            course_comments.save()
            return HttpResponse('{"status":"success", "msg":"评论添加成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"评论添加失败"}', content_type='application/json')


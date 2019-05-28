from django.shortcuts import render

from django.shortcuts import render
from django.views.generic.base import View

from course.models import Video
from .models import Course, Video


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

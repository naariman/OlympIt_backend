from django.http import JsonResponse
from django.views import View
from .models import Lesson
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def lessons_by_type(request, lesson_type):
    lessons = Lesson.objects.filter(type=lesson_type)

    lessons_list = []
    for lesson in lessons:
        lesson_data = {
            "id": lesson.id,
            "name": lesson.name,
            "icon_url": lesson.icon_url,
            "type": lesson.type
        }
        lessons_list.append(lesson_data)

    return JsonResponse(lessons_list, safe=False)

# middleware.py

from django.conf import settings
from django.http import Http404,HttpResponse
import os

class NoStaticMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if settings.DEBUG and request.path.startswith(settings.STATIC_URL):
            static_file_path = os.path.join(settings.STATIC_ROOT, request.path[len(settings.STATIC_URL):])
            if os.path.exists(static_file_path):
                with open(static_file_path, 'rb') as f:
                    return HttpResponse(f.read(), content_type='application/octet-stream')
            else:
                raise Http404()
        else:
            return self.get_response(request)

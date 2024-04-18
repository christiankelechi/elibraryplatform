
from rest_framework import routers
from core_app_root.ai_applications.viewsets.booksummarizer import BookSummarizerViewset

router=routers.SimpleRouter()
router.register(r'summarize',BookSummarizerViewset,basename='user')


urlpatterns=[
    *router.urls
]

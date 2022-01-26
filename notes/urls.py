from django.urls import path, include
from rest_framework import routers

from .views import AllNotesViewSet, ListDetailsViewSet, TextNotesViewSet, LinkNotesViewSet

router = routers.DefaultRouter()
router.register('', AllNotesViewSet)
router.register('listnote', ListDetailsViewSet)
router.register('textnote', TextNotesViewSet)
router.register('linknote', LinkNotesViewSet)
urlpatterns = router.urls

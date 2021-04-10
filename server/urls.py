from rest_framework import routers
from server.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.urls import path, include

router = routers.DefaultRouter()
#router.register(r'login', LoginViewSet)
router.register(r'store', StoreViewSet)
router.register(r'bigmarket', BigmarketViewSet)

urlpatterns = router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = [
    path('/create', CreateView.as_view()),
    path('/login', LoginView.as_view())
]

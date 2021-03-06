from django.urls import path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView, FormuleView, DarkView, SuccessView, FormView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('formules/', FormuleView.as_view(), name='formules'),
    path('dark/', DarkView.as_view(), name='dark'),
    path('connexion/', FormView.as_view(), name='connexion'),
    path('success/', SuccessView.as_view(), name='success'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

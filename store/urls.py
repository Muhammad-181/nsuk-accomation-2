from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import frontpage, homepage
from .import views




urlpatterns = [
    path('home/', frontpage, name='frontpage'),
    path('', homepage, name='homepage'),
    # path('search/', views.search, name='search-url'),
    path('<slug:slug>/', views.instituition_detail, name='instituition_detail-page'),
    path('<slug:instituition_slug>/<str:id>/', views.property_detail, name='property_deatil-page'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

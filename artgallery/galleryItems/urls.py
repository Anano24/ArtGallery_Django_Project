from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'galleryItems'

urlpatterns = [
    path('', views.IndexView.as_view(), name='homepage'),
    path('add_item/', views.AddItemView.as_view(), name='add_item'),
    path('detailed_view/<int:pk>', views.ItemDetailView.as_view(), name='detailed_item'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path, include

urlpatterns = [
    path('post/', include('post.apis.urls')),
]

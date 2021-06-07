"""foss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.views.static import serve
from django.conf.urls.static import static
from django_comments.feeds import LatestCommentFeed


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('comments/', include('django_comments.urls')),
    path('feeds/latest/', LatestCommentFeed()),
    path('', include('visitorsite.urls')),
    # path('media/<path>', serve,{'document_root': settings.MEDIA_ROOT}),
]

urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
"""project URL Configuration

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
from django.contrib import admin
from django.conf.urls import handler404, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse_lazy
from django.views.generic import RedirectView

urlpatterns = [

    # admin/
    re_path(r'^admin/', admin.site.urls),

    # dashboard/
    re_path(r'^dashboard/', include('dashboard.urls', namespace='dashboard')),

    # Redirect all other urls
    re_path(r'^.*$', RedirectView.as_view(url=reverse_lazy('dashboard:index'))),

]

#handler404 = 'dashboard.views.handle404'
#handler500 = 'dashboard.views.handle500'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
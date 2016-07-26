"""otokon_archive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy
from sponsorship.views import custom_login, custom_logout

urlpatterns = [
    url(r'^$', RedirectView.as_view(url=reverse_lazy("organization_list")), name="base"),
    url(r'^admin/', admin.site.urls),
    url(r'^sponsorship/', include("sponsorship.urls")),
    url(r'^login/$',
        custom_login,
        name="login"),
    url(r'^logout/$',
        custom_logout,
        name="logout"),
    #url(r'^', RedirectView.as_view(url=reverse_lazy("organization_list"))),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy
from sponsorship.views import custom_login, custom_logout
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(TemplateView.as_view(template_name="home.html")), name="base"),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^sponsorship/', include("sponsorship.urls")),
    url(r'^robotics/', include("robotics.urls")),
    url(r'^login/$',
        custom_login,
        name="login"),
    url(r'^logout/$',
        custom_logout,
        name="logout"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

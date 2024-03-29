from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from . import settings

urlpatterns = [
    path("", TemplateView.as_view(template_name="frontpage.html"), name="frontpage"),
    path("erad/", include("erad.urls")),
    path("grant/", include("grant.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]

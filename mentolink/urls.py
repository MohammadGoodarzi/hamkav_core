from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from search import views as search_views

from .api import api


urlpatterns = [
    path("hamkav-admin/", admin.site.urls),
    path("wagtail-admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),

    path('accounts/', include('HamkavAuth.urls',namespace='HamkavAuth')),
    path('blog/', include('HamkavBlog.urls',namespace='HamkavBlog')),
    path('edu/', include('HamkavEduShop.urls',namespace='HamkavEduShop')),
    path('db/', include('HamkavDbManagement.urls',namespace='db')),

    path("api/", api.urls),
    
    #  path('markdownx/', include('markdownx.urls')), #Django Markdownx


]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns = urlpatterns + [
        path('__debug__/', include('debug_toolbar.urls')), #django-debug-toolbar
        
    ]



urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]

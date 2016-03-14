from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from apps.website.views import *
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePage.as_view(), name='home'),
    url(r'^contact-us/$', ContactUsPage.as_view(), name='contact-us'),
    url(r'^python-django/$', PythonDjangoPage.as_view(), name='python-django'),
    url(r'^javascript/$', JavascriptPage.as_view(), name='javascript'),
    url(r'^cross-platform/$', CrossPlatformPage.as_view(), name='cross-platform'),
    url(r'^whoweserve/$', WhoweServePage.as_view(), name='whoweserve'),
    url(r'^customer-success/$', CustomerSuccessPage.as_view(), name='customer-success'),
    url(r'^users/', include('apps.profiles.urls', namespace='profiles')),
    url(r'^blogs/', include('apps.blogs.urls', namespace='blogs')),
    url(r'^customer_contact/', customer_contact, name='customer_contact'),
    url(r'^admin/', include(admin.site.urls))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('',
          (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
          'document_root': settings.STATIC_ROOT}))


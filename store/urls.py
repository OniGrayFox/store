"""store URL Configuration

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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

from products.views import IndexView
from order.views import stripe_webhook_view

static_urlpatterns = [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(extra_context={'title':'store'}), name='index'),
    #path("", include(static_urlpatterns)),
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
    path('accounts/', include('allauth.urls')),
    path('orders/', include('order.urls', namespace='order')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('webhook/stripe/', stripe_webhook_view, name='stripe_webhook')
]

if settings.DEBUG:
    import mimetypes

    mimetypes.add_type("application/javascript", ".js", True)

    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^view-time$', views.view_time),
    url(r'^channel/1$', views.channel, name='channel'),
    url(r'^user-test$', views.user_test, name='user-test'),
    url(r'^create-account$', views.create_account, name='create-account'),
    url(r'^login', views.login, name='login'),
    url(r'^account-created$', views.account_created, name='account-created'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt',
        content_type='text/plain')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

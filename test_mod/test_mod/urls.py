from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from test_table import views as table_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("table/", table_views.table_view, name = 'test_table-view'),
    path("register/", user_views.register, name='register'),
    path("login/", auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path("profile/", user_views.profile, name='profile'),
    path("", include('test_db.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

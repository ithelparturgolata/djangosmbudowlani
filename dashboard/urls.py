from django.urls import path, include
import dashboard.views
from dashboard import views
# from rss import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name=""),
    # path("register", views.register, name="register"),
    # path("login", views.login_view, name="login"),
    # path("logout", views.logout_view, name="logout"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("dashboard_main", views.dashboard_main, name="dashboard_main"),
    path("iso_iso", views.iso_iso, name="iso_iso"),
    path("iso_polityka", views.iso_polityka, name="iso_polityka"),
    path("iso_badanie", views.iso_badanie, name="iso_badanie"),
    path("wspolnoty", views.wspolnoty, name="wspolnoty"),
    path("kontakt", views.kontakt, name="kontakt"),
    path("spoldzielnia_organy", views.spoldzielnia_organy, name="spoldzielnia_organy"),
    path("spoldzielnia_radanadzorcza", views.spoldzielnia_radanadzorcza, name="spoldzielnia_radanadzorcza"),
    path("spoldzielnia_zarzad", views.spoldzielnia_zarzad, name="spoldzielnia_zarzad"),
    path("spoldzielnia_radyosiedli", views.spoldzielnia_radyosiedli, name="spoldzielnia_radyosiedli"),
    path("spoldzielnia_administracje", views.spoldzielnia_administracje, name="spoldzielnia_administracje"),
    path("spoldzielnia_akty", views.spoldzielnia_akty, name="spoldzielnia_akty"),
    path("spoldzielnia_rodo", views.spoldzielnia_rodo, name="spoldzielnia_rodo"),
    path("tu_mieszkam", views.tu_mieszkam, name="tu_mieszkam"),
    path("przetargi", views.przetargi, name="przetargi"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

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
    path("spoldzielnia_statut", views.spoldzielnia_statut, name="spoldzielnia_statut"),
    path("spoldzielnia_samorzad", views.spoldzielnia_samorzad, name="spoldzielnia_samorzad"),
    path("spoldzielnia_ue", views.spoldzielnia_ue, name="spoldzielnia_ue"),
    path("spoldzielnia_kalendarium", views.spoldzielnia_kalendarium, name="spoldzielnia_kalendarium"),
    path("tu_mieszkam", views.tu_mieszkam, name="tu_mieszkam"),
    path("pliki", views.pliki, name="pliki"),
    path("przetargi_details/<int:pk>", views.przetargi_details, name="przetargi_details"),
    path("przetargi", views.przetargi, name="przetargi"),
    path("aktualnosci_details/<int:pk>", views.aktualnosci_details, name="aktualnosci_details"),
    path("aktualnosci", views.aktualnosci, name="aktualnosci"),
    # path("galeria_details/<int:pk>", views.galeria_details, name="galeria_details"),
    # path("galeria", views.galeria, name="galeria"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

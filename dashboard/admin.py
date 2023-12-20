from django.contrib import admin
from .models import TuMieszkam
from .models import Przetargi
from .models import Kalendarium
from .models import Pliki
from .models import Aktualnosci
# from .models import Galeria

admin.site.register(TuMieszkam)
admin.site.register(Przetargi)
admin.site.register(Kalendarium)
admin.site.register(Pliki)
admin.site.register(Aktualnosci)
# admin.site.register(Galeria)
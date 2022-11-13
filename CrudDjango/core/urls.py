from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import static
from .views import  pagg, pagg2, crear, editar, form, libros,eliminar


urlpatterns = [
    path('', pagg,name="pagg"),
    path('tt/', pagg2,name="pagg2"),
    path('eliminar/<int:id>', eliminar, name='eliminar' ),
    path('crear/', crear,name="crear"),
    path('editar/', editar,name="editar"),
    path('editar/<int:id>', editar,name="editar"),
    path('form/', form,name="form"),
    path('index/', libros,name="index"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )

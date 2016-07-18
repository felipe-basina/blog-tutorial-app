from django.contrib import admin

# Register your models here.
from .models import Post
# Adicionado o modelo ao admin para visualizar na pagina de administracao
admin.site.register(Post)

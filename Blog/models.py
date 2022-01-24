from django.contrib import admin
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import PROTECT
from django.forms import ImageField
# Create your models here.
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

import PIL



class Reporter(models.Model):
    nome = models.CharField(max_length=50)
    entrou_em = models.DateField(auto_now_add=True)
    email = models.EmailField(max_length=254)
    link_social = models.CharField(max_length=100)
    resumo = models.TextField()
    foto_de_perfil = models.ImageField(upload_to="uploads/")
    
    def __str__(self):
        return self.nome
    
    def get_nome(self):
        return self.nome
    
    def get_data_entrou_em(self):
        return self.entrou_em
    
    def get_email(self):
        return self.email
    
    def get_link_social(self):
        return self.link_social
    
    def get_foto(self):
        return self.foto
    
    def get_foto_de_perfil(self):
        return self.foto_de_perfil
    
    def get_resumo(self):
        return self.resumo
    #def get_absolute_url(self):
    #   return reverse("Post_detail", kwargs={"pk": self.pk})

class Post(models.Model):
    titulo = models.CharField(max_length=255)
    #imagem_banner = models.ImageField(upload_to ='uploads/')
    #resumo = models.CharField(max_length=255)
    resumo = RichTextField()
    conteudo = RichTextUploadingField()
    #imagem_banner = models.ImageField(None,upload_to=None, height_field=None, width_field=None, max_length=None)
    #imagem_banner = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    #upload = models.ImageField(upload_to ='uploads/')
    #conteudo = RichTextField()
    #conteudo = models.RichTextUploadingField(config_name='portal_config')
    #autor = models.ForeignKey(User, on_delete=models.PROTECT)
    criado_em = models.DateField(auto_now_add=True)#para que serve _("")
    banner = models.ImageField(upload_to='media/')
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)#Testar essa funcionalidade depois

    def __str__(self):
        return self.titulo

    def get_titulo(self):
        return self.titulo

    def get_resumo(self):
        return self.resumo

    def get_data_criacao(self):
        return self.criado_em

    def get_autor(self):
        return self.autor
    
    def get_banner_imagem(self):
        return self.banner
    
    def get_conteudo(self):
        return self.conteudo

    def get_reporter(self):
        return self.reporter


class Celebrity(models.Model):#Modelo Texto 
    name = models.CharField(max_length=255)

class Image(models.Model):#Modelo da imagem
    celebrity = models.ForeignKey(Celebrity,on_delete=PROTECT)#linkada para qual Celebrity
    image = models.ImageField()

class InlineImage(admin.TabularInline):
    model = Image

class CelebrityAdmin(admin.ModelAdmin):
    inlines = [InlineImage]

from django.db import models

# Create your models here.
class Content(models.Model):
    pt_content = models.TextField("Texto Português:")
    eng_content = models.TextField("Texto Inglês:")
    identifier = models.CharField(max_length=30)
    def __str__(self):
        return self.pt_content
    class Meta:
        verbose_name = 'Texto'
        verbose_name_plural = 'Textos'

class Image(models.Model):
    owner = models.CharField("Nome: ",default="Por definir",max_length=30)
    image = models.ImageField("Logo: ",upload_to='images/')
    def __str__(self):
        return self.owner
    class Meta:
        verbose_name = 'Imagem SlideShow'
        verbose_name_plural = 'Imagens SlideShow'


class Portfolio(models.Model):
    TAG_CHOICES = [
        ('outros', 'Outros'),
        ('estudos', 'Mercado'),
        ('comunicacao', 'Comunicação'),
        ('marketing', 'Marketing'),
        ('comercial', 'Comercial'),
        ('estudos comercial', 'Mercado e Comercial'),
        ('estudos comunicacao', 'Mercado e Comunicação'),
        ('comunicacao marketing', 'Comunicação e Marketing'),
    ]
    name = models.CharField("Nome: ",default="Por definir",max_length=30)
    tag = models.CharField(choices=TAG_CHOICES, max_length=100,default="outros")
    image = models.ImageField("Logo: ",upload_to='images/')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Imagem Portfolio'
        verbose_name_plural = 'Imagens Portofolio'
        

class Testimony(models.Model):
    link = models.CharField("Link: ", max_length=300)
    subtitle = models.CharField("Subtítulo: ", max_length=30)
    def __str__(self):
        return self.subtitle
    class Meta:
        verbose_name = 'Link para os testemunhos'
        verbose_name_plural = 'Links para os testemunhos'

from django.db import models


class Foto(models.Model):
    titulo = models.CharField(
        max_length=100,
        verbose_name='Título'
    )

    imagem = models.ImageField(
        upload_to='galeria/',
        verbose_name='Imagem'
    )

    descricao = models.TextField(
        blank=True,
        null=True,
        verbose_name='Descrição'
    )

    criado_em = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Nombre(models.Model):
    nombre = models.CharField(_("Nombre"), max_length=50)
    edad = models.PositiveIntegerField(_("Edad"))

    class Meta:
        verbose_name = _("Nombre")
        verbose_name_plural = _("Nombres")

    def __str__(self):
        return self.name

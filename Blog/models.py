from django.db import models

# Create your models here.
class Locations(models.Model):
    name = models.CharField(unique=True, default="Unknown", verbose_name="Nama Lokasi", max_length=225)

    def __str__(self):
        return self.name


class Destinations(models.Model):
    dest_name = models.CharField(max_length=225 ,verbose_name="Nama Wisata", unique=True, default="Unknown")
    dest_location = models.ForeignKey(Locations, on_delete=models.CASCADE, verbose_name="Lokasi Wisata")

    def __str__(self):
        return self.dest_name


class Article(models.Model):
    dest_name = models.OneToOneField(Destinations, on_delete=models.CASCADE, verbose_name="Nama Wisata")
    dest_desc = models.TextField(verbose_name="Deskripsi", null=True)

    def __str__(self):
        return self.dest_name.dest_name
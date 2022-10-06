from django.db import models

# Create your models here.

class Dosen(models.Model):
    nama = models.CharField(max_length=50)
    nip = models.CharField(max_length=50)
    tanggal_lahir = models.CharField(max_length=50)
    photo = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=50)
    prodi = models.CharField(max_length=50)
    alamat_rumah = models.CharField(max_length=50)

    def ___str___(self):
        return self.nama

class Tendik(models.Model):
    nama = models.CharField(max_length=50)
    nip = models.CharField(max_length=50)
    tanggal_lahir = models.CharField(max_length=50)
    photo = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    unit = models.CharField(max_length=50)
    alamat_rumah = models.CharField(max_length=50)

    def ___str___(self):
        return self.nama

class Mahasiswa(models.Model):
    nama = models.CharField(max_length=50)
    nim = models.CharField(max_length=50)
    tanggal_lahir = models.CharField(max_length=50)
    photo = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    fakultas = models.CharField(max_length=50)
    prodi = models.CharField(max_length=50)

    def ___str___(self):
        return self.nama

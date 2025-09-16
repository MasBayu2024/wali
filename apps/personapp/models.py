from django.db import models

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=150)
    umur = models.IntegerField()
    kota = models.CharField(max_length=100)

    class Meta:
        db_table = 'person'
        managed = False   # set False kalau tabel sudah ada; hapus/ubah jika mau Django buat

    def __str__(self):
        return self.nama

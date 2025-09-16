from django.db import models

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=100)
    umur = models.IntegerField()
    kota = models.CharField(max_length=100)

    class Meta:
        db_table = 'person'   # gunakan tabel yang sudah ada
        managed = False       # biar Django tidak coba bikin ulang tabel

    def __str__(self):
        return self.nama

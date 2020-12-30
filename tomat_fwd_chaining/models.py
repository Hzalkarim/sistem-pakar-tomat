from django.db import models

class Gejala(models.Model):
    BENAR = 'benar'
    SALAH = 'salah'
    PILIHAN = (
        (BENAR, 'ini benar'),
        (SALAH, 'ini salah'),
    )
    kode_gejala = models.CharField(max_length=2, primary_key=True)
    konten = models.CharField(max_length=300)
    pilihan = models.CharField(max_length=10, choices=PILIHAN, default=SALAH)

class Penyakit(models.Model):
    kode_penyakit = models.CharField(max_length=2, primary_key=True)
    nama = models.CharField(max_length=200)

class Aturan(models.Model):
    BENAR = 'benar'
    SALAH = 'salah'
    PILIHAN = (
        (BENAR, 'ini benar'),
        (SALAH, 'ini salah'),
    )
    kebenaran_simpulan = models.CharField(max_length=10, choices=PILIHAN, default=SALAH)
    penyakit_simpulan = models.ForeignKey(Penyakit, on_delete=models.CASCADE)

class AturanGejala(models.Model):
    kode_gejala = models.ForeignKey(Gejala, on_delete=models.CASCADE)
    kode_aturan = models.ForeignKey(Aturan, on_delete=models.CASCADE)
